from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
	return "Kudos! You are done for now."


if __name__ == '__main__':
	app.run(debug=True)
