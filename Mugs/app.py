import MySQLdb
from flask import Flask, jsonify, render_template
import os
import pandas as pd
import numpy as np

app = Flask(__name__)

dsn_database = "school_uni_db"   
dsn_hostname = "localhost"      
dsn_port = 3306                       
dsn_uid = "root"            
dsn_pwd = "Pimn@2001" 

conn = MySQLdb.connect(host=dsn_hostname, port=dsn_port, user=dsn_uid, passwd=dsn_pwd, db=dsn_database)
cursor=conn.cursor()
cursor.execute("""SELECT * FROM dl_school_rename""")
result = cursor.fetchall()
# getting entire table
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
# getting column names
num_fields = len(cursor.description)
col_names = [i[0] for i in cursor.description]

csv = pd.read_csv("DefaultRate.csv")

df = pd.DataFrame(csv)


@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index2.html")
    # return jsonify(col_names)


@app.route("/region")
def region():
    """Return a list of regions."""
    return jsonify(col_names[0])

@app.route("/loans/<region>")
def loans(region):
        df = pd.DataFrame(csv)
        clean_data = df.dropna(how='any')

        data={
                "States": clean_data.States.tolist(),
                "Defaults": clean_data.Defaults.tolist(),
                "Loans": clean_data.Loans.tolist(),
                "DefRate": clean_data.DefRate.tolist()
        }
        return jsonify(data)  


if __name__ == "__main__":
    app.debug= True
    app.run()
