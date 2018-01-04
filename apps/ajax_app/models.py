# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import math
from django.db import models
from django.utils import timezone
from datetime import datetime
from django.db.models import Q

# Create your models here.
class LeadManager(models.Manager):
    def getLeads(self, POST):       
        if POST:
            page = int(POST['page'])
            name = POST['name']
            fromDate = POST['from']
            toDate = POST['to']
            # count = POST['count']
        else:
            page = 1
            name = ''
            fromDate = ''
            toDate = ''
            # count = 2
        if fromDate == '':
            fromDate = datetime(1800, 01, 01)
        if toDate == '':
            toDate = timezone.now()
      
        leads_total = Lead.objects.filter(Q(first_name__contains=name) | Q(last_name__contains=name)).filter(Q(created_at__range=[fromDate, toDate]))
        
        leads = []
        count = 2
        print count
        while count > 0:
            if ((page * 2) - count) < len(leads_total):
                leads.append(leads_total[((page * 2) - count)])
            count -= 1

        result = {
            'leads' : leads,
            'range' : range(0, int(math.ceil(len(leads_total) / 2.0)))
        }
        return result


class Lead(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = LeadManager()