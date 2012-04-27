# -*- coding: utf-8 -*-


from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from forms import CommandForm
from arduino.arduinoControl import ArduinoControl

def commandline(request):
    text=""
    morse=[]
    if request.method == 'GET':         
        form = CommandForm(request.GET) 
        if form.is_valid():
            text = form.cleaned_data['text']
            arduino=ArduinoControl(text)
            arduino.start()
        else:
            queryset = []
    form = CommandForm() 
    return render_to_response("arduino/index.html", {'form': form, "text": text})
    
