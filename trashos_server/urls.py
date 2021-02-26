from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from trashos_server.views.index import index, info
from trashos_server.views.panel import panel
from trashos_server.views.api import get_trashes, new_data

urlpatterns = [
    path('', index, name='index'),
    path('info/', info, name='info'),

    path('panel/', panel, name='panel'),

    path('api/trashes/', get_trashes, name='trashes'),
    path('api/trash/data/', new_data, name='new_data'),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]
