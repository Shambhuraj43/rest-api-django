from django.http import JsonResponse
from api.models import Drink
from api.serializers import DrinkSerializer
# Import Decorators
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def drink_list(request):
    # get all the drinks
    # serialize them
    # return JSON

    if request.method == 'GET':
        # Get all the drinks.
        drinks = Drink.objects.all()

        # Serialize them.
        serializer = DrinkSerializer(drinks, many=True)

        # Return JSON.
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id):
    
    try:
        # Get the object with specific id
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        # If object does not exists, throw 404.
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


