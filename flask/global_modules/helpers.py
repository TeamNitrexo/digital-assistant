#####################
### Dependencies ###
####################
import json, requests, os
from copy import deepcopy


### LOCAL MODULES ###
import global_modules.config
from global_modules.data import main_menu_buttons
from tmr import *
from fabric import Connection


### FLASK DEPENDENCIES ###
from flask import jsonify, session


### DATABASE DEPENDENCIES ###
import models
from global_modules.database import col_messages





################
### Helpers ###
###############
def checkIfDictContainsAllProperties(dictionary:dict, properties:list):
    return all([True for prop in properties if dictionary.get(prop) is not None])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in global_modules.config.ALLOWED_EXTENSIONS



# pops all session variables except for username
def pop_session():
    session.pop('no_response', None)
    session.pop('sinas_job_id', None)
    session.pop('tmr_job_id', None)
    session.pop('task', None)
    session.pop('branch', None)
    session.pop('branch_set', None)

    return None

def replace_value_variable(message_list, value):
    if value is None or value == '':
        return message_list

    new_message_list = []

    for message in message_list:
        new_message_list.append(message.replace('$value', value))

    return new_message_list



# run job til response; loop til session['no_response'] is unset 
def run_job_till_response():
    response = run_job(session['sinas_job_id'])

    if 'no_response' in session:
        while('no_response' in session):
            response = run_job(session['sinas_job_id'])

    return response



# creates new SINAS job from template
def create_sinas_job_from_template(job_template):
    new_job = deepcopy(job_template)
    new_job.id = None

    new_job.save()

    new_job.job_id = str(new_job.id)
    new_job.job_owner = session['username']
    new_job.job_status = "Incomplete"

    new_job.save()

    session['sinas_job_id'] = new_job.job_id

    return None



# creates new TMR job from template
def create_tmr_job_from_template(job_template):
    new_job = deepcopy(job_template)
    new_job.id = None

    new_job.save()

    new_job.job_id = str(new_job.id)
    new_job.job_owner = session['username']
    new_job.job_status = "Incomplete"

    new_job.save()

    session['tmr_job_id'] = new_job.job_id

    return None



# initialize new job
def init_job(sinas_job_id):
    path = '/uploads/' + session['sinas_job_id']

    try: 
        os.mkdir(path) 
    except OSError as error: 
        print(error)

    task = session['task']
    task = 'task=' + task
    init_ini_lines = ["[demo]",task]

    write_to_ini(init_ini_lines)

    return None

def init_tmr_job(tmr_job_id):
    path = '/uploads/' + session['tmr_job_id']

    try: 
        os.mkdir(path) 
    except OSError as error: 
        print(error)

    return None

def write_to_ini(lines):
    if not lines is None:
        if len(lines) > 0:
            path = "/uploads/" + session['sinas_job_id'] + "/" + session['sinas_job_id'] + ".ini"

            with open(path, mode = 'a+', encoding = 'utf-8') as myfile:
                myfile.write('\n'.join(lines))

                myfile.write('\n')

    return None



def get_rasa_response(question):
    data = json.dumps({"sender": "Rasa","message": question})

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    res = requests.post(
        # 'http://rasa-service:5005/webhooks/rest/webhook',
        url = 'http://localhost:5005/webhooks/rest/webhook',
        data = data,
        headers = headers
    )

    res = res.json()
    val = res[0]['text']

    if val == "I'm sorry, I did not understand the question. Could you please rephrase the Question?":
        rasa_reply = {
            "message": [{
                'type': 'text',
                "content": "I'm sorry, I did not understand the question. Please rephrase the question."
            }],
            "buttons": main_menu_buttons
        }
    else:
        rasa_reply = {
            "message": [{
                'type': 'text',
                'content': val
            }],
            "buttons": main_menu_buttons
        }

    response = jsonify(rasa_reply)

    print(response)

    return response



# run SINAS and TMR jobs
def run_job(sinas_job_id):
    job_template = models.SinasJobTemplates.objects.get(job_id = sinas_job_id)

    if job_template.next_action == 'run_pysinas':
        job_template.job_status = "Incomplete"

        job_template.save()

        try:
            c = Connection(
                host="root@ubuntu-wine", 
                port=22,
                connect_kwargs={"password": "ubuntupassword"}
            )

            ssh_command = "cd /jobs/" + session['sinas_job_id']

            ssh_command = ssh_command + " && "

            sinas_command = "wine /pysinas/bin/run_pysinas.exe --job=" + session['sinas_job_id'] + ".ini"

            ssh_command = ssh_command + sinas_command

            job_template.job_status = "Completed"

            job_template.save()

            job_successful = {
                "message": [{
                    'type': 'text',
                    'content': 'The sinas task ran successfully.'
                },
                {
                    'type': 'html',
                    'content': 'Click on this <a href="/download/'+ str(session['sinas_job_id']) +'" target="_blank">link</a> to download the files.'
                },
                {
                    'type': 'text',
                    'content': 'What would you like to do next?'
                }],
                "buttons": main_menu_buttons
            }

            response = jsonify(job_successful)

            pop_session()

            return response
        except Exception as e:
            if 'no_response' in session:
                session.pop('no_response')

            job_unsuccessful = {
                "message": [{
                    'type': 'text',
                    'content': 'Could not complete the sinas task.'
                },
                {
                    'type': 'text',
                    'content': 'What would you like to do next?'
                }],
                "buttons": main_menu_buttons
            }

            response = jsonify(job_unsuccessful)

            pop_session()

            return response

    if job_template.next_action == 'run_tmr':
        job_template.job_status = "Incomplete"

        job_template.save()

        try:
            job_template.job_status = "Completed"

            job_template.save()

            job_successful = {
                "message": [{
                    'type': 'text',
                    'content': 'The TMR task ran successfully.'
                },
                {
                    'type': 'html',
                    'content': 'Click on this <a href="/download/'+ str(session['tmr_job_id']) +'" target="_blank">link</a> to download the files.'
                },
                {
                    'type': 'text',
                    'content': 'What would you like to do next?'
                }],
                "buttons": main_menu_buttons
            }

            response = jsonify(job_successful)

            pop_session()

            return response
        except Exception as e:
            if 'no_response' in session:
                session.pop('no_response')

            job_unsuccessful = {
                "message": [{
                    'type': 'text',
                    'content': 'Could not complete the TMR task.'
                },
                {
                    'type': 'text',
                    'content': 'What would you like to do next?'
                }],
                "buttons": main_menu_buttons
            }

            response = jsonify(job_unsuccessful)

            pop_session()

            return response

    for i in range(len(job_template.template)):
        if job_template.template[i].task_name == job_template.next_action:
            action_id = i

    if job_template.template[action_id].onlyAddIni:
        write_to_ini(job_template.template[action_id].addToIni)

        job_template.next_action = job_template.template[action_id].nextTask

        job_template.save()

        session['no_response'] = 'True'

        return 'Add to INI file'

    if job_template.template[action_id].uploaded.dependentOnThisParameter:
        response_message = session['task'] + "_" + job_template.next_action

        db_reply = col_messages.find_one({"name": response_message})

        response = jsonify(db_reply['data'])

        if 'no_response' in session:
            session.pop('no_response')

        return response # dependent on File Upload

    if job_template.template[action_id].valuePresent.dependentOnThisParameter:
        response_message = session['task'] + "_" + job_template.next_action

        db_reply = col_messages.find_one({"name": response_message})
        response = jsonify(db_reply['data'])

        if 'no_response' in session:
            session.pop('no_response')

        return response # dependent on value: True, False or text'

    for i in range(len(job_template.template)):
        if job_template.template[i].task_name == job_template.next_action:
            action_id = i

    if job_template.template[action_id].uploaded:
        job_template.next_action = 'ovl'

        job_template.save()

        db_reply = col_messages.find_one({"name": 'branch_two_upload_ovl_file'})

        response = jsonify(db_reply['data'])

        if 'no_response' in session:
            session.pop('no_response')

        return response
    else:        
        if not job_template.template[action_id].uploaded:
            db_reply = col_messages.find_one({"name": 'branch_two_upload_bdf_file'})

            response = jsonify(db_reply['data'])

            if 'no_response' in session:
                session.pop('no_response')

            return response
