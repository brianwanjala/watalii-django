from django.shortcuts import render, get_object_or_404, redirect
from .models import TourPackage, Booking, ContactMessage
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def list(request):
    packages = TourPackage.objects.all()
    return render(request, 'tours/tour_lists.html', {'packages': packages})

def details(request, pk):
    package = get_object_or_404(TourPackage, pk=pk)

    return render(request, 'tours/details.html', {'package': package})

def book_tour(request, pk):
    package = get_object_or_404(TourPackage, pk=pk)
    
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        number_of_people = request.POST.get("number_of_people")
        message = request.POST.get("message")

        booking = Booking.objects.create(
            package=package,
            full_name=full_name,
            email=email,
            phone=phone,
            number_of_people=number_of_people,
            message=message
        )

        # Send booking confirmation email
        send_mail(
            subject="Watalii Booking Received",
            message=f"""
Hello {booking.full_name},

Your booking for {package.title} has been received successfully.

Number of people: {booking.number_of_people}
Phone: {booking.phone}

We will contact you soon to confirm your booking.

Thank you,
Watalii Tours
            """,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[booking.email],
            fail_silently=True,
        )

        return render(request, 'tours/booking_success.html', {'package': package})

    return render(request, 'tours/booking_form.html', {'package': package})


def contact(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            full_name = full_name,
            email = email,
            subject = subject,
            message = message
        )

        return redirect('contact')
    return render(request, "pages/contact.html")
