document.addEventListener('DOMContentLoaded', function () {
    fetchResults();
});

function fetchResults() {
    // Aquí puedes realizar una solicitud fetch a tu backend para obtener los resultados
    // Por simplicidad, simularemos los resultados aquí
    const trips = [
        { trip: "trip 1", zipCodes: [11000, 11001, 11003] },
        { trip: "trip 2", zipCodes: [10012, 12023] },
        { trip: "trip 3", zipCodes: [10014, 12022, 12030] }
    ];
    const assignments = [
        { trip: "trip 1", truckPlate: "23" },
        { trip: "trip 2", truckPlate: "12" },
        { trip: "trip 3", error: "No trucks meet requirements" }
    ];

    displayTrips(trips);
    displayAssignments(assignments);
}

function displayTrips(trips) {
    const tripsList = document.getElementById('trips');
    tripsList.innerHTML = '';
    trips.forEach(trip => {
        const li = document.createElement('li');
        li.textContent = `${trip.trip} → zip code: ${trip.zipCodes.join(', ')}`;
        tripsList.appendChild(li);
    });
}

function displayAssignments(assignments) {
    const assignmentsList = document.getElementById('assignments');
    assignmentsList.innerHTML = '';
    assignments.forEach(assignment => {
        const li = document.createElement('li');
        if (assignment.error) {
            li.textContent = `${assignment.trip} → ${assignment.error}`;
        } else {
            li.textContent = `${assignment.trip} → Truck plate ${assignment.truckPlate}`;
        }
        assignmentsList.appendChild(li);
    });
}
