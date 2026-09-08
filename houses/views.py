from django.shortcuts import render
from django.http import JsonResponse
from .models import Houses
# Create your views here.
def house_list(request):
    houses=Houses.objects.all()
    data=[]
    for house in houses:
        data.append({
            "house_id":house.house_id,
            "title":house.title,
            "bsa":house.business_area
        })
    return JsonResponse({
            "code":200,
            "message":"查询成功",
            "data":data
        })
    