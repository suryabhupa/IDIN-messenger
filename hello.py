from flask import Flask
app = Flask (__name__)
@app.route('/')
def hello_world():
	return 'Hello World!'
if __name__ == '__main__':
	app.run()

# A class is like a spec sheet. It explains how something
# will be designed. A class might be people, and an object
# might be person. Amber and Al are of class person. I have
# class cat and class dog, and my family's cat is something
# of that class. The instance would be 'Amber' or 'Al' or
# 'Atlanta'. An argument is the input of a function, just 
# like in algebra. Some people refer to it as a thing that 
# a function passes. Here, we created a module (a small
	# program) and called it __name__, which was the argument
	# of a function. That function was our module itself, which
	# is also an instance, a specific member of the Flask class
	# of programs. Because we are writing in Python, we actually
	# had to import the Flask class, which is what we started
	# with.

	# A decorator is that they just used a matching pattern, where
	# any URL that matches the pattern should go to Hello World.
	# The matching thing they most likely used is called regex,
	# which is a compressed matching syntax. We put the URL as /
	# which means the root level. Anything that matches the
	# pattern will run. The URL / should trigger the fucntion
	# underneath it. When you go to google.com, you are going to
	# google.com/. I can define my domain name later on, and my
	# program will only care about the / and what comes after it.
	# Putting / means that my app will run on any domain, like
	# my computer or any domain I buy.

	# Also, 127.0.0.1 is the same thing as localhost. This will
	# be important later. Sometimes things are supposed to run 
	# on localhost but they want you to enter in the numbers in
	# the program instead.

	# Run() runs the local server with our application. That
	# Run is a function that Flask already defined. And () 
	# are allowed to be empty because they can pull in random
	# variables from all over the place. So Flask already 
	# defined Run to run things on localhost. It will always
	# run things on whatever domain I'm on. So if I'm running
	# it from my computer, it runs from localhost, and if I 
	 # upload my program to a server it will run on the server's
	 # domain.
	 
