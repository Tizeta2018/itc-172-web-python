from django.urls import path
from . import views


urlpatterns =[
    path('', views.index,name='index' ),
    path('clubmeetings/', views.clubmeetings, name='meetings' ),
    path('clubminutes/', views.clubminutes, name='minutes' ),
    path('clubresources/', views.clubresources, name='resources' ),
    path('getmeeting/', views.getmeeting, name='getmeeting' ),
    path('meetingdetail/<int:id>', views.meetingdetail, name='details'),
]
