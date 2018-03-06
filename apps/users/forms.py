from django import forms
from django.contrib.auth.models import User
from passwords.fields import PasswordField
from django.core.exceptions import ValidationError
from passwords.validators import ComplexityValidator


def validate_equel(val1, val2):
    if val1 != val2:
        raise ValidationError('两次输入密码不一样，请重新输入！')


class FormWidget(forms.TextInput):
    """docstring for FormWidget"""
    @property
    def media(self):
        return forms.Media(
            css={"all": ("/static/novel/css/index.css")},
        )


class LoginForm(forms.Form):
    user_name = forms.CharField(
        label='用户', min_length=4, max_length=16, widget=forms.TextInput(attrs={"placeholder": "请输入用户名"}))
    user_passwd = forms.CharField(label='密码', min_length=6, max_length=18,
                                  widget=forms.TextInput(attrs={"placeholder": "请输入用户密码", "type": "password"}))

    # class Meta:
    #     # model = LoginForm
    #     widgets = {
    #         "user_name": forms.TextInput(attrs={'placeholder': '请输入用户名'}),
    #     }


class RegisterForm(forms.Form):

    forms.Form.error_css_class = 'error'

    user_name = forms.CharField(
        help_text='请输入用户名(必填)',
        error_messages={'required': '请填写名字'},
        min_length=4,
        max_length=16,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入用户名（必填）'})
    )

    user_passwd = PasswordField(
        help_text='请输入密码(必填)',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请输入密码（必填）'})
    )

    user_passwd_confirm = PasswordField(
        help_text='请再次输入密码(必填)',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请再次输入密码（必填）'})
        # widget=forms.PasswordInput,
    )
    user_email = forms.EmailField(
        help_text='请输入邮箱(选填)',
        required=False,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '请输入邮箱'})
    )
    auto_login = forms.BooleanField(
        label='自动登录',
        widget=forms.CheckboxInput(attrs={'checked': "checked", 'placeholder': '自动登录'}),       required=False
    )

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        user_name = cleaned_data.get('user_name')
        user_passwd = cleaned_data.get('user_passwd')
        user_passwd_confirm = cleaned_data.get('user_passwd_confirm')
        if User.objects.filter(username=user_name).count():
            # raise forms.ValidationError('用户名已存在，请换其他用户名！')
            msg = '用户名已存在，请换其他用户名！'
            self.add_error('user_name', msg)
        if user_passwd and user_passwd_confirm and user_passwd != user_passwd_confirm:
            msg = '两次输入密码不一致，请重新输入！'
            self.add_error('user_passwd', msg)
        return cleaned_data

    def clean_password(self):
        cleaned_data = super(RegisterForm, self).clean()
        user_passwd = cleaned_data.get('user_passwd')
        user_passwd_confirm = cleaned_data.get('user_passwd_confirm')
        if user_passwd and user_passwd_confirm and user_passwd != user_passwd_confirm:
            raise forms.ValidationError('两次输入密码不一致，请重新输入！')
        return cleaned_data

    class Meta:
        model = User


# class SearchForm(forms.Form):
#     keywords = forms.CharField(label='书名', min_length=1, max_length=100)
