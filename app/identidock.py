from flask import Flask, render_template, Response
import requests
app = Flask(__name__)

@app.route('/')
def main_page():
	# return 'Hello Docker!\n'
	name = "Billy"
	return render_template('index.html', name=name)

@app.route('/monster/<name>')
def get_identicon(name):
	r = requests.get('http://dnmonster:8080/monster/' + name + '?size=80')
	image = r.content
	return Response(image,mimetype='image/png')

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0')