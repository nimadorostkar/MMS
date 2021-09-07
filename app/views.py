from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django import template
from . import models
from django.contrib.auth.models import User
from .models import Profile
#from .forms import ProfileForm, UserForm, TicketForm, InventoryForm
from itertools import chain
from django.contrib.auth import get_user_model
from django.db import transaction
from django.urls import reverse
from django.db.models import Q
import datetime





#------------------------------------------------------------------------------
@login_required()
def index(request):
    s = "ssss"
    context = {'s':s}
    return render(request, 'index.html', context)







# End
