import os

import pandas as pd
import numpy as np
import MySQLdb

# import pymysql
# pymysql.install_as_MySQLdb()

import sqlalchemy as db
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

rds_connection_string = "root:Pimn@2001@127.0.0.1:3306"
engine = db.create_engine(f'mysql://{rds_connection_string}')

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Pimn@2001@127.0.0.1:3306/school_uni_db"
db = SQLAlchemy(app)



connection = engine.connect()
metadata = db.MetaData()

# # reflect an existing database into a new model
Base = automap_base()
# # reflect the tables
Base.prepare(db.engine, reflect=True)

AID = db.Table('aid_data', metadata, autoload=True, autoload_with=engine)

print("Show Keys")
print(AID.columns.keys())
print(repr(metadata.tables['aid_data']))
print("End Keys")
# print(db.engine.table[0])
# print(Base.classes.keys())

# session = Session(db.engine)
# print("Session Query.........")
# SN = db.engine.table_names()[0]
# print(session.query(SN.school_name).all())
# print("End Session Query.....")
# # Save references to each table
# debt_Metadata = Base.classes.debt_data
# aid_Metadata = Base.classes.aid_data
# print(debt_Metadata)
# print(aid_Metadata)

# PVT = Base.classes.static_pvt_pub
# print(session.query(PVT.Description).all())

# SN = Base.classes.school_name
# print(session.query(SN.school_name).all())


@app.route("/")
def index():
    """Return the homepage."""
    return render_template("Main Page.html")


@app.route("/names")
def names():
    """Return a list of sample names."""

    # Use Pandas to perform the sql query
    stmt = db.session.query(aid_Metadata).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    # Return a list of the column names (sample names)
    # return jsonify(list(df.columns)[2:])


# @app.route("/metadata/<sample>")
# def sample_metadata(sample):
#     """Return the MetaData for a given sample."""
#     sel = [
#         Samples_Metadata.sample,
#         Samples_Metadata.ETHNICITY,
#         Samples_Metadata.GENDER,
#         Samples_Metadata.AGE,
#         Samples_Metadata.LOCATION,
#         Samples_Metadata.BBTYPE,
#         Samples_Metadata.WFREQ,
#     ]

    # results = db.session.query(*).all()

#     # Create a dictionary entry for each row of metadata information
#     sample_metadata = {}
#     for result in results:
#         sample_metadata["sample"] = result[0]
#         sample_metadata["ETHNICITY"] = result[1]
#         sample_metadata["GENDER"] = result[2]
#         sample_metadata["AGE"] = result[3]
#         sample_metadata["LOCATION"] = result[4]
#         sample_metadata["BBTYPE"] = result[5]
#         sample_metadata["WFREQ"] = result[6]

#     print(sample_metadata)
#     return jsonify(sample_metadata)


# @app.route("/samples/<sample>")
# def samples(sample):
#     """Return `otu_ids`, `otu_labels`,and `sample_values`."""
#     stmt = db.session.query(Samples).statement
#     df = pd.read_sql_query(stmt, db.session.bind)

#     # Filter the data based on the sample number and
#     # only keep rows with values above 1
#     sample_data = df.loc[df[sample] > 1, ["otu_id", "otu_label", sample]]
#     # Format the data to send as json
#     data = {
#         "otu_ids": sample_data.otu_id.values.tolist(),
#         "sample_values": sample_data[sample].values.tolist(),
#         "otu_labels": sample_data.otu_label.tolist(),
#     }
#     return jsonify(data)


if __name__ == "__main__":
    app.run()


