#!C:/Python34/python
print('Content-Type:text/html\n\n')

import cgi,cgitb
form = cgi.FieldStorage()
user = form.getvalue('username')
passwd =form.getvalue('password')
if user == None and passwd == None:
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

import os
import mysql.connector
conn = mysql.connector.connect(user = "root",password = "")
cur = conn.cursor()
cur.execute("create database if not exists assesment")
cur.execute("use assesment")
cur.execute("create table if not exists loginlog(username VARCHAR(255),password CHAR(16))")
cur.execute("INSERT INTO loginlog values('"+user+"','"+passwd+"')")
cur.execute("select * from adminlogin")
out = cur.fetchall()
flag = 0
for each in out:
	if user == each[0] and passwd == each[1]:
		flag = 1
		break
if flag == 1:
	print('''<html>
		<head><title>Python project</title></head>
			<script type="text/javascript">
  

function setCookie(cname,exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires=" + d.toGMTString();
    var cvalue = 'admin';
    document.cookie = cname+"="+cvalue+"; "+expires;
    window.location = "adminpage.html";
}
</script><body onload = "setCookie('currentuser',1)"></body>
			</html>''')
else:
	cur.execute("SELECT * from testlogin")
	tp = cur.fetchall()
	flaguser = 0
	for each in tp:
		if user == each[0] and passwd == each[1]:
			flaguser = 1
			break
	if flaguser == 1:
		print('''<html>
		<head><title>Python project</title></head>
		<script type="text/javascript">
 		function setCookie(cname,exdays) {
		    var d = new Date();
		    d.setTime(d.getTime() + (exdays*24*60*60*1000));
		    var expires = "expires=" + d.toGMTString();
		    var cvalue = 'tester';
		    document.cookie = cname+"="+cvalue+"; "+expires;
		    window.location = "mainpage.html"
}
</script><body onload = "setCookie('currentuser',1)">
</body>
			</html>''')
	else:
		print('''<html>
			
			<body>
			<meta http-equiv="refresh" content="0;url =index.html">
			</body>
			</html>''')

conn.commit()
conn.close()