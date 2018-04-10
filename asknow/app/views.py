from django.shortcuts import render, render_to_response

from asknow import settings


def index(request):
    return render_to_response('app/index.html', {
        'app_name': settings.APP_NAME,
        'title': 'Hello, World!',
        'questions': build_questions(),
        'blocks': build_blocks()
    })


def build_questions():
    titles, bodies, votes = [], [], []
    authors = []
    for x in range(25):
        titles.append('Test title ' + str(x + 1))
        bodies.append('This is a some random text: abort, butter, cancel, duck, echo, fog, glass')
        votes.append('90K')
        authors.append({'name': 'Denis Sologub'})
    return [{'title': t, 'body': b, 'votes': v, 'author': a}
            for t, b, v, a in zip(titles, bodies, votes, authors)]


def build_blocks():
    titles, bodies = [], []
    for i in range(3):
        titles.append('Block ' + str(i + 1))
        bodies.append('Some block content')
    return [{'title': t, 'body': b} for t, b in zip(titles, bodies)]
