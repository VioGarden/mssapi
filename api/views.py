from django.shortcuts import render

from django.http import JsonResponse

def api_home(request):
    data = {"Remember": "uru, coldrain, sawano"}
    return JsonResponse(data)
