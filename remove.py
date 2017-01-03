#!C:/Python34/python
print("Content-Type: text/html\n\n")
import cgi,cgitb
form  = cgi.FieldStorage()
value = form.getvalue('value')

import mysql.connector
conn = mysql.connector.connect(user = "root",password="",database = "assesment")
cur = conn.cursor()
cur.execute('DELETE from testlogin where username = "'+value+'"')
conn.commit()
conn.close()
print('''<html>
	<head>
	<meta http-equiv = "refresh" content="0; removeuser.py">
	</head>
	</html>''')