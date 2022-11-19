import ibm_db

connection = ibm_db.connect("DATABASE=bludb;HOSTNAME=98538591-7217-4024-b027-8baa776ffad1.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=30875;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=lgm69103;PWD=3C3EUtNxNUE5zoCL",'','')

print(connection)
print("Connection Successfull !\n\n")

sql = "SELECT EMAIL,PASSWORD FROM logins"
stmt = ibm_db.exec_immediate(connection, sql)
dictionary = ibm_db.fetch_assoc(stmt)
while dictionary != False:
    # printing
    print("Full Row : ", dictionary)
    dictionary = ibm_db.fetch_assoc(stmt)