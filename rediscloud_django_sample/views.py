from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.cache import cache
import sys

def home(request):
  return render_to_response('index.html', {})

def command(request):
  try:
    a = request.GET["a"]
    if a == 'set':
      res = cache.set('welcome_msg', 'Hello from Redis!')
    elif a =='get':
      res = cache.get('welcome_msg')
    elif a == 'info':
      res = ''.join(['%s: %s<br/>' % (k,v) for k,v in cache._client.info().iteritems()]) 
    elif a == 'flush':
      res = cache.clear()
    else:
      res = ''
  except Exception as e:
    print "Error: %s" % e 
    return HttpResponse("Error")

  return HttpResponse(res)
