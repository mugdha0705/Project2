import pymysql
# pymysql.install_as_MySQLdb()
import MySQLdb


#Enter the values for you database connection
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
cursor.fetchone()