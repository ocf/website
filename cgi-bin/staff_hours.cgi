#!/usr/bin/env python3
# dear god this is a terrible script please don't scroll down
import ldap3, yaml, cgi, random
from hashlib import md5
from urllib.parse import urlencode
from collections import defaultdict

GRAVATAR_SIZE = 100

print("Content-type: text/html\n\n")
print("""<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
<head>
  <title>Open Computing Facility - Staff Hours</title>
	<meta http-equiv="content-type" content="text/html; charset=utf-8" />
	<!--style type="text/css">
	@import url("/bleuarctic.css")
	</style>-->
	<link rel="alternate stylesheet" type="text/css" href="/bleuice.css" title="bleuice" />
	<link rel="stylesheet" type="text/css" href="/bleuarctic.css" title="bleuarctic" />
	<link rel="shortcut icon" href="/favicon.png" type="image/png" />""")


print("""
<style>
#summerBanner {
	background-image: url("/logos/yolo.png");
	background-position: 100% 0%;
	background-repeat: no-repeat;
	background-color: #ddee99;

	padding-top: 20px;
	padding-bottom: 10px;
	padding-left: 20px;
	padding-right: 193px;

	margin: 15px -15px;
	margin-top: -20px;
}

#summerBanner #sorry, #summerBanner #happy {
	font-weight: bold;
	font-family: Helvetica, Arial, sans-serif;
	color: #222;
	line-height: 1.2em;
}

#summerBanner #sorry {
	font-size: 28px;
}

#summerBanner #happy {
	font-size: 16px;
}

#summerBanner > p {
	margin-top: 0px;
	margin-bottom: 10px;
}
</style>
""")
print("""	</head>
	<body>""")
print(open('/services/http/ocf/www/header.html').read())

# print("""<div id="mothercontainer">
# <div id="container">
# <div id="summerBanner">
# <p id="sorry">Have questions? Drop by for help from a friendly volunteer staffer!</p>
# <p>OCF staff members hold regular drop-in staff hours to provide assistance with account issues or with OCF services. We're always happen to help troubleshoot account or service issues!</p>
# <!-- <p>In exceptional circumstances, we can usually arrange a meeting with an OCF staff member, although we will try to schedule multiple appointments simultaneously to preserve staff member time.</p> -->
# <p>Keep in mind the OCF volunteers sometimes have last-minute conflicts, so it's a good idea to check this page before coming in for cancellations.</p>
#  <p id="happy">Welcome back from the OCF!</p>
#  </div>
# """)

print("""<div id="mothercontainer">
<div id="container">
<div id="summerBanner">
<p id="sorry">Staff hours have concluded for the Fall semester.</p>
<p>OCF staff members hold regular drop-in staff hours to provide assistance with account issues or with OCF services. We're always happen to help troubleshoot account or service issues!</p>
<!-- <p>In exceptional circumstances, we can usually arrange a meeting with an OCF staff member, although we will try to schedule multiple appointments simultaneously to preserve staff member time.</p> -->
<p>Since we're all students, we don't hold staff hours during R.R.R. week, finals week, or during breaks. If you have urgent questions, feel free to <a href="https://ocf.io/contact">send us an email</a>. Otherwise, we look forward to seeing you in the Spring!</p>
 <p id="happy">Happy Holidays from the OCF!</p>
 </div>
""")

# <p>OCF staff are student volunteers dedicated to providing free computing for members of the UC Berkeley community. Each week, friendly staffers hold staff hours in <a href="http://wiki.ocf.berkeley.edu/services/lab/">the lab</a> to assist OCF members.</p>
# <p>Because our volunteer staff have limited time, we <em>strongly</em> prefer that users requesting support attempt to attend regular staff hours instead of <a href="http://wiki.ocf.berkeley.edu/contact/">emailing us</a> or asking for a special appointment.</p>

print("<div id=\"staff-hours\">")

ldap_server = ldap3.Server("ldap.ocf.berkeley.edu", port=636, use_ssl=True)
ldap_conn = ldap3.Connection(ldap_server, user="", password="", auto_bind=True)
ldap_base = "ou=People,dc=OCF,dc=Berkeley,dc=EDU"


with open("/home/s/st/staff/staff_hours.yaml") as f:
	data = yaml.safe_load(f)
	positions = defaultdict(lambda: "Staff Member")

	for user, position in data["staff-positions"].items():
		positions[user] = position

	def get_staff(staff):
		"""Returns an iterable of dictionaries, one per staff member, with keys
		user, name, position, and gravatar."""

		def get_staff_info(user):
			"""Returns a dictionary of info on a single staff member."""

			search_filter = "(uid={})".format(user)
			response = ldap_conn.search(ldap_base, search_filter, ldap3.SEARCH_SCOPE_WHOLE_SUBTREE, attributes=["cn"])

			name = ldap_conn.response[0]["attributes"]["cn"][0] if response else user

			# only display first and last name
			name_parts = name.split(" ")
			print_name = "{} {}".format(name_parts[0], name_parts[len(name_parts) - 1])

			def gravatar(size):
				"""Returns a gravatar URL for the given user and image size."""
				email = user + "@ocf.berkeley.edu"
				hash = md5(email.lower().encode("utf-8")).hexdigest()

				url = "https://www.gravatar.com/avatar/{}?{}"
				params = urlencode({"d": "mm", "s": size})

				return url.format(hash, params)

			return {
				"user": user,
				"name": print_name,
				"position": positions[user],
				"gravatar": gravatar
			}

		return map(get_staff_info, staff)

	# print info on each set of staff hours
	for hour in data["staff-hours"]:
		print("<div class=\"day {}\">".format("cancelled" if hour["cancelled"] else ""))

		day, time = map(cgi.escape, (hour["day"], hour["time"]))
		time = time.replace("-", "&ndash;")

		header = "<div class=\"title\"><strong>{}</strong> {} {}</div>"
		status = "<span class=\"cancelled\">cancelled this week</span>" if hour["cancelled"] else ""
		header = header.format(day, time, status)
		print(header)

		# print staff faces
		print("	<ul class=\"faces\">")
		staff = list(get_staff(hour["staff"]))
		random.shuffle(staff)
#		staff = random.shuffle(get_staff(hour["staff"]))
#		staff = sorted(get_staff(hour["staff"]), key=lambda s: s["name"].split(" ")[1])

		for staffm in staff:
			info = (staffm["name"], staffm["position"], staffm["gravatar"](GRAVATAR_SIZE))
			name, position, gravatar = map(cgi.escape, info)
			print("<li>")
			print("	<p class=\"image\"><img alt=\"gravatar\" src=\"{}\" /></p>".format(gravatar))
			print("	<p class=\"name\">{}</p>".format(name))
			print("	<p class=\"position\">{}</p>".format(position))
			print("</li>")

		print("	</ul>")
		print("</div>")


print("</div></div></div> <!-- end div container and mothercontainer -->")
print(open('/services/http/ocf/www/footer.html').read())
print(open('/services/http/ocf/www/tracker.html').read())
print("""
	</body>
	</html>""")
