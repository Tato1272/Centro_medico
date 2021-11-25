from django.shortcuts import render

# Create your views here.

def return_base(request):
    return render(request,"base.html")
