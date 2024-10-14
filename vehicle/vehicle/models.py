from django.db import models

# Create your models here.
from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    driver_license_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Vehicle(models.Model):
    make = models.CharField(max_length=50)  # e.g., Toyota, Ford
    model = models.CharField(max_length=50)  # e.g., Camry, Focus
    year = models.IntegerField()
    vin_number = models.CharField(max_length=17, unique=True)  # Vehicle Identification Number
    license_plate_number = models.CharField(max_length=15, unique=True)
    color = models.CharField(max_length=30, blank=True, null=True)
    mileage = models.IntegerField(default=0)
    daily_rental_rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.year} {self.make} {self.model}'


class Rental(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # Link to Customer
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)  # Link to Vehicle
    rental_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(blank=True, null=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f'Rental {self.id} - {self.customer} - {self.vehicle}'


class Payment(models.Model):
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)  # Link to Rental
    payment_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)  # e.g., Credit Card, Cash

    def __str__(self):
        return f'Payment {self.id} - {self.rental}'


class Maintenance(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)  # Link to Vehicle
    description = models.TextField()
    maintenance_date = models.DateField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    performed_by = models.CharField(max_length=100)  # Mechanic or service company

    def __str__(self):
        return f'Maintenance {self.id} - {self.vehicle}'
