from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('Controller','../templates'))

class Controller:
	output = ""
	def __init__(self):
		self.clearOutput()

	def getOutput(self):
		return self.output

	def addOutput(self, a):
		self.output+=a

	def clearOutput(self):
		self.output = ""

	def addView(self, view_name, var_dict):
		template = env.get_template(view_name)
		self.addOutput(template.render(var_dict))
