from django.urls import path
from .views import login_view
from .views import RegisterView

urlpatterns=[
path('login/',login_view,name='login'),
path('register/',RegisterView.as_view(),name='register'), # Class Based View
]