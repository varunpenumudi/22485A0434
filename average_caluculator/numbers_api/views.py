from django.shortcuts import render
from django.http import JsonResponse
import requests

def average(lis):
    product = 1
    for num in lis:
        product *= num

# Create your views here.
def get_numbers(request, numberid):
    if request.method != "GET":
        return JsonResponse({"Error":"GET Request Required."})
    
    if not ( numberid in ['p','f','e','r'] ):
        return JsonResponse({
            "error":"page not found",
        }, status=404)
    
    test_response = requests.get("", timeout=0.5)
    if test_response:
        return JsonResponse({"error":"timeout"}, status="400")
    
    response = {
        "numbers": [],
        "windowPrevState": [],
        "windowCurrState": [],
        "avg": average([])
    }
    return JsonResponse({"message":"sucess",}, status = 200)