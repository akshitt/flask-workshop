from flask import Flask, render_template, url_for, redirect 
from forms import LoginForm 

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


@app.route("/")
def home():
	return render_template('home.html')

@app.route("/about")
def about():
	return render_template('about.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.username.data == 'akshit' and form.password.data == 'password':
			return redirect(url_for('about'))
			
	return render_template('login.html', form=form)



if __name__ == '__main__':
	app.run(debug=True)


# 127.0.0.1 is the IP address of your local machine. 5000 is the port number. 
# localhost instead of 127.0.0.1 will give the same results.
