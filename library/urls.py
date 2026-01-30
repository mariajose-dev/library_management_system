from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-genre/', views.add_genre, name='add_genre'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # <- logout URL
    path('add-author/', views.add_author, name='add_author'),
    path('add-language/', views.add_language, name='add_language'),
    path('add-book/', views.add_book, name='add_book'),
]
