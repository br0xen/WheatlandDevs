from mod_python import apache
import sys
root_dir = "/var/www/wheatlanddevs.com/app/"
sys.path.append(root_dir)
sys.path.append(root_dir+"core/")
sys.path.append(root_dir+"controllers/")
sys.path.append(root_dir+"models/")

from cgi import parse_qs, escape
from Controller import Controller

params = {}

def index(req):
	parseQS(req)
	users(req)
	return

def users(req):
	parseQS(req)
	from Users import *
	users = Users()
	req.content_type = "text/html"
	if(params["func"] == "doLogin"):
		users.doLogin()

	if users.logged_in:
		users.profile()
	else:
		users.loginScreen()

	req.write(users.getOutput())

def parseQS(req):
	d = parse_qs(req.subprocess_env['QUERY_STRING'])
	for k, v in d.iteritems():
		if k == "f":
			params['func'] = v[0]

