from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

import users
from .models import *
from .forms import *


def home(request):
    category = Category.objects.all()
    reviews = Review.objects.all()
    form = ReviewForm(request.POST or None)
    room = Review.objects.all()

    if request.method == "POST" and form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        # instance.room = room
        instance.save()
        return redirect("hotel:home")
    return render(
        request, "home.html", { "reviews": reviews, "form": form, 'category':category}
    )


def services(request):
    return render(request, "services.html")


def RoomListView(request, slug):
    category = Category.objects.all()
    room_category = Category.objects.filter(slug=slug).first()
    rooms = Room.objects.all()
    rooms = Room.objects.filter(category=room_category) if room_category else rooms

    return render(  
        request, "room_list.html", {"rooms": rooms, "category": category}
    )



@login_required(login_url="users/sign_in")
def room_detail(request, slug):
    room = get_object_or_404(Room, slug=slug)
    form = AvailabilityForm(request.POST)
    # form = forms.ReviewForm(request.POST or None)
    booked = room.booking_set.filter(user=request.user)
    is_success = False

    if request.method == "POST" and form.is_valid():
        instance = form.save(commit=False)
        is_success = True
        instance.room = room
        instance.user = request.user    
        room.status = False 
        room.save()
        instance.save()
        form.save()
        form = AvailabilityForm
    return render(
        request,
        "room_detail_view.html",
        {
            "room": room,
            "form": form,
            "booked": booked,
            "is_success": is_success,
        },
    )
