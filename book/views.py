from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def search_id(request):
    return HttpResponse("这是一个测试！")