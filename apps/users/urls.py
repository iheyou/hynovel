from django.conf.urls import url

from users import views
app_name = 'users'
#
urlpatterns = [
    url(r'^register', views.sign_up, name='register'),
    url(r'^info', views.user_info, name='userinfo'),
    url(r'^collect', views.novel_collect, name='collect'),
    url(r'^is_collected', views.get_collect_info, name='collected'),
    url(r'^bookrack', views.bookrack, name='bookrack'),
    url(r'^[a-zA-Z0-9]{4:16}', views.user_content, name='users')
#     url(r'^login/', views.sign_in, name='login'),
]
