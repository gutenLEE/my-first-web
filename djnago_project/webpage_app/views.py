from django.shortcuts import render

#
def index(request):
    print("============================")
    return render(request, 'index.html')

def weather(request):
    return render(request, 'weather index.html')

def transportaion(request):
    return render(request, 'transportaion index.html')