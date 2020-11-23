from django.shortcuts import render

def taskLista(request):
    return render(request, 'tasklist.html')

# Create your views here.
