from django.shortcuts import render

# Create your views here.

def form(request):
    return render(request, 'form.html')

def result(request):
    print(request.POST)
    return render(request, 'result.html', {"data":request.POST})