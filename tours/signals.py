from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Booking

@receiver(post_save, sender=Booking)
def booking_status_email(sender, instance, created, **kwargs):
    if not created:
        if instance.status == "approved":
            send_mail(
                subject="Watalii Booking Approved",
                message=f"""
Hello {instance.full_name},

Great news! Your booking for {instance.package.title} has been APPROVED.

We will contact you soon with the final travel details.

Thank you for choosing Watalii Tours.
                """,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[instance.email],
                fail_silently=True
            )

        elif instance.status == "cancelled":
            send_mail(
                subject="Watalii Booking Cancelled",
                message=f"""
Hello {instance.full_name},

Unfortunately, your booking for {instance.package.title} has been CANCELLED.

If you need help booking another tour, please contact us.

Watalii Tours
                """,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[instance.email],
                fail_silently=True
            )
