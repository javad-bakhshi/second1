
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('second_app/',include('second_app.urls')),
    path('admin/', admin.site.urls),
]
