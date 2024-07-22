from django.http import JsonResponse

def say_hello(request):
    return JsonResponse({"message": "Hello User"})
