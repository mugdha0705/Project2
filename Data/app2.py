# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#
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
cursor.execute("""SELECT * FROM aid_data""")
cursor.fetchone()

cursor=conn.cursor()
cursor.execute("""SELECT * FROM school_name""")
result = cursor.fetchone()

print(result)









@app.route("/")
def index():
    """Return the homepage."""
    return render_template("Main Page.html")


@app.route("/names")
def names():
    return "Hello World"
    
    
#Enter the values for you database connection


if __name__ == "__main__":
    app.run()

