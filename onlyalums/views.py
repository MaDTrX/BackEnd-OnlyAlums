from django.shortcuts import render

# Add the following import
from django.http import JsonResponse

# Define the home view
def home(request):
  return JsonResponse({'foo':'bar'})