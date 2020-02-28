import pandas as pd
from django.shortcuts import render,redirect
from sklearn.externals import joblib
from django.shortcuts import render
from django.http import HttpResponse
# from .forms import myForm
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
import pickle
from sklearn.externals import joblib
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd
from django.contrib import messages
# Create your views here.
from .forms import UserRegisterForm,Career_Prediction
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import FormDB,User


def index(request):
    return render(request,'CCS/index.html')


def ohevalue(df):
    ohe_col=joblib.load('E:\FYP\pkl\ohe.pkl')
    cat_columns=['Best_Course','Best_Language','Certification','Interested_Area','Coding_Skills','Communication_Skills','Mangerial_Skills','Self_Learning','Reading_Writing_Skills','Working_Strategy','Solution_Provider']
    df_processed=pd.get_dummies(df,columns=cat_columns)
    newdict={}
    for i in ohe_col:
        if i in df_processed.columns:
            newdict[i]=df_processed[i].values
        else:
            newdict[i]=0
    newdf=pd.DataFrame(newdict)
    return newdf

def approvereject(unit):
    try:
        mdl=joblib.load("E:\FYP\pkl\model.pkl")
        print(unit)
        y_pred=mdl.predict(unit)
        newdf=pd.DataFrame(y_pred,columns=['Academia','Data Scientist','Mobile App Developer','Project Manager','Software Engineer','Tester','Web Developer'])
        suggest=""
        for i in newdf.columns:
            if newdf[i].values==1:
                suggest=i
        return (' {}'.format(suggest))
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)


def userparameters(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = Career_Prediction(request.POST)
            if form.is_valid():
                myDict = (request.POST).dict()
                df = pd.DataFrame(myDict, index=[0])
                print(df)
                career_suggestion = approvereject(ohevalue(df))
                form_id=form.save()
                form_pk=form_id.pk
                f=FormDB.objects.get(pk=form_pk)
                f.Suggestion=career_suggestion
                f.user_id_id=request.user.id
                f.save()
                messages.success(request, 'The Career We suggest for You is  {}'.format(career_suggestion))

        form = Career_Prediction()
        return render(request, 'CCS/form.html', {'form': form})
    else:
        redirect('login')


def contact(request):
    return render(request,"CCS/contact.html")


def ourteam(request):
    return render(request,'CCS/team.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'CCS/register.html', {'form': form})






