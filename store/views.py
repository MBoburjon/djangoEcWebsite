from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Store

def index(request):
  products = Store.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'products': products,
  }
  return HttpResponse(template.render(context, request))


def cart(request):
  products = Store.objects.all().values()
  template = loader.get_template('cart.html')
  context = {
    'products': products,
  }
  return HttpResponse(template.render(context, request))


def checkout(request):
  products = Store.objects.all().values()
  template = loader.get_template('checkout.html')
  context = {
    'products': products,
  }
  return HttpResponse(template.render(context, request))


def contact(request):
  products = Store.objects.all().values()
  template = loader.get_template('contact.html')
  context = {
    'products': products,
  }
  return HttpResponse(template.render(context, request))


def detail(request):
  products = Store.objects.all().values()
  template = loader.get_template('detail.html')
  context = {
    'products': products,
  }
  return HttpResponse(template.render(context, request))


def shop(request):
  products = Store.objects.all().values()
  template = loader.get_template('shop.html')
  context = {
    'products': products,
  }
  return HttpResponse(template.render(context, request))


def testall(request):
  products = Store.objects.all().values()
  template = loader.get_template('testall.html')
  context = {
    'products': products,
  }
  return HttpResponse(template.render(context, request))


def testDetail(request, id):
  products = Store.objects.get(id=id)
  template = loader.get_template('testDetail.html')
  context = {
    'products': products,
  }
  return HttpResponse(template.render(context, request))
