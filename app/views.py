from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request,'main.html')

def amazon(request):
    return render(request,'amazon.html')

def flipkart(request):
    return render(request,'flipkart.html')

def myntra(request):
    return render(request,'myntra.html')