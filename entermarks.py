#!C:/Python34/python
print('Content-Type : text/html\n\n')

import cgi,cgitb

form = cgi.FieldStorage()
candidate_name = form.getvalue('candidate_name')
roll_no = form.getvalue('roll_no')
class_name = form.getvalue('class_name')
program_mark_1 = form.getvalue('program_mark_1')
program_mark_2 = form.getvalue('program_mark_2')
program_mark_3 = form.getvalue('program_mark_3')
interview_mark_1 = form.getvalue('interview_mark_1')
interview_mark_2 = form.getvalue('interview_mark_2')
if candidate_name == None and roll_no == None:
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
conn = mysql.connector.connect(user = 'root',password = '',host = 'localhost',database = 'assesment')
cur = conn.cursor()
cur.execute('''CREATE table if not exists mark_list
	(candidate_name VARCHAR(255),
	class_name VARCHAR(20),
	roll_no VARCHAR(20),
	program_mark_1 int,
	program_mark_2 int,
	program_mark_3 int,
	interview_mark_1 int,
	interview_mark_2 int)''')
cur.execute('SELECT * from mark_list')
roll = cur.fetchall()
flag = 0
for each in roll:
	if roll_no == each[2]:
		flag = 1
if flag == 0:
	cur.execute("INSERT INTO mark_list values('"+candidate_name+"','"+class_name+"','"+roll_no+"','"+program_mark_1+"','"+program_mark_2+"','"+program_mark_3+"','"+interview_mark_1+"','"+interview_mark_2+"')")
	print('''
		<html>
		<body>
		<meta http-equiv="refresh" content="0;url =mainpage.html">
		</body>
		</html>''')
else:
	print('''
		<html>
		<body>
		<meta http-equiv="refresh" content="0;url =mainpageerror.html?error='Mark already entered'">
		</body>
		</html>''')
conn.commit()
conn.close()