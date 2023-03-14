from django.shortcuts import render

# Create your views here.
'''def condtions(request):
    d={'a':50}
    return render(request,'condtions.html',d)

def condtions(request):
    d={'a':50,'b':90}
    return render(request,'condtions.html',d)'''

def condtions(request):
    d={'a':50,'b':900,'c':100}
    return render(request,'condtions.html',d)
