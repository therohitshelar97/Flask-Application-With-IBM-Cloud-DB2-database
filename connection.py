import os

os.add_dll_directory('C:\\Personal\\IBM-Cloud-Database-Connections\\myenv\Lib\\site-packages\\clidriver\\bin') 

import ibm_db

print(ibm_db.__version__)

# Connection parameters
# dsn = (
#     "DATABASE=bludb;"
#     "HOSTNAME=0c77d6f2-5da9-48a9-81f8-86b520b87518.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;"
#     "PORT=31198;"
#     "PROTOCOL=TCPIP;"
#     "UID=mkh19143;"
#     "PWD=gN58GN1tK31PO1OT;"
# )

# try:
#     # Connect to the database
#     conn = ibm_db.connect(dsn, "", "")
#     print("Connected to Db2!")
# except:
#     print("Unable to connect to the database.")