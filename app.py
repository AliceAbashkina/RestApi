from flask import Flask, jsonify, request 
from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy.dialects.postgresql import JSON, BIGINT, VARCHAR

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)
app = Flask(__name__)
if __name__ == '__main__':
    app.run()
