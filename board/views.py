from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

def writeform(request):
    # 인증 체크
    if request.session['authuser'] is None:
        return HttpResponseRedirect('/user/loginform')