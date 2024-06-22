from django.urls import path
from . import views
from .views import CustomLoginView


urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('register/', views.user_register, name='register'),
    path('login/', CustomLoginView.as_view() , name='login'),
    path('logout/', views.user_logout_view, name='logout'),
    path('detail/<int:pk>', views.news_detail_view, name='detail'),
    path('news_create/', views.news_create, name='create'),
    path('news_delete/<int:pk>', views.news_delete, name='delete'),
    path('author_list/', views.author_list, name='author')
]