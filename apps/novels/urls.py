from django.conf.urls import url
from novels import views

app_name = 'novels'
urlpatterns = [
    # url(r'^variety/', include('novel.urls')),
    url(r'^category/(?P<variety>[a-zA-z]{3,8})/(?P<page>[0-9]*)',
        views.novels, name='novel_variety'),
    url(r'^info/(?P<novel_id>[0-9a-zA-Z]+)',
        views.novel_detail, name='novel_detail'),
    url(r'^catalogue/(?P<novel_id>[0-9a-zA-Z]+)/(?P<sort_by>(asc|desc)?)/(?P<chap_page>[0-9]+)',
        views.chapter_list, name='chapter_list'),
    # url(r'^users/(?P<type>login|register|[0-9a-zA-Z]+)$',
    #     views.login, name='user_login'),
    url(r'^search/$', views.search, name='search'),

]
