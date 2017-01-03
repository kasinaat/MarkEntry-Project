#!C:/Python34/python
print("Content -Type:test/html\n\n")

print('''<html>
		<head><title>Python project</title></head>
			<script type="text/javascript">
			function deleteCookie() {
				document.cookie = "currentuser=; expires=Thu, 01 Jan 1970 00:00:00 UTC";
  				window.location = "index.html";
			}
			</script>
			<body onload = "deleteCookie()"></body>
			</html>''')