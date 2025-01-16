import os

os.add_dll_directory('C:\\Personal\\IBM-Cloud-Database-Connections\\myenv\\Lib\\site-packages\\clidriver\\bin') 

import ibm_db
import ibm_db_dbi

from flask import *

app = Flask(__name__)


# Connection parameters
dsn_hostname = "815fa4db-dc03-4c70-869a-a9cc13f33084.bs2io90l08kqb1od8lcg.databases.appdomain.cloud"
dsn_uid = "ywc60234"
dsn_pwd = "WWAij8PA9hBNQrj7"
dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = "bludb"
dsn_port = "30367"
dsn_protocol = "TCPIP"
dsn_security = "SSL"

#Create database connection
#DO NOT MODIFY THIS CELL. Just RUN it with Shift + Enter
dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};"
    "SECURITY={7};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd,dsn_security)

try:
    conn = ibm_db.connect(dsn, "", "")
    print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)

except:
    print ("Unable to connect: ", ibm_db.conn_errormsg() )


@app.route("/")
def Index():
    #Construct the query that retrieves all rows from the INSTRUCTOR table
    selectQuery = "select * from SB4C"
   
    #Execute the statement
    selectStmt = ibm_db.exec_immediate(conn, selectQuery)
  
    #Fetch the Dictionary (for the first row only) - replace ... with your code
    # data = ibm_db.fetch_assoc(selectStmt)
    rows = []  # List to store all rows
    row = ibm_db.fetch_assoc(selectStmt)
    while row:  # Loop until no more rows are returned
        rows.append(row)  # Append the current row (as a dictionary)
        row = ibm_db.fetch_assoc(selectStmt)  # Fetch the next row

    data = rows
    return render_template("index.html",data=data)

@app.route('/',methods=['POST'])
def Enter():
    id = request.form.get("id")
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    city = request.form.get("city")
    ccode = request.form.get("ccode")
    print(id,fname,lname,city,ccode)
    insert = "insert into SB4C(id, fname, lname, city, ccode) values ('{}','{}','{}','{}','{}') ".format(id,fname,lname,city,ccode)
    ibm_db.exec_immediate(conn, insert)
    return redirect(url_for('Index'))

@app.route('/delete')
def Delete():
    id = request.args.get('id')
    DelQuery = "delete from SB4C where id = {}".format(id)
    ibm_db.exec_immediate(conn, DelQuery)
    return redirect(url_for('Index'))

@app.route('/update')
def Update():
    id = request.args.get('id')
    SelectOne = "Select * from SB4C where id = {}".format(id) 
    selectStmt = ibm_db.exec_immediate(conn, SelectOne)
    data = ibm_db.fetch_assoc(selectStmt)
    print(data)
    return render_template('Update.html',data=data) 

@app.route('/update1',methods=['POST'])
def Update1():
    id = request.form.get("id")
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    city = request.form.get("city")
    ccode = request.form.get("ccode")
    print(id,fname,lname,city,ccode)
    insert = "update SB4C set fname='{}', lname='{}', city='{}', ccode='{}' where id = '{}'".format(fname,lname,city,ccode,id)
    ibm_db.exec_immediate(conn, insert)
    return redirect(url_for('Index'))



if __name__=='__main__':
    app.run(debug=True)