# from flask_sqlalchemy import SQLAlchemy
# from flask import Flask
# from os import path
# 
# app = Flask(__name__)
# dbUrl = path.realpath(path.dirname(path.abspath(__file__)) + '/../db/')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////%s/db.sqlite' % dbUrl
# db = SQLAlchemy(app)
# 
# 
# 
# 
# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)
#     spojHandle = db.Column(db.String(120), unique=True)
# 
#     def __init__(self, username=None, spojHandle = None):
#         self.username = username;
#         self.spojHandle = spojHandle;
# 
# class Submission(db.Model):
#     __tablename__ = 'submissions'
#     id = db.Column(db.Integer, primary_key = True);
#     judge = db.Column(db.String, primary_key = True);
#     userId = db.Column(db.Integer);
#     problemCode = db.Column(db.String);
#     memory = db.Column(db.Integer);
#     time = db.Column(db.Integer);
#     submissionDate = db.Column(db.DateTime);
#     lang = db.Column(db.String);
#     veredict = db.Column(db.String);
#     insertDate = db.Column(db.DateTime);
# 
#     def __init__(self):
#         self.id = None;
#         self.judge = None;
#         self.userId = None;
#         self.problemCode = None;
#         self.memory = None;
#         self.time = None;
#         self.submissionDate = None;
#         self.lang = None;
#         self.veredict = None;
#         self.insertDate = None;
# 
# 
# 
# # db.session.execute(User.__table__.insert(), [x.__dict__ for x in [...]])
# #.execute([a,b])
# # db.session.commit()
# print User.query.all()
        

    