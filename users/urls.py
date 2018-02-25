from django.conf.urls import url
from django.contrib.auth.views import login
from . import views
'''Defining URL Patterns for users'''
app_name='users'
urlpatterns=[
    #Login Page
    url(r'^login/$',login,{'template_name':'users/login.html'},name='login'),
    #Log Out
    url(r'^logout/$',views.logout_view,name='logout'),
    url(r'^register/$',views.register,name='register')
]
