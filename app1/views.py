from django.shortcuts import render

# Create your views here.

def kiddo(request):
    return render(request,'kiddo.html')