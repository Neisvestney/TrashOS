from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from trashos_server.views.index import index

urlpatterns = [
    path('', index, name='index'),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]
