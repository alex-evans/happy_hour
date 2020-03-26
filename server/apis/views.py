from django.http import JsonResponse
from journal.models import Entry


def apis_view(request):
    if request.POST:
        print("POST")
        data = {
            'name': 'post'
        }
    data = {
        'name': 'test'
    }
    
    return JsonResponse(data)
