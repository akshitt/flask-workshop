from flask import Flask, render_template, url_for, redirect 

app = Flask(__name__)

@app.route("/")
def home():
	return render_template('home.html')

@app.route("/about")
def about():
	return render_template('about.html')

if __name__ == '__main__':
	app.run(debug=True)


# 127.0.0.1 is the IP address of your local machine. 5000 is the port number. 
# localhost instead of 127.0.0.1 will give the same results.
