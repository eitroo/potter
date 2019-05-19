from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
import pickle
import numpy as np
import os

clf = pickle.load(open('./defaultSVM','rb'))

# Create your views here.
def index(request):
    context = {
        'text': "Hello world"
    }
    return render(request,'index.html', context = context)


def detect(request):
    samples = dict(request.GET)
    print(samples)
    samples = samples.get('data[]')
    arr = np.array(samples).reshape(6,-1)
    result = clf.predict(arr).any()
    return render(request, 'index.html', int(result))