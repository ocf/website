#!/bin/sh
 
cat <<EOF
Status: 503
Content-Type: text/html; charset=iso-8859-1
 
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2//EN">
<html>
<head>
<title>503 - Service temporary unavailable</title>
</head>
<body>
<h1>503 - Service temporary unavailable</h1>
<p>Sorry, this website is currently down for maintainance please
retry in a few minutes</p>
</body>
</html>
EOF
