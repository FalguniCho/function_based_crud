from django.urls import path
from . import views

urlpatterns=[
    path('s2/',views.signup,name="signup_url"),
    path('l2/',views.loginv,name='loginv_url'),
    path('lg2/',views.logoutv,name='logoutv_url')
]