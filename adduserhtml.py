#!C:/Python34/python
print('Content-Type:text/html\n\n')
import cgi,cgitb
form = cgi.FieldStorage()
val = form.getvalue('val')
print('''<html>
<head>
	<title>Python Project</title>
	<link rel="stylesheet" type="text/css" href="bootstrap/css/bootstrap.min.css">
    <div class=" col-xs-12 text-center" style="background-color:#CB7230;padding-bottom: 10px;">
    	<div class="col-xs-6" style="color: white";><h1>Karpagam College of Engineering</h1>
    </div>
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
<script type="text/javascript">
  
function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i=0; i<ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

function checkCookie() {
    var user = getCookie("currentuser");
    if (user == "admin") {
    } else {
      if(user == "tester"){
          window.location = "mainpage.html";
      }
    }
}
</script>
<body onload = "checkCookie()" style="background-color: #E0E0E0">

<div class="row" >
	<div class="col-xs-12" style="background-color: #E0E0E0">
		<div class="col-xs-2 col-xs-offset-1">
				<span class="col-xs-offset-4"><button class="btn">home</button></span>
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
						<li><a href="adduser.html">Add</a></li>
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
				<span ><button class="btn" >logout</button></span>
			</div>
		</div>
	</div>
<form name = "myform" class="form-horizontal col-xs-6 login-form col-xs-offset-3" method="POST" action="adduser.py" style="padding-top: 200px">
<fieldset class="col-xs-8 col-xs-offset-2 me"><legend>Add User</legend>
  <div class="form-group">  
    <label for="inputEmail3" class="col-sm-2 control-label">UserID</label>
    <div class="col-sm-10">
      <input type="text" class="form-control" id="inputEmail3" placeholder="UserID" name="username">
    </div>
  </div>
  <div class="form-group">
    <label for="inputPassword3" class="col-sm-2 control-label">Password</label>
    <div class="col-sm-10">
      <input type="text" class="form-control" id="inputPassword3" placeholder="Password" name="password">
    </div>
  </div>
  
  <div class="form-group">
    <div class="col-sm-offset-2 col-sm-10" style="padding-bottom: 35px"  >
      <input type="submit" class="btn" style="background-color: #CB7230;color: white" value="Add User">
    </div>
  </div>
</form>
<div>''')
if val:
	print("%s"%val)
	print('''
	</div>
	</body>
	</html>''')
else:
	print('''
	</div>
	</body>
	</html>''')