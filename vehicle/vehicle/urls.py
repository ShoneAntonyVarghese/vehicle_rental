from django.urls import path,include

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    
     path('book_vehicle/', views.book_vehicle, name='book_vehicle'),

     path('process-payment/<int:vehicle_id>/', views.process_payment, name='process_payment'),

      path('rental-summary/<int:rental_id>/', views.rental_summary, name='rental_summary'),

    path('rentals/', views.rentals, name='rentals'),
]


