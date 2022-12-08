from django.http import JsonResponse
from api.models import Drink
from api.serializers import DrinkSerializer

# Create your views here.

def drink_list(request):
    # get all the drinks
    # serialize them
    # return JSON


    # Get all the drinks.
    drinks = Drink.objects.all()

    # Serialize them.
    serializer = DrinkSerializer(drinks, many=True)

    # Return JSON.
    return JsonResponse({'drinks': serializer.data})


