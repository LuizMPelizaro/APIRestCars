from django.http import JsonResponse


def cars(request):
    if request.method == 'GET':
        car = {
            'model': 'A8',
            'car_year': '2020',
            'car_brand': 'Audi'
        }
        return JsonResponse(car)
