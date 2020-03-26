from django.http import JsonResponse
from journal.models import Entry
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
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
