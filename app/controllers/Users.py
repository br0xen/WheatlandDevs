from MyController import MyController as controller

class Users(controller):
	logged_in = False
	def __init__(self):
		self.checkLogin()

	def checkLogin(self):
		return self.logged_in
	
	def loginScreen(self):
		self.fullView("users/login.html")

	def doLogin(self):
		self.logged_in = True

	def profile(self):
		self.fullView("users/profile.html")
