from flask import Flask,request, jsonify

app = Flask(__name__)

class Doctor:
    def __init__(self, id, name, specialty, schedule):
        self.id = id
        self.name = name
        self.specialty = specialty
        self.schedule = schedule

class Appointment:
    def __init__(self, id, doctor_id, patient_name, time):
        self.id = id
        self.doctor_id = doctor_id
        self.patient_name = patient_name
        self.time = time


doctors = [
    Doctor(1, "Dr. Smith", "Cardiologist", ["Monday", "Wednesday"]),
    Doctor(2, "Dr. Johnson", "Dermatologist", ["Tuesday", "Thursday"]),
]

appointments = [
    Appointment(1, 1, "John Doe", "2023-10-15 14:00:00"),
    Appointment(2, 2, "Jane Smith", "2023-10-16 10:30:00"),
] 

@app.route('/doctors')
def get_doctors():
    # Retrieve and return a list of doctors
    return jsonify([doctor.__dict__ for doctor in doctors])

@app.route('/doctors/<int:doctor_id>')
def get_doctor(doctor_id):
    # Retrieve and return details of a specific doctor
    doctor = next((d for d in doctors if d.id == doctor_id), None)
    if doctor:
        return jsonify(doctor.__dict__)
    else:
        return jsonify({'error': 'Doctor not found'}),
@app.route('/appointments', methods=['POST'])
def book_appointment():
    # Parse request data and create a new appointment
    data = request.json
    appointment = Appointment(
        len(appointments) + 1,
        data['doctor_id'],
        data['patient_name'],
        data['time']
    )
    appointments.append(appointment)
    return jsonify({'message': 'Appointment booked successfully'})

if __name__ == '__main__':
    app.run(port=4700)