from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib import auth

from users.forms import LoginForm, RegisterForm


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
            # user = UserProfile.objects.create_user(
            #     username=username,
            #     password=password,
            #     email=user_email,
            # )
            # user.save()
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


def sign_in(request):
    redirect_to = request.POST.get('next', request.GET.get('next'))
    # if request.method == 'POST':
    #     form = LoginForm(request.POST)
    #     if form.is_valid():
    #         users = auth.authenticate(
    #             user_name=request.POST['user_name'], user_passwd=request.POST['user_passwd'])
    #         auth.login(request, users)
    #         messages.success(request, '登录成功，正在跳转页面！')
    #         request.session.clear_expired()
    #         return render(request, 'users/users.html')
    #     else:
    #         return render(request, 'users/users.html', {'form': form})
    # else:
    form = LoginForm()
    return render(request, 'users/login.html', {'form': form, 'next':
redirect_to})