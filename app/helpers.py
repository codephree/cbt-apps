from flask import abort, current_app
from flask_login import login_required, current_user
from app.extensions import db, bcrypt
from app.models.user import User
from app.models.question import Question
import os
from sqlalchemy import exc


class Helper:

    def __init__(self):
        self.name = 'I am helper class to save all the function'
        self.ALLOWED_EXTENSIONS = {'csv', 'txt', 'psv'}

    def check_admin(self):
        if current_user.is_authenticated and current_user.is_admin != 1:
         abort(404)

    def check_not_admin(self):
        if current_user.is_authenticated and current_user.is_admin == 1:
         abort(404)
    

    def allowed_file(self,filename):
         return '.' in filename and \
         filename.rsplit('.', 1)[1].lower() in self.ALLOWED_EXTENSIONS

    def OtbData(self,filename):
            fileObj = open(os.path.join(
                current_app.root_path,
                current_app.config['UPLOAD_FOLDER'],
                filename
            ), "r")
            words = fileObj.read().splitlines() #puts the file into an array
            fileObj.close()
            data_to_upload = []
            for data in words:
               data_to_upload.append(data.split(','))
            return data_to_upload
    
    def do_bulk_user(self,filename):
        data = self.OtbData(filename)
        try:
            for sublist in data: 
                user = User(**{
                    "firstname": sublist[0],
                    "lastname": sublist[1],
                    "email": sublist[2],
                    "password": bcrypt.generate_password_hash(sublist[3]),
                })
                db.session.add(user)
            db.session.commit()
            return True
        except exc.IntegrityError as Error:
           return False
        
    def do_bulk_question(self, filename):
        data = self.OtbData(filename)
        try:
            for sublist in data: 
                question = Question(**{
                    "question": sublist[0],
                    "options": sublist[1],
                    "is_right": sublist[2]
                })
                db.session.add(question)
            db.session.commit()
            return True
        except exc.IntegrityError as Error:
           return False
        
    def split_string_to_radio(self, string):
         string_to_array = []
         string_to_array.append(string.split('|'))
         return string_to_array
        
        
        