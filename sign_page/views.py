from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.template import RequestContext, loader, Context
from django.http.cookie import SimpleCookie

def main_page(request):
    if request.method == 'POST':
        print('POOOOOSSSTTTT/n')
        print(request.COOKIES.get('arr'))
        print(gk(request.COOKIES.get('arr')))
    t = loader.get_template('sign_page/index.html')
    c = Context({'app': 'My app', 'user': request.user, 'ip_address': request.META['REMOTE_ADDR'], 'message': 'I am view 1.'})
    #cookiess = SimpleCookie()
    #cookiess['sad'] = 'asd'
    #request.cookies = cookiess
    template = loader.get_template('sign_page/index.html')
    context = {}
    response = HttpResponse(template.render(context, request))
    #response.set_cookie(key="qeqw", value="312")
    return response
    #return render(request, 'sign_page/index.html', {})

def gk(arr_str):
  return [int(i) for i in arr_str.split(',')]