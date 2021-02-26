from django.db import models
from django.utils import timezone


class Trash(models.Model):
    x = models.FloatField("Координата X")
    y = models.FloatField("Координата Y")
    display_address = models.CharField("Отображаемый адрес", max_length=100)
    key = models.CharField("Ключ", max_length=16, unique=True)

    def __str__(self):
        return self.display_address

    def get_fullness(self):
        return max([x.last_data.data if x.last_data else 0 for x in self.trashsensor_set.all()])

    def to_json(self):
        return {
            'x': self.x,
            'y': self.y,
            'address': self.display_address,
            'fullness': self.get_fullness()
        }


class TrashSensorData(models.Model):
    sensor = models.ForeignKey("TrashSensor", on_delete=models.CASCADE)
    date = models.DateTimeField("Время")
    data = models.FloatField("Заполненость")

    def __str__(self):
        return f"[{self.date.strftime('%d.%m.%Y %H:%M:%S UTC')}] {self.data * 100}% - {self.sensor.display_name} - {self.sensor.trash.display_address}"

    def to_json(self):
        return {
            'displayName': self.sensor.display_name,
            'data': self.data
        }


class TrashSensor(models.Model):
    trash = models.ForeignKey(Trash, on_delete=models.CASCADE)

    display_name = models.CharField("Отображаемое название", max_length=64)
    name = models.CharField("Название", max_length=64)

    @property
    def last_data(self) -> TrashSensorData:
        return self.trashsensordata_set.last()

    def __str__(self):
        return f"{self.display_name} - {self.trash.display_address}"
