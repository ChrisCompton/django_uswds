from django.shortcuts import render

# Create your views here.
def demo(request):
    return render(request, 'demo.html')