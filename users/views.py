from django.shortcuts import render

from django.http import JsonResponse

def users_home(request):
    data = {"users":"Violet!!!"}
    return JsonResponse(data)
