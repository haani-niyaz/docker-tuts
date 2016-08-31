from flask import Flask, render_template, Response, request
import requests
import redis

cache = redis.StrictRedis(host='redis',port=6379,db=0)

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def main_page():

	name = ''
	if request.method == 'POST':
		name = request.form['name']
	
	return render_template('index.html', name=name)

@app.route('/monster/<name>')
def get_identicon(name):


	# Lookup on name
	image = cache.get(name)

	# Check if name is already in the cache
	# Redis will return 'None' if we have a Cache miss. Resort to falllback..
	if image is None:
		# Output debug info
		print("Cache miss", flush=True)
		r = requests.get('http://dnmonster:8080/monster/' + name + '?size=80')
		image = r.content
		# Add image to cache
		cache.set(name,image)
	
	return Response(image,mimetype='image/png')

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0')