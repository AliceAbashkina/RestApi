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

if __name__ == '__main__':
    app.run()
