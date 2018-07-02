from django.shortcuts import render
from django.http import HttpResponseRedirect
from guestbook.models import Guestbook
# Create your views here.
def deleteform(request):
    id = request.GET.get('id')
    context = {'id' : id}
    return render(request, 'guestbook/deleteform.html', context)

def delete(request):
    Guestbook.objects.filter(id=request.POST['id']).filter(password=request.POST['password']).delete() # 필터 = where절과 비슷
    return HttpResponseRedirect('/guestbook')

def list(request):
    guestbook_list = Guestbook.objects.all().order_by('-regdate') # all은 모든 객체 가져옴
    context = {'guestbook_list' : guestbook_list}
    return render(request, 'guestbook/list.html', context)

def add(request):
    guestbook = Guestbook()
    guestbook.name = request.POST['name']
    guestbook.password = request.POST['password']
    guestbook.message = request.POST['message']

    guestbook.save()

    return HttpResponseRedirect('/guestbook')

