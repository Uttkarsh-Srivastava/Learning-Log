from django.conf.urls import url
from . import views

'''Defining url pattern for loging_logs'''
app_name='learning_logs'

urlpatterns=[
    #homepage
    url(r'^$',views.index,name='index'),
    #displaying topics
    url(r'^topics/$',views.topics,name='topics'),
    #displaying entries of topics
    url(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),
    #Page for adding new topics
    url(r'^new_topic/$',views.new_topic,name='new_topic'),
    url(r'^new_topic(?P<topic_id>\d+)/$',views.new_entry,name='new_entry'),
    url(r'^edit_entry/(?P<entry_id>\d+)/$',views.edit_entry,name='edit_entry'),
    
]
