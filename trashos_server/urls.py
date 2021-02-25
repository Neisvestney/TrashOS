from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from trashos_server.views.index import index, info
from views.panel import panel

urlpatterns = [
    path('', index, name='index'),
    path('info/', info, name='info'),

    path('panel/', panel, name='panel'),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]
