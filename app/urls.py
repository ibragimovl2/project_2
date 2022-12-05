from django.urls import path, include
from app.views import *




urlpatterns = [
    path('', index, name='index'),
    path('biz_haqimiz/<int:id>/', biz_haqimiz, name='biz_haqimiz'),
    path('blog/<int:id>/', blog, name='blog'),
    path('post/', post, name='post'),
    path('bandqilish/', bandqilish, name='bandqilish')

]