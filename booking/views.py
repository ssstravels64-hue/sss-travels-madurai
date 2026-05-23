from django.shortcuts import render, redirect
from .models import Booking
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from twilio.rest import Client

def home(request):
    return render(request, 'home.html')


def booking_page(request):

    if request.method == "POST":

        request.session['name'] = request.POST.get('name')
        request.session['phone'] = request.POST.get('phone')

        request.session['pickup'] = request.POST.get('pickup')
        request.session['drop'] = request.POST.get('drop')

        request.session['distance'] = request.POST.get('distance') or 0

        request.session['car_type'] = request.POST.get('car_type')

        request.session['date'] = request.POST.get('date')

        return redirect('/success/')

    
    return render(request, 'booking.html')

def success_page(request):
    return render(request, 'success.html')


def about_page(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect



from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.shortcuts import render
from .models import Booking

def payment_success(request):

    name = request.session.get('name')
    phone = request.session.get('phone')

    pickup = request.session.get('pickup')
    drop = request.session.get('drop')

    distance = request.session.get('distance') or 0

    car_type = request.session.get('car_type')

    date = request.session.get('date')

    amount = float(distance) * 20

    Booking.objects.create(
        name=name,
        phone=phone,

        pickup_location=pickup,
        drop_location=drop,

        distance=distance,

        car_type=car_type,

        travel_date=date,

        amount=amount,

        payment_status="Paid"
    )

    return render(request, 'success.html')

    return redirect("/booking/")