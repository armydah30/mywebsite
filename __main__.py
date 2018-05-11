import os
from mysite.app import app

if __name__ == '__main__': #The port to be listening to — hence, the URL must be <hostname>:<port>/ inorder to send the request to this program
	app.run(debug=True)  #Start listening
