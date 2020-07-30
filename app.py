from flask import Flask, render_template, redirect,jsonify
from flask_pymongo import PyMongo
import json

# Needed if we switch to postgres versus mongoDB
#from flask_sqlalchemy import SQLAlchemy
from os import environ
from pprint import pprint

app = Flask(__name__)

#uncomment the two lines string below to connect locally to the remote MongoDB

app.config["MONGO_URI"] = environ.get('MONGODB_URI') 

# Use flask_pymongo to set up mongo connection

#app.config["MONGO_URI"] = environ.get('MONGODB_URI')
mongo = PyMongo(app)

@app.route("/")
def index():
   # aqi_info = mongo.db.geo_with_nas.find_all()
    # how to tie this to the map logic where the data needs to come from mongoDB
    return render_template("index.html", test="passing a value works")


@app.route("/aqidata")
def aqidata():
    aqi_datas = mongo.db.geo_with_nas.find()
    # for document in aqi_datas: 
    #     pprint(document)
    features = []
    for aqi_data in aqi_datas:
     
        features.append(aqi_data['features'])
    geojson = {"type":"FeatureCollection",
    "features":features}
    
    return jsonify(geojson)
    

if __name__ == "__main__":
    app.run(debug=True)

