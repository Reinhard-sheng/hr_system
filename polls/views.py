from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Interviewer, InterviewProcess, SassUser
from django.template import loader
from django.shortcuts import redirect


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = SassUser.objects.filter(name=username, password=password)
    if user.exists():
        return HttpResponseRedirect('/polls/home')
    else:
        return HttpResponse('Login fail.')


def login_fail(request, name):
    return HttpResponse("Login fail %s" % name)


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))


def login_check(request, login, password):
    user = SassUser.objects.filter(name=login, password=password)
    if user:
        response = redirect('polls')
        return response
    else:
        return redirect('login_fail')


def interviewer(request, uid):
    # 校验session
    interviewer = Interviewer.objects.filter(id=uid)
    process_list = InterviewProcess.objects.filter(interviewer=uid).all()
    process_list_new = []
    status = {}
    status_dict = {}
    for flag, state in InterviewProcess.CHOICES:
        if flag == 'p':
            info = 'green'
        elif flag == 'f':
            info = 'red'
        else:
            info = 'pink'
        status[flag] = info
        status_dict[flag] = state
    for process in process_list:
        process_list_new.append((process.name, status.get(
            process.status), status_dict.get(process.status)))
    template = loader.get_template('interviewer.html')
    context = {
        'interviewer': interviewer[0],
        'process_list': process_list_new,
    }
    return HttpResponse(template.render(context, request))


def home(request):
    # 校验session
    sass_user_id = get_uid_from_session()
    interviewer_list = Interviewer.objects.filter(sass_user=sass_user_id)
    template = loader.get_template('home.html')
    context = {
        'interviewer_list': interviewer_list,
    }
    return HttpResponse(template.render(context, request))


# 校验session
def check_session(request):
    pass

def get_uid_from_session(request):
    # return a sass user id
    pass