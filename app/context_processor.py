from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from . import models
from .models import Repair_request







def repair_req_notif(request):
    return {
    'repair_req_notif':models.Repair_request.objects.filter(Status='جدید'),
    'notif':models.Repair_request.objects.filter(Status='جدید').count()
     }
