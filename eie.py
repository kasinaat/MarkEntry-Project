#!C:/Python34/python
print("Content-Type: text/html\n\n")
import mysql.connector
conn = mysql.connector.connect(user = "root",password="",database = "assesment")
cur = conn.cursor()
cur.execute("SELECT * from mark_list where roll_no like '__n%' order by(roll_no)")
mark = cur.fetchall()
print('''<html>
<head>
	<title>Python project</title>
	<link rel="stylesheet" type="text/css" href="bootstrap/css/bootstrap.min.css">
	<script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
	<script src="src/jquery.table2excel.js"></script>
    <div class=" col-xs-12 text-center" style="background-color: #CB7230;padding-bottom: 10px;">
    <div class="col-xs-6" style="color: white";><h1>Karpagam College of Engineering</h1></div>
    </div>
</head>
<style>
.dropdown {
    position: relative;
    display: inline-block;
}

.dropdown-content {
    display: none;
    position: sticky;
    background-color: #CB7230;
    min-width: 150px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    padding: 12px 16px;
}

.dropdown:hover .dropdown-content {
    display: block;
}
a:link{
	text-decoration: none;
	color: white;
	font-size: 20px;
}
a:active{
	text-decoration: none;
	color:white;
}
a:hover{
	text-decoration: none;
	color: white;

}
a:visited{
	text-decoration: none;
	color: white;
}
</style>
<script>
function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length,c.length);
        }
    }
    return "";
}
function checkCookie() {
    var user = getCookie("currentuser");
    if (user != "admin") {
        window.location = "index.html";
    }
}
$("button").click(function() {
				$(".table2excel").table2excel({
					exclude: ".noExl",
					name: "Excel Document Name",
					filename: "myFileName",
					fileext: ".xls",
					exclude_img: true,
					exclude_links: true,
					exclude_inputs: true
				});
			});
		</script>

<body onload = "checkCookie()" style="background-color: #e0e0e0">
<div class="row" >
	<div class="col-xs-12" style="background-color: #E0E0E0">
		<div class="col-xs-2 col-xs-offset-1">
				<span class="col-xs-offset-4"><button class="btn">Home</button></span>
			</div>
		<div class="col-xs-2">
			<div class="dropdown">
				<span ><button class="btn " >Mark list</button></span>
					<div class="dropdown-content" style=" background-color: #CB7230;">
						<li><a href="auto.py">Auto</a></li>
						<li><a href="cse.py">CSE</a></li>
						<li><a href="eee.py">EEE</a></li>
						<li><a href="ece.py">ECE</a></li>
						<li><a href="ete.py">ETE</a></li>
						<li><a href="eie.py">EIE</a></li>
						<li><a href="it.py">IT</a></li>
						<li><a href="mech.py">Mech</a></li>
					</div>
			</div>
		</div>
		<div class="col-xs-2">
			<div class="dropdown">
				<span ><button class="btn " s>Users</button></span>
					<div class="dropdown-content" style="background-color: #CB7230;">
						<li><a href="adduserhtml.py">Add</a></li>
						<li><a href="cse.py">Remove</a></li>
					</div>
			</div>
		</div>
		<div class="col-xs-2">
			<div class="dropdown ">
				<span><button class="btn">Student log</button></span>
					<div class="dropdown-content" style=" background-color: #CB7230;">
						<li><a href="auto.py">Auto</a></li>
						<li><a href="cse.py">CSE</a></li>
						<li><a href="eee.py">EEE</a></li>
						<li><a href="ece.py">ECE</a></li>
						<li><a href="ete.py">ETE</a></li>
						<li><a href="eie.py">EIE</a></li>
						<li><a href="it.py">IT</a></li>
						<li><a href="mech.py">Mech</a></li>
					</div>
			</div>
		</div>
		<div class="col-xs-2">
				<div class="dropdown ">
				<span ><button class="btn" >more</button></span>
				<div class="dropdown-content" style=" background-color: #CB7230;">
						<li><a href="logout.py">logout</a></li>
				</div>
			</div>
		</div>
	</div>
	<div class = "col-xs-12">
	<button class = "btb btn-success">Export as Sheet</button>
	</div>
	<div class = "col-xs-12">
<table class="table table-bordered table2excel table-responsive" style="border-color: black">
	<thead style="border-color: black">
		<tr style="border-color: black">
			<th>S.no</th>
			<th>Rollno.</th>
			<th>Name</th>
			<th>Dept/Class</th>
			<th>mark1</th>
			<th>mark2</th>
			<th>mark3</th>
			<th>mark4</th>
			<th>mark5</th>
			<th>total</th>
		</tr>
	</thead>''')
print("<tbody>")
itr = 0
for each in mark:
	itr += 1
	total = each[3] + each[4] + each[5] + each[6] + each[7]
	print('<tr>')
	print('<td>%d</td>'%itr)
	print('<td>%s</td>'%each[2])
	print('<td>%s</td>'%each[0])
	print('<td>%s</td>'%each[1])
	print('<td>%d</td>'%each[3])
	print('<td>%d</td>'%each[4])
	print('<td>%d</td>'%each[5])
	print('<td>%d</td>'%each[6])
	print('<td>%d</td>'%each[7])
	print('<td>%d</td>'%total)
	print('</tr>')
print('</div> </body>')
print('</html>')
conn.commit()
conn.close()