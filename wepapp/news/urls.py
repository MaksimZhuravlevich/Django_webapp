from django.urls import path
from . import views

urlpatterns = [
    path('',views.news_home,name="news_home"),
    path('create',views.create,name="create"),
    path('news_create',views.news_create,name="news_create"),
    path('article/<int:pk>',views.NewsDetailView.as_view(),name='news_detail'),
    path('newspaper/<int:pk>',views.NewspaperDetailView.as_view(),name='newspaper_detail'),
    path('article/<int:pk>/news_update',views.NewsUpdateView.as_view(),name='news_update'),
    path('article/<int:pk>/news_delete',views.NewsDeleteView.as_view(),name='news_delete'),
    # path('number',views.number,name="kontacts")

]
