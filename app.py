from datetime import datetime
from enum import Enum
from collections import defaultdict
from flask import Flask, jsonify

# Definiciones de clases
class TripState(Enum):
    PENDING = "Pendiente"
    ON_TRIP = "En viaje"
    DELIVERED = "Entregado"

class DayOfWeek(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

class Purchase:
    def __init__(self, customer_name, items, purchase_date):
        self.customer_name = customer_name
        self.items = items
        self.purchase_date = purchase_date

    def get_total_price(self):
        return sum(item.price for item in self.items)

    def get_total_weight(self):
        return sum(item.weight for item in self.items)

class Trip:
    def __init__(self, departure, state=TripState.PENDING):
        self.departure = departure
        self.state = state
        self.zip_codes = []

    def add_zip_code(self, zip_code):
        if len(self.zip_codes) < 3:
            self.zip_codes.append(zip_code)
            return True
        else:
            return False

    def total_weight(self):
        return sum(self.weight for self in self.items)

class Address:
    def __init__(self, address, city, zip_code):
        self.address = address
        self.city = city
        self.zip_code = zip_code

class Truck:
    def __init__(self, plate_number, max_weight_capacity, work_days):
        self.plate_number = plate_number
        self.max_weight_capacity = max_weight_capacity
        self.work_days = work_days
        self.state = TruckState.PENDING

class TruckState(Enum):
    PENDING = "Pendiente"
    ON_TRIP = "En viaje"
    DELIVERED = "Entregado"

# Funciones para planificar viajes y asignar camiones

def plan_trips(planning_date):
    trips = []
    # Lógica para armar los viajes
    # Supongamos que tenemos una lista de compras (purchases) para el día de planificación
    purchases = [
        Purchase("Cliente1", [Item("Producto1", 10, 1)], datetime(2024, 3, 1)),
        Purchase("Cliente2", [Item("Producto2", 20, 2)], datetime(2024, 3, 1)),
        Purchase("Cliente3", [Item("Producto3", 30, 3)], datetime(2024, 3, 1))
    ]
    
    zip_codes = defaultdict(list)
    for purchase in purchases:
        for item in purchase.items:
            zip_codes[purchase.purchase_date].append(item.included_in.zip_code)
    
    for purchase_date, codes in zip_codes.items():
        trip = Trip(purchase_date)
        for code in codes:
            if not trip.add_zip_code(code):
                trips.append(trip)
                trip = Trip(purchase_date)
                trip.add_zip_code(code)
        trips.append(trip)
    
    return trips

def assign_trucks(planning_date, trips):
    assignments = {}
    # Lógica para asignar camiones
    # Supongamos que tenemos una lista de camiones disponibles (trucks) para el día de planificación
    trucks = [
        Truck("123", 1000, [DayOfWeek.MONDAY, DayOfWeek.TUESDAY]),
        Truck("456", 1500, [DayOfWeek.MONDAY, DayOfWeek.WEDNESDAY])
    ]

    for trip in trips:
        suitable_trucks = [truck for truck in trucks if planning_date.weekday() in truck.work_days and truck.max_weight_capacity >= trip.total_weight()]
        if suitable_trucks:
            assignments[trip] = suitable_trucks[0].plate_number
            trip.state = TripState.ON_TRIP
        else:
            assignments[trip] = None
    
    return assignments

app = Flask(__name__)

@app.route('/api/purchases')
def get_purchases():
    # Lógica para obtener las compras de la base de datos
    purchases = [
        {"customer_name": "Cliente1", "items": [{"name": "Producto1", "price": 10, "weight": 1}], "purchase_date": "2024-03-01"},
        {"customer_name": "Cliente2", "items": [{"name": "Producto2", "price": 20, "weight": 2}], "purchase_date": "2024-03-01"},
        {"customer_name": "Cliente3", "items": [{"name": "Producto3", "price": 30, "weight": 3}], "purchase_date": "2024-03-01"}
    ]
    return jsonify(purchases)

@app.route('/api/trips')
def get_trips():
    # Lógica para obtener los viajes de la base de datos