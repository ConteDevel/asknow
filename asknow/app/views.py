from django.shortcuts import render, render_to_response

from asknow import settings

def index(request):
	return render_to_response('app/index.html', {
		'app_name': settings.APP_NAME,
		'title': 'Hello, World!',
	})

