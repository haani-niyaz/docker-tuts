from flask import Flask, render_template, Response, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def main_page():

	name = ''
	if request.method == 'POST':
		name = request.form['name']
	
	return render_template('index.html', name=name)

@app.route('/monster/<name>')
def get_identicon(name):
	r = requests.get('http://dnmonster:8080/monster/' + name + '?size=80')
	image = r.content
	return Response(image,mimetype='image/png')

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0')