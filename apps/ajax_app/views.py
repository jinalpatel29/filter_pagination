# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Lead
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def index(req):  
    if (req.method == "POST"):
        return render(req, 'ajax_app/index.html', Lead.objects.getLeads(req.POST))
    leads = Lead.objects.all()
    pages = len(leads)   
    return render(req, 'ajax_app/index.html', Lead.objects.getLeads(None), {'range': range(0, pages)})

# def reset(req):   
#     return redirect('/')