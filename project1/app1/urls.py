from django.urls import path
from . import views

urlpatterns=[
    path('a1/',views.addv, name="add_url"),
    path('s1/',views.showv, name="show_url"),
    path('u1/<int:op>/',views.updatev, name="update_url"),
    path('d1/<int:op>/',views.deletev, name="delete_url")
]