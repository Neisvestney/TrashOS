from django.http import JsonResponse

from trashos_server.models import Trash


def get_trashes(request):
    return JsonResponse({
        'trashes': [t.to_json() for t in Trash.objects.all()]
    })
