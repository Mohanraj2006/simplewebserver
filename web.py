from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<head>
<title align="centre">TOP SOFTWARE COMPANIES WITH REVENUE TABLE </title>
</head>
<body bgcolor="white" align="centre" textcolor="black" >
  

TOP SOFTWARE COMPANIES WITH REVENUE TABLE 
<table border="3" cellspacing="4" cellpadding="6" height="500" width="1000">
<caption >TOP FIVE REVENUE GENERATING SOFTWARE COMPANY</caption>
<tr>
			<th>COMPANY NAME</th>
			<th>POSITION</th>
			<th>GOOD RATING</th>
		</tr>
		<tr>
			<td>TATA</td>
			<td>11THS</td>
			<td>9.0</td>



		</tr>

		<tr>
			<td>JIO</td>
			<td>3RD</td>
			<td>9</td>

		</tr>

		<tr>
			<td>VI</td>
			<td>1ST</td>
			<td>5</td>
		</tr>
<tr>
			<td>BSNL</td>
			<td>50TH</td>
			<td>7</td>

		</tr>

		<tr>
			<td>VIBRO</td>
			<td>2ND</td>
			<td>1</td>
		</tr>
	</table>
	</body>
</html>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()