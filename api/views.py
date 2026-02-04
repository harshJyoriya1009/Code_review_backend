import requests
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# N8N_WEBHOOK_URL = "http://localhost:5678/webhook/analyze-repo"
N8N_WEBHOOK_URL = "http://localhost:5678/webhook-test/analyze-repo" 

@csrf_exempt
def analyze_code(request):
    if request.method == "OPTIONS":
        return JsonResponse({}, status=200)
    
    if request.method != "POST":
         return JsonResponse({"error": "POST only"}, status=405)

    
    try:
        body=json.loads(request.body)

        response = requests.post(
            N8N_WEBHOOK_URL,
            json=body,
            timeout=500
        )
        return JsonResponse(response.json(), safe=False)
    
    except Exception as e:
        return JsonResponse(
            {"error":str(e)},
            status=500
        )

