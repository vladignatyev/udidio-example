# How to obtain device information without TestFlight App
## UDID.io Usage Example

The famous [UDID.io allows any user to get the device information](http://get.udid.io/) like UDID, IMEI, Serial No. of the iPhone and iPad using mobile provisioning.

This repo contains example application which uses the "third-parties API" to use UDID.io as the part of your website or mobile application.

## API description and spec
The API uses POST callback mechanism to send data back to your web application.
You are required to build URL and pass user through the composed URL. You also required to make user understand that he should use Mobile Safari browser in order to make UDID registration work. 
The URL contains a service name, POST callback URL and parameter called 'schemeurl', which should be always equal to '0' for the current version of API.

An example of such URL is as follows:
```http://get.udid.io/thirdparty/api/?callback=<your_post_callback_url>&service=My Test App&schemeurl=0```

Your POST endpoint should accept following fields:
* ```imei``` - the IMEI identifier of iPhone, iPad or iPod
* ```udid``` - the UDID identifier
* ```product``` - the product name, for example 'iPhone7,1' for iPhone 6+
* ```version``` - the device version
* ```serial``` - the serial number of the device.

## Example application

This example application is written using Flask web application framework and Python programming language. But if you're unfamiliar with those technologies, you could easily create your own.

The example application is very simple. It shows the "Check in" link. When user taps that link on iPhone, Provisioning Profile installation dialog appears, then user is being redirected to UDID.io and then back to web application, which now shows UDID of user's iPhone.

To try the example app open this link: https://rocky-eyrie-4945.herokuapp.com/

To run your own copy of the app you may use Heroku or run locally for development.

## Heroku deployment
Check that ```Heroku Toolbelt``` is installed properly, else install it from official Heroku Toolbelt website https://toolbelt.heroku.com/

1. Clone this repo
2. ```cd``` into cloned repo directory.
3. ```heroku apps:create```
4. ```heroku config:add SERVER_NAME=appname.herokuapp.com``` where ```appname.herokuapp.com``` is a server name obtained on previous step
5. ```git push heroku master```
6. ```heroku open```

## Local development
1. Clone this repo
2. Create ```virtualenv```
3. Install requirements into newly created virtual env.
4. Run ```DEBUG=1 python app.py``` - it will run the app in debug mode, and will use auto-reload mechanism on code changes.

For further development of this app refer to the official [Flask documentation](http://flask.pocoo.org).
