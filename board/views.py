from django.http import HttpResponseRedirect
from django.shortcuts import render
from board.models import Board

# Create your views here.
def writeform(request):
    try:
        if request.session['authuser'] is not None:
            return render(request, 'board/write.html')
    except:
        return HttpResponseRedirect('/user/loginform')

def list(request):
    board_list = Board.objects.all().order_by('-regdate')
    context = {'board_list' : board_list}
    return render(request, 'board/list.html', context)

def write(request):
    board = Board()
    board.user_id = request.session['authuser']['id']
    board.title = request.POST['title']
    board.content = request.POST['content']

    board.save()

    return HttpResponseRedirect('/board')

def view(request):
    try:
        exception = request.session['authuser']['id'] # 로그인 되어있지 않을 시 예외발생시키는 코드
        board_list = Board.objects.filter(id=request.GET['id'])
        context = {'board_list': board_list}
        return render(request, 'board/view.html', context)
    except:
        return HttpResponseRedirect('/user/loginform')


def delete(request):
    try:
        if int(request.GET['user_id']) == int(request.session['authuser']['id']):
            Board.objects.filter(id=request.GET['id'], user_id=request.GET['user_id']).delete()
            return HttpResponseRedirect('/board')
        else:
            return HttpResponseRedirect('/board')
    except:
        return HttpResponseRedirect('/user/loginform')

def modifyform(request):
    if int(request.GET['user_id']) == int(request.session['authuser']['id']):
        board_list = Board.objects.filter(id=request.GET['id'])
        context = {'board_list' : board_list}
        return render(request, 'board/modify.html', context)
    else:
        return HttpResponseRedirect('/board/view?id=' + request.GET['id'])

def modify(request):
    board_rm = Board.objects.filter(id=request.GET['id'])
    for boards in board_rm:
        boards.title = request.POST['title']
        boards.content = request.POST['content']

        boards.save()

    return HttpResponseRedirect('/board/view?id=' + request.GET['id'])