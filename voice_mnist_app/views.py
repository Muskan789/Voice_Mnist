from django.shortcuts import render
import librosa
# Create your views here.

def getmain(request):
    return render(request,'index.html')

def solve(request):
    print('its working')
    blob = request.FILES['audio_data']
    print(blob)
    print('hahaha')


    return render(request,'display.html')


