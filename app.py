# -*- coding: utf-8 -*-
import os
import flask

from heroku import HerokuRequest

app = flask.Flask(__name__)

app.secret_key = 'Your secret key.'

app.debug = os.environ.get('DEBUG', False) == '1'

if app.debug:
    pass
else:
    app.config.update(SERVER_NAME=os.environ['SERVER_NAME'])
    app.request_class = HerokuRequest

app.config.update(HTTP_PREFIX='http://')


@app.route('/')
def hello_world():
	callback = ''
	service = 'UDID registration test app'
	
	api_link = 'https://get.udid.io/thirdparty/api/?callback=%(callback)s&service=%(service)s' % {
		'callback': callback,
		'service': service
	}

	return '<a href="%s">Check in the device.</a>' % api_link


@app.route('/postback', methods=['POST'])
def postback():
	udid = request.args.get('udid')
	imei = request.args.get('imei')
	product = request.args.get('product')
	version = request.args.get('version')
	serial = request.args.get('serial')

	return ''


if __name__ == "__main__":
    if app.debug:
        app.run(host='0.0.0.0', port=8000, debug=True)
    else:
        print """To run application you should use application 
server or run it with DEBUG=1 environmental variable set"""
