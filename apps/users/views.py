from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib import auth

from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from users.models import UserCollectNovels
from users.forms import LoginForm, RegisterForm
from novels.models import Novel


# class DivErrorList(ErrorList):
#     def __str__(self):
#         return self.as_divs()
#
#     def as_divs(self):
#         if not self:
#             return ''
# return '<div class="errorlist alert alert-danger" role="alert">%s</div>'
# % ''.join(['<div class="error">%s</div>' % e for e in self])


def sign_up(request):
    redirect_to = request.POST.get('next', request.GET.get('next'))
    if request.method == 'POST':
        signup_form = RegisterForm(request.POST)
        if signup_form.is_valid():
            signup_info = signup_form.cleaned_data
            username = signup_info['user_name']
            password = signup_info['user_passwd']
            user_email = signup_info['user_email'] if signup_info[
                'user_email'] else None
            user = User.objects.create_user(
                username=username,
                password=password,
                email=user_email,
            )
            user.save()
            messages.success(request, '注册成功，正在跳转页面！')
            if signup_info['auto_login']:
                user = auth.authenticate(
                    username=username, password=password)
                auth.login(request, user)
                if redirect_to:
                    return HttpResponseRedirect(redirect_to)
                else:
                    return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/')
        else:
            return render(request, 'users/register.html', {'form': signup_form})
    else:
        form = RegisterForm()
        return render(request, 'users/register.html', {
            'form': form,
            'next': redirect_to
        })


# def sign_in(request):
#     redirect_to = request.POST.get('next', request.GET.get('next'))
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             users = auth.authenticate(
#                 user_name=request.POST['user_name'], user_passwd=request.POST['user_passwd'])
#             auth.login(request, users)
#             messages.success(request, '登录成功，正在跳转页面！')
#             request.session.clear_expired()
#             return render(request, 'users/users.html')
#         else:
#             return render(request, 'users/users.html', {'form': form})
#     else:
#         form = LoginForm()
# return render(request, 'users/login.html', {'form': form, 'next':
# redirect_to})


def user_info(request):
    user_id = request.session.get('_auth_user_id')
    if user_id:
        username = User.objects.get(id=user_id)
        return render(request, 'users/user.html', {'users': username})
    else:
        return HttpResponseRedirect('/users/login')


def novel_collect(request):
    novel_id = request.GET['novel_identify']
    novel = Novel.objects.get(book_identify=novel_id)
    user_id = request.session.get('_auth_user_id')
    is_collect = request.GET['is_collect']
    if novel_id and user_id and is_collect == 'False':
        UserCollectNovels.objects.get_or_create(
            user_id=user_id,
            novel_name=novel.book_name,
            novel_identify=novel_id,
            novel_image=novel.book_image,
            novel_author=novel.book_author,
            novel_latest=novel.book_latest
        )
        return HttpResponse("200 ok")
    elif novel_id and user_id and is_collect == 'True':
        UserCollectNovels.objects.filter(
            user_id=user_id,
            novel_identify=novel_id
        ).delete()
        return HttpResponse("200 ok")
    elif novel_id and user_id:
        is_collected = UserCollectNovels.objects.get(
            user_id=user_id,
            novel_identify=novel_id
        )
        if is_collected:
            return HttpResponse("True")
        else:
            return HttpResponse('False')
    else:
        return HttpResponse("")


def get_collect_info(request):
    novel_id = request.GET['novel_identify']
    user_id = request.session.get('_auth_user_id')
    if novel_id and user_id:
        try:
            UserCollectNovels.objects.get(
                user_id=user_id,
                novel_identify=novel_id
            )
            return HttpResponse("True")
        except Exception as error:
            return HttpResponse(error)
    else:
        return HttpResponse('')


def bookrack(request):
    user_id = request.session.get('_auth_user_id')
    if user_id:
        try:
            novel_list = UserCollectNovels.objects.filter(user_id=user_id).order_by('-add_date')
            return render(request, 'users/bookrack.html', {'novels': novel_list})
        except Exception as error:
            return HttpResponse(error)
