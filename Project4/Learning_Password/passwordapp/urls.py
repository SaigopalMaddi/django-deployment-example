from django.urls import path,include
from passwordapp import views

app_name = 'passwordapp'

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('user_login/',views.user_login, name='user_login'),
]
