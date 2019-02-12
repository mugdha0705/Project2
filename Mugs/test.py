
#import pymysql
# pymysql.install_as_MySQLdb()
import MySQLdb
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

dsn_database = "school_uni_db"   # e.g. "MySQLdbtest"
dsn_hostname = "localhost"      # e.g.: "mydbinstance.xyz.us-east-1.rds.amazonaws.com"
dsn_port = 3306                        # e.g. 3306 
dsn_uid = "root"             # e.g. "user1"
dsn_pwd = "Pimn@2001"            # e.g. "Password123"



conn = MySQLdb.connect(host=dsn_hostname, port=dsn_port, user=dsn_uid, passwd=dsn_pwd, db=dsn_database)
 

cursor=conn.cursor()
cursor.execute("""SELECT * FROM dl_school_rename""")
result = cursor.fetchall()

# cursor=conn.cursor()
# cursor.execute("""SELECT * FROM default_data_final""")
# result = cursor.fetchall()

print(result)

Itype = []
date=[]
qtr=[]
dollaramt=[]
receipient=[]

for item in result: 
        Itype.append(item[0]),
        date.append(item[1])
        qtr.append(item[2])
        dollaramt.append(item[3])
        receipient.append(item[4])

listOfLists = [Itype, date, qtr, dollaramt, receipient]

print(dollaramt)

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index2.html")
    
    # return jsonify(listOfLists)


# @app.route("/names")
# def names():
#     return "Hello World"

# @app.route("/")
# def index():
#     """Return the homepage."""
#     return render_template("index.html")


@app.route("/QTR")
def QTR():
    """Return a list of sample names."""
    return jsonify(listOfLists)
#     # Use Pandas to perform the sql query
#     return jsonify(list(listOfLists))  


# @app.route("/metadata/<sample>")
# def result(loan):
#     """Return the MetaData for a given sample."""
#      cursor=conn.cursor()
#     cursor.execute("""SELECT * FROM dl_school_rename""")
#     result = cursor.fetchall()
#     return jsonify(list(result)

    # Create a dictionary entry for each row of metadata information
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


# # @app.route("/samples/<sample>")
# # def samples(sample):
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


# if __name__ == "__main__":
#     app.run()

    
    
# #Enter the values for you database connection


if __name__ == "__main__":
    app.run()
