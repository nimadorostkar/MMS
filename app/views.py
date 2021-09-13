from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django import template
from . import models
from django.contrib.auth.models import User
from .models import Profile
from .forms import ProfileForm, UserForm
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





#------------------------------------------------------------------------------
@login_required
def profile(request):
  profile = models.Profile.objects.filter(user=request.user)
  if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            username = user_form.cleaned_data['username']
            first_name = user_form.cleaned_data['first_name']
            last_name = user_form.cleaned_data['last_name']
            email = user_form.cleaned_data['email']
            password1 = user_form.cleaned_data['password1']
            password2 = user_form.cleaned_data['password2']
            phone = profile_form.cleaned_data['phone']
            address = profile_form.cleaned_data['address']
            user_photo = profile_form.cleaned_data['user_photo']
            user_form.save()
            profile_form.save()
            context = {'profile': profile,'user_form': user_form,'profile_form': profile_form }
            return render(request, 'page-user.html', context)
  else:
      user_form = UserForm(instance=request.user)
      profile_form = ProfileForm(instance=request.user.profile)

  context = {
  'profile': profile,
  'user_form': user_form,
  'profile_form': profile_form,
  }
  return render(request, 'page-user.html', context)





#------------------------------------------------------------------------------
@login_required
def search(request):
    if request.method=="POST":
        search = request.POST['q']
        if search:
            material = models.Material.objects.filter(Q(name__icontains=search) | Q(description__icontains=search))
            product = models.Product.objects.filter(Q(name__icontains=search))
            station = models.Station.objects.filter(Q(name__icontains=search) | Q(description__icontains=search))
            match = chain(material, product, station)
            if match:
                return render(request,'search.html', {'sr': match})
            else:
                messages.error(request,  '   چیزی یافت نشد ، لطفا مجددا جستجو کنید ' )
        else:
            return HttpResponseRedirect('/search')
    return render(request, 'search.html', {})





#------------------------------------------------------------------------------
@login_required()
def mold(request):
    molds = models.Mold.objects.all()
    molds_img = models.MoldImage.objects.all()
    return render(request, 'mold.html', {'molds': molds, 'molds_img':molds_img})


@login_required()
def mold_detail(request, id):
    mold = get_object_or_404(models.Mold, id=id)
    mold_img = models.MoldImage.objects.all()
    context = {'mold':mold, 'mold_img':mold_img}
    return render(request, 'mold_detail.html', context)




#------------------------------------------------------------------------------
@login_required()
def category(request):
    category = models.Category.objects.all()
    return render(request, 'category.html', {'category': category})


@login_required()
def category_detail(request, id):
    category = get_object_or_404(models.Category, id=id)
    molds = models.Mold.objects.all()
    molds_img = models.MoldImage.objects.all()
    context = {'category':category, 'molds':molds, 'molds_img':molds_img}
    return render(request, 'category_detail.html', context)






#------------------------------------------------------------------------------
@login_required()
def manufacturer(request):
    manufacturers = models.Manufacturer.objects.all()
    return render(request, 'manufacturer.html', {'manufacturers': manufacturers})


@login_required()
def manufacturer_detail(request, id):
    manufacturer = get_object_or_404(models.Manufacturer, id=id)
    molds = models.Mold.objects.all()
    molds_img = models.MoldImage.objects.all()
    context = {'manufacturer':manufacturer, 'molds':molds, 'molds_img':molds_img}
    return render(request, 'manufacturer_detail.html', context)







#------------------------------------------------------------------------------
@login_required()
def product(request):
    products = models.Product.objects.all()
    return render(request, 'product.html', {'products': products})


@login_required()
def product_detail(request, id):
    product = get_object_or_404(models.Product, id=id)
    molds = models.Mold.objects.all()
    molds_img = models.MoldImage.objects.all()
    context = {'product':product, 'molds':molds, 'molds_img':molds_img}
    return render(request, 'product_detail.html', context)





#------------------------------------------------------------------------------
@login_required()
def manufacture_req(request):
    manufacture_requests = models.Manufacture_request.objects.all()
    return render(request, 'manufacture_req.html', {'manufacture_requests': manufacture_requests})


@login_required()
def manufacture_req_detail(request, id):
    manufacture_request = get_object_or_404(models.Manufacture_request, id=id)
    context = {'manufacture_request':manufacture_request}
    return render(request, 'manufacture_req_detail.html', context)





#------------------------------------------------------------------------------
@login_required()
def repair_req(request):
    repair_requests = models.Repair_request.objects.all()
    repair_img = models.RepairImage.objects.all()
    return render(request, 'repair_req.html', {'repair_requests': repair_requests, "repair_img":repair_img})


@login_required()
def repair_req_detail(request, id):
    repair_request = get_object_or_404(models.Repair_request, id=id)
    repair_img = models.RepairImage.objects.all()
    repair_operation = models.Repair_operation.objects.all()
    context = {'repair_request':repair_request, 'repair_img':repair_img, 'repair_operation':repair_operation}
    return render(request, 'repair_req_detail.html', context)










# End
