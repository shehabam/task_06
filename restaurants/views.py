from django.shortcuts import render, redirect
from .models import Restaurant
from .forms import RestaurantForm

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):
    context = {
        "restaurants":Restaurant.objects.all()
    }
    return render(request, 'list.html', context)


def restaurant_detail(request, restaurant_id):
    context = {
        "restaurant": Restaurant.objects.get(id=restaurant_id)
    }
    return render(request, 'detail.html', context)

def restaurant_create(request):
    restaurant = RestaurantForm()
    if request.method == "POST":
        restaurant = RestaurantForm(request.POST)
        if restaurant.is_valid():
            restaurant.save()
            return redirect('restaurant-list')

    context = {
        'restaurant': restaurant
    }

    return render(request, 'create.html', context)
