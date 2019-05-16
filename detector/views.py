from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from sklearn.svm import SVC
import pickle
import numpy as np
import os

pothole = False
clf = pickle.load(open(os.getcwd()+'\defaultSVM'))
# Create your views here.
def index(request):

    return render(request,'detector/index.html', context = {'pothole':pothole})

def detect(request, samples):
    arr = np.array(samples['data']).reshape(-1,6)
    return render(request, 'detector/index.html', clf.predict(samples['data'].reshape()).any())