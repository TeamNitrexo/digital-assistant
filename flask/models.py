import re
from flask import flash
from mongoengine import *
from werkzeug.security import generate_password_hash


class Users(Document):
    # NOTE: make HTML input fields require values to avoid setting minimum field lengths

    ### MODEL FIELDS ###
    first_name = StringField(max_length = 100)

    last_name = StringField(max_length = 100)

    user_email = EmailField(unique = True)

    user_password = StringField(max_length = 200)

    user_type = StringField(
        max_length = 200, 
        choices = {'User', 'Admin'}
    )


    ### PRIVATE ###
    fields_to_clean = [
        'first_name',
        'last_name',
        'user_email',
        'user_password'
    ]
    num_of_fields = len(fields_to_clean)


    def hash_password(self, unhashed_password:str):
        return generate_password_hash(
            password = unhashed_password,
            method = 'pbkdf2:sha256',
            salt_length = 16
        )


    def clean(self):
        # removes leading/trailing spaces
        for i in range(self.num_of_fields):
            prop = self.fields_to_clean[i]
            value = self[prop]

            self[prop] = value.strip()

        self['user_password'] = self.hash_password(self['user_password'])

        super().clean()


    def update(self, **updatedInfo):
        num_of_invalid_updates = 0
        passwordIsUpdated = True

        for i in range(self.num_of_fields):
            currentProperty = self.fields_to_clean[i]
            new_value = updatedInfo[currentProperty]

            # if there is no update to a field, the old value is used
            if len(new_value) == 0 or re.compile('^\s+$').match(new_value) != None:
                if currentProperty == 'user_password':
                    passwordIsUpdated = False

                updatedInfo[currentProperty] = self[currentProperty]

                num_of_invalid_updates += 1

            # removes leading/trailing spaces 
            if currentProperty in updatedInfo:
                updatedInfo[currentProperty] = updatedInfo[currentProperty].strip()

        if passwordIsUpdated:
            updatedInfo['user_password'] = self.hash_password(updatedInfo['user_password'])

        # stores temporary flash messages for use in template
        if num_of_invalid_updates == len(self.fields_to_clean):
            flash(
                message = "No updates occurred",
                category = "info"
            )
        else:
            flash(
                message = "Successfully updated user",
                category = "success"
            )

        super().update(**updatedInfo)


class ThermalQnA(Document):
    question = StringField(
        min_length=2, # character + question mark
    )

    answer = StringField(min_length=1)


class Links(EmbeddedDocument):
    value = BooleanField()

    valueTrue = StringField(max_length = 200)

    valueFalse = StringField(max_length = 200)

    dependentOnThisParameter = BooleanField()


class SingleTask(EmbeddedDocument):
    task_name = StringField(
        max_length = 200,
        required = True
    )

    field_type = StringField(
        max_length = 200,
        required = True
    )

    uploaded = EmbeddedDocumentField(Links)

    required = BooleanField()

    file_type = StringField(max_length = 200)

    value = StringField(max_length=1000)

    valuePresent = EmbeddedDocumentField(Links)

    addToIni = ListField(StringField(max_length = 200))

    onlyAddIni = BooleanField()

    nextTask = StringField(max_length = 200)


class SinasJobTemplates(Document):
    task = StringField(
        max_length = 200,
        required = True
    )

    job_id = StringField(
        max_length = 200,
        required = True
    )

    next_action = StringField(
        max_length = 200,
        required = True
    )

    template = ListField(EmbeddedDocumentField(SingleTask))

    job_owner = StringField(
        max_length = 200,
        required = True, 
        default = "template"
    )

    job_status = StringField(
        max_length = 200,
        required = True,
        default = "Queued"
    )
