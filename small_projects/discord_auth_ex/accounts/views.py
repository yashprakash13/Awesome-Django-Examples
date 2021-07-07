from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
import requests


@login_required()
def home(request):
    return JsonResponse({'msg' : f'Hello {request.user.nickname}'})

