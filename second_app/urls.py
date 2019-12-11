from django.urls import path

from . import views


urlpatterns=[
    path('',views.index,name='index'),
    path('form_view/',views.form_view,name='form_view'),
]
