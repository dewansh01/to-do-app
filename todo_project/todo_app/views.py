from .models import Todo
from django.http import JsonResponse
from django.http import HttpResponse
# Create your views here.
def greet(request):
    return HttpResponse("No ! its not text only web page lol :) but developer is backend guy :)")
def todo_list(request):
    response = list(Todo.objects.all().values())
    return JsonResponse({'list':response})

def details(request,id):
    try:
        response=list(Todo.objects.all().filter(pk=id).values())
    except Todo.DoesNotExist:
        return JsonResponse({'error':'model doesnt exist'})
    return JsonResponse({id:response})