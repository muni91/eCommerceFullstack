from django.http.response import HttpResponse
from django.http import JsonResponse

# Create your views here.
def home(request):
    return JsonResponse({'muni':'creator','purpose':'complete_functional_website'})
