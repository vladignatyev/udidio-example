# -*- coding: utf-8 -*-
import os
import flask

from flask import url_for, request

from heroku import HerokuRequest

app = flask.Flask(__name__)

# Application variables

app.secret_key = 'Your secret key.'
debug_mode = os.environ.get('DEBUG', False) == '1'
http_prefix = 'https://'
server_name = os.environ['SERVER_NAME']

app.debug = debug_mode

if app.debug:
    pass
else:
    app.config.update(SERVER_NAME=server_name)
    app.request_class = HerokuRequest

app.config.update(HTTP_PREFIX=http_prefix)


def build_api_link(service_name, callback_url):
	"""
	Utility for building UDID.io API links
	"""
	api_link = 'https://get.udid.io/thirdparty/api/?callback=%(callback)s&service=%(service)s&schemeurl=0' % {
		'callback': callback_url,
		'service': service_name
	}

	return api_link


@app.route('/')
def index():
	"""
	Homepage endpoint
	
	The homepage contains the link "Check in the device", which will pass 
	user through UDID obtaining process
	"""
	callback_url = ''.join((http_prefix, server_name, url_for('.postback')))
	api_link = build_api_link('UDID registration test app', callback_url)

	return '<a href="%s">Check in the device.</a>' % api_link


@app.route('/postback', methods=['POST'])
def postback():
	"""
	POST callback endpoint

	The UDID.io service will send a POST request to this endpoint.
	Values send with the POST request will contain UDID, IMEI, Product, Version and Serial No.
	"""
	udid = request.args.get('udid')

	# fields
	imei = request.args.get('imei')
	product = request.args.get('product')
	version = request.args.get('version')
	serial = request.args.get('serial')

	return 'Device UDID is: %s' % udid


if __name__ == "__main__":
    if app.debug:
        app.run(host='0.0.0.0', port=8000, debug=True)
    else:
        print """To run application you should use application 
server or run it with DEBUG=1 environmental variable set"""
