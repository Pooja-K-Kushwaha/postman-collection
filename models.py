from flask_sqlalchemy import SQLAlchemy
import json
db = SQLAlchemy()
 
class TableModel(db.Model):
    __table_args__ = {'schema': 'settings'}
    __tablename__ = 'user_acceptance'
    
    app_id = db.Column(db.String(80),primary_key=True)
    user_id = db.Column(db.String(80),primary_key=True)
    version=db.Column(db.Integer,primary_key=True)
    tstamp=db.Column(db.DateTime,primary_key=True)
    action=db.Column(db.String(80))
 
    def __init__(self,app_id,user_id,version,tstamp,action):
        self.app_id = app_id      #to remove for (auto-increment)
        self.user_id =user_id
        self.version=version
        self.tstamp=tstamp
        self.action=action
     
    def json1(self):
        return {"app_id":self.app_id, "user_id":self.user_id, "version":self.version  ,"tstamp":str(self.tstamp), "action":self.action}


class Accepted_entries(db.Model):
    __bind_key__ = "local"
    __table_args__ = {'schema': 'public'}
    __tablename__ = 'user_acceptance_accepted_entries'
    int_id = db.Column(db.Integer, primary_key=True)
    int_user_id = db.Column(db.Integer, nullable=False)
    txt_action_type = db.Column(db.Text, nullable=False)
    app_id = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.String(255), nullable=False)
    version = db.Column(db.Integer, nullable=False)
    tstamp = db.Column(db.DateTime, nullable=False)
    action = db.Column(db.String(255), nullable=False)
    def __init__(self, int_user_id, txt_action_type, app_id, user_id, version, tstamp, action):
        self.int_user_id = int_user_id
        self.txt_action_type = txt_action_type
        self.app_id = app_id
        self.user_id = user_id
        self.version = version
        self.tstamp = tstamp
        self.action = action
    def json1(self):
        return {"int_user_id":self.int_user_id,"txt_action_type":self.txt_action_type,"app_id":self.app_id, "user_id":self.user_id, "version":self.version, 
                "tstamp":str(self.tstamp), "action":self.action}

class Master_entries(db.Model):
    __bind_key__ = "master"
    __table_args__ = {'schema': 'public'}
    __tablename__ = 'master_user'
    int_user_id = db.Column(db.Integer, primary_key=True)
    user_name= db.Column(db.Integer, nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    def __init__(self,user_name,active):
        self.user_name=user_name
        self.active=active
    
    def json2(self):
        return {"int_user_id":self.int_user_id,"user_name":self.user_name, "active":self.active}




    
    