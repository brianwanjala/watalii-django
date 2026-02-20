from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from tours.models import Booking
from django.contrib.admin.views.decorators import staff_member_required

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()

    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)   
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("home")

@login_required
def dashboard(request):
    bookings = Booking.objects.filter(user=request.user).order_by('booked_at')

    return render(request, "accounts/dashboard.html", {"bookings": bookings})



@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if booking.status=="Pending":
        booking.status = "Cancelled"
        booking.save()
        messages.success(request, "Booking cancelled successfully.")

    else:
        messages.error(request, "you cannot cancel this tour at the moment")

    return redirect("dashboard")


@staff_member_required
def admin_dashboard(request):
    bookings = Booking.objects.all().order_by("-booked_at")

    pending_count = Booking.objects.filter(status="pending").count()
    approved_count = Booking.objects.filter(status="approved").count()
    cancelled_count = Booking.objects.filter(status="cancelled").count()

    context = {
        "bookings": bookings,
        "pending_count": pending_count,
        "approved_count": approved_count,
        "cancelled_count": cancelled_count,
    }

    return render(request, "admindashboard1/admindashboard.html", context)

@staff_member_required
def approve_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.status = "approved"
    booking.save()
    return redirect("admin_dashboard")


@staff_member_required
def cancel_booking_admin(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.status = "cancelled"
    booking.save()
    return redirect("admin_dashboard")