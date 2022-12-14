#####################
### Dependencies ###
####################
import os, zipfile, io, pathlib, shutil, mimetypes
from functools import wraps


### LOCAL MODULES ###
import global_modules.config
from global_modules.database import col_messages 
from tmr import *
from global_modules.helpers import *
from global_modules.data import no_user_found


### FLASK DEPENDENCIES ###
from flask import Flask, render_template, session, jsonify, request, send_file, redirect, url_for, send_from_directory, flash


### MONGO DATABASE MODELS ###
import models


### SECURITY DEPENDENCIES ###
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash






#######################
### Initialization ###
######################
mimetypes.add_type('application/javascript', '.js')

app = Flask(__name__)
app.secret_key = global_modules.config.SECRET_KEY


### FLASK APP CONFIGURATIONS ###
app.config['UPLOAD_FOLDER'] = global_modules.config.UPLOAD_FOLDER


### VIEW DECORATORS ###
def login_required(viewFunction):
    @wraps(viewFunction)
    def checkIfLoggedIn():
        if 'username' not in session:
            return redirect(url_for('login'))

        return viewFunction()

    return checkIfLoggedIn

def admin_login_required(viewFunction):
    @wraps(viewFunction)
    def checkIfAdmin(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))

        queryset = models.Users.objects(user_email__exact = session['username'])

        if queryset.count() != 1 or queryset[0].user_type != "Admin":
            return redirect(url_for('index'))

        return viewFunction(*args, **kwargs, admin_user = queryset[0])

    return checkIfAdmin






####################
### Flask Routes ###
####################

# DIGITAL ASSISTANT
@app.route('/')
@login_required
def index():
    current_user = models.Users.objects(user_email__exact = session['username'])[0]

    # temp?
    session['branch_set'] = False
    session['branch'] = ''

    return render_template(
        'Nchatbot.html',
        current_user = current_user
    )


@app.route('/message')
@login_required
def message():
    reply = request.args.get('reply')
    question = request.args.get('question')

    if reply:
        if reply == 'branch_options':
            session['branch'] = ''
            session['branch_set'] = False

            db_reply = col_messages.find_one({"name": 'branch_options_response_body'})

            response = jsonify(db_reply['data'])

        if reply in ['Thermo-Elastic Verification', 'Temperature Mapping', 'Ask Questions', 'models.Tutorials', 'Perform TMR', 'Thermal Model Reduction']:
            session['branch'] = reply
            session['branch_set'] = True

        if session['branch'] == 'Thermo-Elastic Verification':
            if reply == 'branch_one_options':
                db_reply = col_messages.find_one({"name": 'branch_one_options_response_body'})

                response = jsonify(db_reply['data'])
            elif reply == 'GMM':
                db_reply = col_messages.find_one({"name": 'branch_one_gmm'})

                response = jsonify(db_reply['data'])
            elif reply == 'TMM':
                db_reply = col_messages.find_one({"name": 'branch_one_tmm'})

                response = jsonify(db_reply['data'])
            elif reply == 'SM':
                db_reply = col_messages.find_one({"name": 'branch_one_sm'})

                response = jsonify(db_reply['data'])
            elif reply == 'TM':
                db_reply = col_messages.find_one({"name": 'branch_one_tm'})

                response = jsonify(db_reply['data'])
            else:
                db_reply = col_messages.find_one({"name": 'branch_one_response_body'})

                response = jsonify(db_reply['data'])

        if session['branch'] == 'Thermal Model Reduction':
            db_reply = col_messages.find_one({"name": 'branch_thermal_model_reduction'})

            response = jsonify(db_reply['data'])

        if session['branch'] == 'Ask Questions' or reply == 'branch_three':
            db_reply = col_messages.find_one({"name": 'branch_three_ask'})

            response = jsonify(db_reply['data'])

        if session['branch'] == 'Temperature Mapping' or reply == 'branch_two_task_options_response_body':
            if reply == 'branch_two_task_options_response_body' or reply == 'Temperature Mapping':
                db_reply = col_messages.find_one({"name": 'branch_two_task_options_response_body'})

                response = jsonify(db_reply['data'])

                print('DDDDDDDDD')

                if 'sinas_job_id' in session:
                    session.pop('sinas_job_id')
            else:
                if reply in ['allinone', 'conductorgen', 'csv2tdf', 'gradinterpol', 'gradprep', 'interpolate', 'matgen']:
                    session['task'] = reply

                if 'task' in session:
                    if not 'sinas_job_id' in session:
                        job_template = models.SinasJobTemplates.objects.get(
                            task=session['task'], 
                            job_id='template'
                        )

                        create_sinas_job_from_template(job_template)

                        init_job(session['sinas_job_id'])

                        response = run_job_till_response()
                    else:
                        response = run_job_till_response()

        if session['branch'] == 'models.Tutorials' or reply == 'branch_tutorials':
            tutorials_count = models.Tutorials.objects.count()

            if tutorials_count == 0:
                response_json = {
                    "message": [{
                                'type': 'text',
                                'content': "No tutorials available."
                            }           
                    ],
                    "buttons": main_menu_buttons
                }

                response = jsonify(response_json)
            else:
                tutorials = models.Tutorials.objects()

                if reply == 'branch_tutorials' or reply == 'models.Tutorials':
                    # reply with list of tutorials
                    buttons = []

                    for tutorial in tutorials:
                        item = {}
                        item["text"] = tutorial.name
                        item["value"] = "tutorial_" + str(tutorial.id)
                        buttons.append(item)

                    response_json = {
                        "message": [{
                            'type': 'text',
                            'content': "Choose the tutorial."
                        }],
                        "buttons": buttons
                    }

                    response = jsonify(response_json)
                else:
                    if reply in ["tutorial_" + str(tutorial.id) for tutorial in tutorials]:
                        # reply with Chapter number
                        tutorial_id = reply.split("_")[1]
                        session["tutorial"] = tutorial_id

                        chapters = models.Videos.objects(tutorial_id_reference=tutorial_id).distinct(field="chapter_number")

                        buttons = []

                        for chapter in chapters:
                            item = {}
                            item["text"] = str(chapter)
                            item["value"] = "chapter_" + str(chapter)
                            buttons.append(item)

                        response_json = {
                            "message": [{
                                'type': 'text',
                                'content': "Choose the chapter."
                            }],
                            "buttons": buttons
                        }

                        response = jsonify(response_json)

                    else:
                        if "chapter_" in reply:
                            # reply with lesson numbers
                            chapter_number = reply.split("_")[1]
                            session["chapter_number"] = chapter_number

                            lessons = models.Videos.objects(tutorial_id_reference=session["tutorial"], chapter_number = session["chapter_number"]).distinct(field="lesson_number")

                            buttons = []

                            for lesson in lessons:
                                item = {}
                                item["text"] = lesson
                                item["value"] = "lesson_" + str(lesson)
                                buttons.append(item)

                            response_json = {
                                "message": [{
                                    'type': 'text',
                                    'content': "Choose the lesson."
                                }],
                                "buttons": buttons
                            }

                            response = jsonify(response_json)
                        else:
                            if "lesson_" in reply:
                                # send video
                                lesson_number = reply.split("_")[1]
                                session["lesson_number"] = lesson_number

                                video = models.Videos.objects.get(
                                    tutorial_id_reference=session["tutorial"], 
                                    chapter_number = session["chapter_number"],
                                    lesson_number = session["lesson_number"]
                                )

                                video_html = """
                                    <video width="320" height="240" controls>
                                        <source src="{}" type="video/mp4">

                                        Your browser does not support the video tag.
                                    </video>
                                """.format(video.video_url)

                                response_json = {
                                    "message": [{
                                        'type': 'html',
                                        'content': video_html
                                    }],
                                    "buttons": main_menu_buttons
                                }

                                response = jsonify(response_json)

                                ## pop session variables
                                session.pop('tutorial', None)
                                session.pop('chapter_number', None)
                                session.pop('lesson_number', None)
                            else:
                                response_json = {
                                    "message": [{
                                        'type': 'text',
                                        'content': "Something went wrong. What would you like to do next?"
                                    }],
                                    "buttons": main_menu_buttons
                                }
                                response = jsonify(response_json)

        if session['branch'] == "Perform TMR" or reply == "Perform TMR":
            session.pop('sinas_job_id', None)
            session.pop('tmr_job_id', None)
            session['task'] = 'perform_tmr'

            if 'task' in session:
                if not 'tmr_job_id' in session:
                    response = {
                        "message": [{
                            'type': 'text',
                            'content': 'Some Reply'
                        }]
                    }

                    response = jsonify(response)

                    job_template = models.SinasJobTemplates.objects.get(task=session['task'], job_id='template')

                    create_tmr_job_from_template(job_template)

                    init_tmr_job(session['tmr_job_id'])

                    response = run_job(session['tmr_job_id'])
                    response = jsonify(response)
                else:
                    response = {
                        "message": [{
                            'type': 'text',
                            'content': 'Some Else Reply'
                        }]}

                    response = jsonify(response)

    if question:
        response = get_rasa_response(question)

    response.headers.add("Access-Control-Allow-Origin", "*")

    return response


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if not 'username' in session:
        session.pop('username')
        return jsonify(no_user_found)

    if session.get('tmr_job_id'):
        if request.method == 'POST':
            # check if the post request has the file part
            if 'file' not in request.files:
                return { 'status' : 'File not present.'}

            file = request.files['file']

            # if user does not select file, submit an empty part without filename
            if file.filename == '':
                return { 'status' : 'File name invalid.'}

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                new_filename = "file" + os.path.splitext(filename)[1]

                file.save(os.path.join(app.config['UPLOAD_FOLDER'], session['tmr_job_id'], new_filename))

                job_template = models.SinasJobTemplates.objects.get(job_id = session['tmr_job_id'])

                for i in range(len(job_template.template)):
                    if job_template.template[i].task_name == job_template.next_action:
                        action_id = i

                job_template.template[action_id].uploaded.value = True
                job_template.template[action_id].value = new_filename

                if job_template.template[action_id].uploaded.dependentOnThisParameter:
                    job_template.next_action = job_template.template[action_id].uploaded.valueTrue

                job_template.save()

        response = run_job(job_template.job_id)

        return response

    if session.get('sinas_job_id'):
        if request.method == 'POST':
            # check if the post request has the file part
            if 'file' not in request.files:
                return { 'status' : 'File not present.'}

            file = request.files['file']

            # if user does not select file, submit an empty part without filename
            if file.filename == '':
                return { 'status' : 'File name invalid.'}

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                new_filename = "file" + os.path.splitext(filename)[1]

                file.save(os.path.join(app.config['UPLOAD_FOLDER'], session['sinas_job_id'], new_filename))

                job_template = models.SinasJobTemplates.objects.get(job_id = session['sinas_job_id'])

                for i in range(len(job_template.template)):
                    if job_template.template[i].task_name == job_template.next_action:
                        action_id = i

                job_template.template[action_id].uploaded.value = True
                job_template.template[action_id].value = new_filename

                if job_template.template[action_id].uploaded.dependentOnThisParameter:
                    job_template.next_action = job_template.template[action_id].uploaded.valueTrue

                    write_to_ini(replace_value_variable(job_template.template[action_id].addToIni, job_template.template[action_id].value))

                job_template.save()

        response = run_job(job_template.job_id)

        if 'no_response' in session:
            while('no_response' in session):
                response = run_job(session['sinas_job_id'])

        return response
    else:
        # return to main task if job id doesn't exist in session
        pass


@app.route('/tutorials/<tutorial_id>/<chapter>/<lesson>/<filename>' , methods=["GET", "POST"])
def send_tutorial_video(tutorial_id, chapter, lesson, filename):
    folder = "/tutorials/" + tutorial_id + "/" + chapter + "/" + lesson

    return send_from_directory(
        folder,
        filename,
        as_attachment = False
    )



# ACCOUNT LOGIN/LOGOUT & PROFILE
@app.route('/logout')
@login_required
def logout():
    session.clear()

    return redirect(url_for('login'))


@app.route('/login',  methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        queryset = models.Users.objects(user_email__exact = email)

        if queryset.count() == 1 and check_password_hash(queryset[0].user_password, password):
                session['username'] = email # !change

                return redirect(url_for('index'))
        else:
            flash(
                message = "Invalid credentials",
                category = 'danger'
            )

    return render_template('login.html')



# USER/ADMIN PAGES
@app.route('/profile' , methods=["GET", "POST"])
@login_required
def user_profile():
    user = models.Users.objects.get(user_email = session['username'])

    if request.method == "GET":
        return render_template(
            "update_profile.html",
            current_user = user
        )
    elif request.method == "POST":
        user.update(
            id = user.id, 
            first_name = request.form['user_first_name'],
            last_name = request.form['user_last_name'], 
            user_email = request.form['user_email'], 
            user_password = request.form['user_password']
        )

        return redirect(url_for('user_profile'))


@app.route('/admin')
@admin_login_required
def admin_dashboard(admin_user):
    user_count = models.Users.objects.count()
    conversation_count = models.Conversations.objects.count()
    job_count = models.SinasJobTemplates.objects.count()

    return render_template(
        'dashboard.html', 
        current_user = admin_user, # this object is provided by the decorator 
        user_count = user_count, 
        conversation_count = conversation_count, 
        job_count = job_count
    )


@app.route('/admin/users')
@admin_login_required
def admin_users_dashboard(admin_user):
    page = request.args.get('page')

    if page:
        try:
            page_nb = int(page)
        except:
            page_nb = 0

        if page_nb < 1:
            page_nb = 1
    else:
        page_nb = 1

    items_per_page = 10 
    offset = (page_nb - 1) * items_per_page

    user_count = models.Users.objects.count()

    if offset > user_count:
        offset = user_count // items_per_page

    if (offset + items_per_page) > user_count:
        next_page = None
    else:
        next_page = (offset // items_per_page) + 2

    if offset == 0:
        previous_page = None
    else:
        previous_page = (offset // items_per_page)

    users = models.Users.objects.skip(offset).limit(items_per_page)

    return render_template(
        'users.html',
        users = users, 
        next_page = next_page, 
        previous_page = previous_page, 
        current_user = admin_user,
        page_nb = page_nb
    )


@app.route('/admin/users/add' , methods = ["GET", "POST"])
@admin_login_required
def admin_user_add(admin_user):
    if request.method == "GET":
        return render_template(
            "adduser.html", 
            current_user = admin_user
        )
    elif request.method == "POST":
        new_user = models.Users(
            first_name = request.form['user_first_name'], 
            last_name = request.form['user_last_name'], 
            user_email = request.form['user_email'], 
            user_password = request.form['user_password'], 
            user_type = request.form['user_type']
        )
        new_user.save()

        return render_template(
            'adduser.html', 
            warningmessage = "User added successfully.", 
            current_user = admin_user
        )


@app.route('/admin/users/delete/<id>')
@admin_login_required
def admin_user_delete(id, **_):
    """
    NOTE:
    The _ is a placeholder for the 'admin_user' argument passed by the decorator. The ** means that the placeholder catches multiple key-value arguments (i.e. kwargs), which is what the 'admin_user' is. Placeholders are used for ignoring arguments passed to a function.

    """

    user_to_delete = models.Users.objects(id__exact = id)[0]

    if session['username'] == user_to_delete.user_email:
        session.pop('username')

    user_to_delete.delete()

    return redirect(url_for("admin_users_dashboard"))


@app.route('/admin/users/edit/<id>' , methods = ["GET", "POST"])
@admin_login_required
def admin_user_edit(id, admin_user):
    user_to_edit = models.Users.objects.get(id = id)

    if request.method == "GET":
        return render_template(
            "edituser.html", 
            user = user_to_edit, 
            current_user = admin_user
        )
    elif request.method == "POST":
        user_to_edit.update(
            id = id,
            first_name = request.form['user_first_name'], 
            last_name = request.form['user_last_name'], 
            user_email = request.form['user_email'], 
            user_password = request.form['user_password'],
            user_type = request.form['user_type'] 
        )

        return redirect(url_for(
            'admin_user_edit',
            id = id,
            admin_user = admin_user
        ))



# SINAS JOBS
@app.route('/myjobs')
@login_required
def myjobs():
    current_user = models.Users.objects.get(user_email = session['username'])

    page = request.args.get('page')

    if page:
        try:
            page_nb = int(page)
        except:
            page_nb = 0
        if page_nb < 1:
            page_nb = 1
    else:
        page_nb = 1

    items_per_page = 10 
    offset = (page_nb - 1) * items_per_page

    job_count = models.SinasJobTemplates.objects(job_owner=session['username']).count()

    if offset > job_count:
        offset = job_count // items_per_page

    if (offset + items_per_page) > job_count:
        next_page = None
    else:
        next_page = (offset // items_per_page) + 2

    if offset == 0:
        previous_page = None
    else:
        previous_page = (offset // items_per_page)

    jobs = models.SinasJobTemplates.objects(job_owner=session['username']).skip( offset ).limit( items_per_page )

    return render_template(
        'sinas_jobs.html',
        jobs = jobs,
        next_page = next_page, 
        previous_page = previous_page,
        current_user = current_user,
        page_nb = page_nb
    )


@app.route('/sinas/delete/<id>')
def delete_myjob(id):
    if 'username' in session:
        job = models.SinasJobTemplates.objects.get(id = id)

        if job:
            if job.job_owner == session['username']:
                # delete files
                shutil.rmtree(
                    "/uploads/"+id,
                    ignore_errors=True
                )

                # delete from database
                job.delete()

                return redirect(request.referrer)
            else:
                return redirect(request.referrer)
        else:
            return redirect(request.referrer)


@app.route('/download/<sinas_job_id>')
def download_zip(sinas_job_id):
    job_path = "/uploads/" + str(sinas_job_id) + "/"
    base_path = pathlib.Path(job_path)
    data = io.BytesIO()

    with zipfile.ZipFile(data, mode='w') as z:
        for f_name in base_path.iterdir():
            z.write(f_name)

    data.seek(0)
    zip_filename = str(sinas_job_id) + ".zip"

    return send_file(
        data,
        mimetype='application/zip',
        as_attachment=True,
        attachment_filename=zip_filename
    )


@app.route('/sinas')
def sinas():
    button_input = request.args.get('button')
    text_input = request.args.get('text')

    if 'sinas_job_id' in session:    
        if button_input:
            job_template = models.SinasJobTemplates.objects.get(job_id = session['sinas_job_id'])

            for i in range(len(job_template.template)):
                if job_template.template[i].task_name == job_template.next_action:
                    action_id = i

            job_template.template[action_id].value = str(button_input)

            job_template.template[action_id].valuePresent.value = True

            if job_template.template[action_id].valuePresent.dependentOnThisParameter:
                if job_template.template[action_id].value == "true":
                    job_template.next_action = job_template.template[action_id].valuePresent.valueTrue
                elif job_template.template[action_id].value == "false":
                    job_template.next_action = job_template.template[action_id].valuePresent.valueFalse
                else:
                    job_template.next_action = job_template.template[action_id].valuePresent.valueTrue

                write_to_ini(replace_value_variable(job_template.template[action_id].addToIni, job_template.template[action_id].value))

            job_template.save()
        elif text_input:
            job_template = models.SinasJobTemplates.objects.get(job_id = session['sinas_job_id'])

            for i in range(len(job_template.template)):
                if job_template.template[i].task_name == job_template.next_action:
                    action_id = i

            job_template.template[action_id].value = text_input

            job_template.template[action_id].valuePresent.value = True

            if job_template.template[action_id].valuePresent.dependentOnThisParameter:
                job_template.next_action = job_template.template[action_id].valuePresent.valueTrue

                write_to_ini(replace_value_variable(job_template.template[action_id].addToIni, job_template.template[action_id].value))

            job_template.save()
        else:   
            response = run_job(session['sinas_job_id'])

        if 'no_response' in session:
            while('no_response' in session):
                response = run_job(session['sinas_job_id'])

        return response



# !development
@app.route('/video' , methods=["GET", "POST"])
def test_video():
    current_user = models.Users.objects.get(user_email = session['username'])

    chapters = models.Videos.objects(tutorial_id_reference="5ffde0045c2f9acd0144c1d1").distinct(field="chapter_number")

    if 'username' in session:
        user = models.Users.objects.get(user_email = session['username'])

        video_url = url_for('static', filename="videos/Chapter1_Lesson1_Geometry_Simplification_v0.1.mp4")

        return render_template(
            'test_video.html', 
            video_url = video_url, 
            current_user = current_user
        )
    else:
        return redirect(url_for('login'))

# !development
@app.route('/ru')
def reset_users():
    session.clear()
    models.Users.objects.delete()

    admin1Account = models.Users(
        first_name = 'test admin',
        last_name = '1',
        user_email = 'admin1@nitrexo.com',
        user_password = '1',
        user_type = 'Admin'
    )
    admin1Account.save()

    admin2Account = models.Users(
        first_name = 'test admin',
        last_name = '2',
        user_email = 'admin2@nitrexo.com',
        user_password = '1',
        user_type = 'Admin'
    )
    admin2Account.save()

    userAccount = models.Users(
        first_name = 'test',
        last_name = 'user',
        user_email = 'user@nitrexo.com',
        user_password = '1',
        user_type = 'User'
    )
    userAccount.save()

    return redirect(url_for('login'))






if __name__ == '__main__':
    app.run(debug = True) # !development