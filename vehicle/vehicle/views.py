from django.shortcuts import get_object_or_404, render,redirect

from .models import Payment, Rental, Vehicle
from django.utils import timezone
# Create your views here.
def home(request):
    return render(request,'home.html')

def process_payment(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)

    if request.method == 'POST':
        # Handle the payment logic (mock for now)
        # In a real-world app, integrate a payment gateway like Stripe or PayPal

        # Create a rental record
        rental = Rental.objects.create(
            customer=request.user,  # Assuming you have authentication enabled
            vehicle=vehicle,
            rental_date=timezone.now(),
        )

        # Mock payment
        Payment.objects.create(
            rental=rental,
            amount=vehicle.daily_rental_rate,
            payment_method="Credit Card",  # For example, mock this
        )

        return redirect('rental_summary', rental_id=rental.id)

    return render(request, 'process_payment.html', {'vehicle': vehicle})

def rental_summary(request, rental_id):
    # Fetch the rental by its ID
    rental = get_object_or_404(Rental, id=rental_id)

    # Pass the rental object to the template
    return render(request, 'rental_summary.html', {'rental': rental})

def rentals(request):
    # Get all rentals for the logged-in user
    user_rentals = Rental.objects.filter(customer=request.user)

    # Pass the user's rentals to the template
    return render(request, 'rentals.html', {'rentals': user_rentals})

from .models import Vehicle  # Import your Vehicle model

def book_vehicle(request):
    vehicles = Vehicle.objects.all()  # Fetch all vehicles from the database
    return render(request, 'book_vehicle.html', {'vehicles': vehicles})  # Pass vehicles to the template