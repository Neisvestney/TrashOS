from django.contrib import admin

from trashos_server.models import Trash, TrashSensor, TrashSensorData

admin.site.register(Trash)
admin.site.register(TrashSensor)
admin.site.register(TrashSensorData)
