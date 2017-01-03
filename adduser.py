#!C:/Python34/python
print("Content-Type :text/html\n\n")

import cgi,cgitb
form  = cgi.FieldStorage()
newuser = form.getvalue('username')
passcode = form.getvalue('password')
if newuser == None and passcode == None:
	print('''<html>
		<head><title>Python project</title></head>
			<script type="text/javascript">
			function reload() {
  				window.location = "index.html";
			}
			</script>
			<body onload = "reload()"></body>
			</html>''')
	exit()

import mysql.connector
conn = mysql.connector.connect(user = "root",password="",database="assesment")
cur = conn.cursor()
cur.execute('CREATE table if not exists testlogin(username VARCHAR(255),password CHAR(16))')
cur.execute('SELECT * from testlogin')
out = cur.fetchall()
flag = 0
for each in out:
	if each[0] == newuser:
		flag = 1
if flag == 1:
	error = "Username already exists"
	print('''<html>
		<body>
		<meta http-equiv="refresh" content="0;url =adduserhtml.py?val=%s">
		</body>
		</html>'''%error)
else:
	cur.execute("INSERT into testlogin values('"+newuser+"','"+passcode+"')")
	error = "User successfully added"
	print('''<html>
		<body>
		<meta http-equiv="refresh" content="0;url =adduserhtml.py?val=%s">
		</body>
		</html>'''%error)
conn.commit()
conn.close()