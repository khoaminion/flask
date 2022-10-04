from app import db
from sqlalchemy import Sequence
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    user_id = db.Column(db.Integer, Sequence('user_id_seq'), primary_key= True)
    first_name = db.Column(db.String(64), index = True, nullable = False)
    last_name = db.Column(db.String(64), index = True, nullable = False)
    email = db.Column(db.String(120), index = True, unique = True, nullable = False)
    password_hash = db.Column(db.String(128),nullable = False)

    def __repr__(self):
        return '<User full name: {} {}, email: {}>'.format(self.first_name, self.last_name, self.email)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)