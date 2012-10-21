from Controller import Controller as controller

# My Controller is a custom controller for this app
#	It adds a 'addHeader' function which loads the default css
#	An 'addFooter' function which loads the default js
#	And a 'fullView' function which takes a view name and it's variables
#		and it loads up the head, that view, then the footer
class MyController(controller):
	def addHeader(self):
		self.addView("_header.html",
			{	"css":["/assets/css/bootstrap.css","/assets/css/bootstrap-responsive.min.css","/assets/css/wheatland.css"],
				"page_title":"Wheatland Developers"
			})

	def addFooter(self):
		self.addView("_footer.html",{"scripts":["/assets/js/jquery-1.8.2.min.js","/assets/js/bootstrap.min.js"]})

	def fullView(self, page_name, var_dict={}):
		self.addHeader()
		self.addView(page_name, var_dict)
		self.addFooter()
