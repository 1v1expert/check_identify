from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.template import RequestContext, loader, Context
from django.http.cookie import SimpleCookie
import csv
import numpy as np
import matplotlib.pyplot as pl

def main_page(request):
    if request.method == 'POST':
        print('POOOOOSSSTTTT/n')
        print(request.COOKIES.get('arr'))
        data = gk(request.COOKIES.get('arr'))
        #print(data, 'dasdsad!!!!!!!----')
        #print()
        path = "output.csv"
        data.append(request.COOKIES.get('name'))
        csv_writer(data, path)
        plotting()
    #t = loader.get_template('sign_page/index.html')
    #c = Context({'app': 'My app', 'user': request.user, 'ip_address': request.META['REMOTE_ADDR'], 'message': 'I am view 1.'})
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

def csv_writer(data, path):
    with open(path, "a+", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(data)
        
def andrews_curve(x,theta):
  curve = list()
  for th in theta:
    x1 = x[0] / np.sqrt(2)
    x2 = x[1] * np.sin(th)
    x3 = x[2] * np.cos(th)
    x4 = x[3] * np.sin(2.*th)
    curve.append(x1+x2+x3+x4)
  return curve

def plotting():
    accuracy = 1000
    samples = np.loadtxt('data_move.csv', usecols=[0,1,2,3], delimiter=',')
    theta = np.linspace(-np.pi, np.pi, accuracy)

    for s in samples[:20]: # setosa
        pl.plot(theta, andrews_curve(s, theta), 'r')

    pl.xlim(-np.pi,np.pi)
    pl.show()