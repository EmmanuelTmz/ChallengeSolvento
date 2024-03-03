document.addEventListener("DOMContentLoaded", function() {
    fetchPurchases();
    fetchTrips();
    fetchTrucks();
});

function fetchPurchases() {
    fetch('/api/purchases')
    .then(response => response.json())
    .then(data => {
        const purchasesDiv = document.getElementById('purchases');
        purchasesDiv.innerHTML = '<h2>Purchases</h2>';
        data.forEach(purchase => {
            purchasesDiv.innerHTML += `<div class="purchase">
                                            <h3>${purchase.customer_name}</h3>
                                            <p>Date: ${purchase.purchase_date}</p>
                                            <ul>
                                                ${purchase.items.map(item => `<li>${item.name} - Price: ${item.price} - Weight: ${item.weight}</li>`).join('')}
                                            </ul>
                                        </div>`;
        });
    });
}

function fetchTrips() {
    fetch('/api/trips')
    .then(response => response.json())
    .then(data => {
        const tripsDiv = document.getElementById('trips');
        tripsDiv.innerHTML = '<h2>Trips</h2>';
        data.forEach(trip => {
            tripsDiv.innerHTML += `<div class="trip">
                                        <h3>Departure: ${trip.departure}</h3>
                                        <p>Status: ${trip.state}</p>
                                        <p>Zip Codes: ${trip.zip_codes.join(', ')}</p>
                                    </div>`;
        });
    });
}

function fetchTrucks() {
    fetch('/api/trucks')
    .then(response => response.json())
    .then(data => {
        const trucksDiv = document.getElementById('trucks');
        trucksDiv.innerHTML = '<h2>Trucks</h2>';
        data.forEach(truck => {
            trucksDiv.innerHTML += `<div class="truck">
                                        <h3>Plate Number: ${truck.plate_number}</h3>
                                        <p>Max Weight Capacity: ${truck.max_weight_capacity}</p>
                                        <p>Work Days: ${truck.work_days.join(', ')}</p>
                                    </div>`;
        });
    });
}
