from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
import requests
from core.api.serializers import ParameterSerializer

class GatewayAPI(viewsets.GenericViewSet):
    filterset_fields = ["name", "status"]
    serializer_class = None

    # character/?name=rick&status=alive&species=human
    @action(detail=False, methods=["post"], serializer_class=ParameterSerializer)
    def rick_and_mort_api(self, request):
        parameter = request.data.get("parameter")
        response = requests.get(f'https://rickandmortyapi.com/api/{parameter}')
        return Response(response.json())

    # pair/EUR/GBP
    # latest/USD
    # https://www.exchangerate-api.com/docs/standard-requests
    @action(detail=False, methods=["post"], serializer_class=ParameterSerializer)
    def converter_api(self, request):
        parameter = request.data.get("parameter")
        response = requests.get(f'https://v6.exchangerate-api.com/v6/29930766e126894647e9a551/{parameter}')
        return Response(response.json())

    @action(detail=False, methods=["get"])
    def pokemon_api(self, request):
        response = requests.get('https://pokeapi.co/api/v2/pokemon-species/')
        return Response(response.json())
    
    @action(detail=False, methods=["get"])
    def cats_facts_api(self, request):
        response = requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=1')
        return Response(response.json())

