from django.utils import timezone
from django.shortcuts import render


tweets = [
    {'user_name': 'jorgebastida', 'message': 'Hello world!', 'timestamp': timezone.now()},
    {'user_name': 'jaimeirurzun', 'message': 'I like ponies! http://djangopony.com', 'timestamp': timezone.now()},
    {'user_name': 'jorgebastida', 'message': 'Django RULEZZZZZZ', 'timestamp': timezone.now()}
]


def timeline(request):
    return render(request, 'website/index.html', {'tweets': tweets})
