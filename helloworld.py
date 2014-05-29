from flask import Flask
app = Flask (__name__)
@app.route('/')
def hello_world():
	return 'Hello World!'
if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')

# If you want you can make roothe server publicly available by
# changing the call of run() to have host='0.0.0.0') I dunno
# why it works, but I guess that means your computer is now
# actually hosthing the program for the world.
