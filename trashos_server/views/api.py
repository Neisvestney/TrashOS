from django.contrib.auth.decorators import login_required
from django.utils.timezone import now

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from trashos_server.models import Trash, TrashSensorData


def get_trashes(request):
    return JsonResponse({
        'trashes': [t.to_json() for t in Trash.objects.all()]
    })


@csrf_exempt
def new_data(request):
    try:
        trash = Trash.objects.get(key=request.GET.get('key'))
        for k, v in request.GET.dict().items():
            if k == 'key': continue
            sensor = trash.trashsensor_set.get(name=k)
            TrashSensorData.objects.create(sensor=sensor, data=v, date=now())

        return HttpResponse("OK")
    except Trash.DoesNotExist:
        return HttpResponse("403")


@login_required
def get_details(request):
    if (name := request.GET.get("name")) is not None:
        trash = Trash.objects.get(display_address=name)
        return JsonResponse({'detailFullness': [s.last_data.to_json() for s in trash.trashsensor_set.all() if s.last_data]})
    return HttpResponse("403")
