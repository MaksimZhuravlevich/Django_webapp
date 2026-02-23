from django.urls import path
from . import views

urlpatterns = [
    path('',views.news_home,name="news_home"),
    path('create',views.create,name="create"),
    path('news_create',views.news_create,name="news_create")
    # path('number',views.number,name="kontacts")
]
