from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout_view'),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("cancel-booking/<int:booking_id>/", views.cancel_booking, name="cancel_booking"),
    path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("approve-booking/<int:booking_id>/", views.approve_booking, name="approve_booking"),
    path("cancel-booking-admin/<int:booking_id>/", views.cancel_booking_admin, name="cancel_booking_admin"),


    ]