from flask import Flask, jsonify, request 
from flask_sqlalchemy import SQLAlchemy
import os
from config import DevelopmentConfig
from flask_migrate import Migrate
from flask_marshmallow  import Marshmallow
from sqlalchemy.dialects.postgresql import JSON, BIGINT, VARCHAR

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate()
migrate.init_app(app,db)
ma = Marshmallow(app)
class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.BIGINT, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    password = db.Column(db.String(64))
    
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<id {}>'.format(self.id)   

if __name__ == '__main__':
    app.run()
