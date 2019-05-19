from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
import pickle
import numpy as np
import os
from sklearn.svm import SVC

clf = pickle.load(open('./defaultSVM','rb'))

# Create your views here.
def index(request):
    context = {
        'text': "Hello world"
    }
    return render(request,'index.html', context = context)


def detect(request):
    samples = request.GET.get("data")
    arr = np.array(samples).reshape(6,-1)
    result = clf.predict(arr).any()
    return render(request, 'index.html', result)