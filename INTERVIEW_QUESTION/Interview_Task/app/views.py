from django.http import JsonResponse
import requests
from app.models import Population
from rest_framework import status,response
from rest_framework.views import APIView
from app.serializers import PopulationSerializer

def get_population(request):
    url = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"
    response = requests.get(url)
    data = response.json()["data"]
    for country in data:
        Population.objects.create(country=country["Nation"], year=country["Year"], human_count = country["Population"])
        print("Saved data")
    return JsonResponse(data, safe=False)

class PopulationView(APIView):

    def get(self,request,pk=None,format=None):
        if pk is None:
            result = Population.objects.all()
            respone = PopulationSerializer(result,many=True)
            return response({"Status": status.HTTP_200_OK,"Payload":respone.data})
        
        else:
            result = Population.objects.get(id=pk)
            response = PopulationSerializer(result)
            return response({"Status": status.HTTP_200_OK,"Payload":response.data})