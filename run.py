from web import app

if __name__ == "__main__":
    app.run(debug=True)


# mysql database configuration

# from distutils.log import debug

# import mysql.connector
# from mysql.connector import Error

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd = "1234",
#   database="Buy_Sell_books",
#   auth_plugin='mysql_native_password'
# )

# db = mydb.cursor()

# db.execute('insert into school_books values (2, "Chemistry-Ncert", 12,"","NCERT","Mohammed Huzefa", 2020, "English");')

# mydb.commit()