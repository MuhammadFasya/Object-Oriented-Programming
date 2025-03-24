class MedicalRecord:
    def __init__(self, patient_id, patient_name, patient_diagnose, patient_treatment):
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.patient_diagnose = patient_diagnose
        self.patient_treatment = patient_treatment

class Patient:
    def __init__(self, medical_record):
        self.medical_record = medical_record

class Doctor:
    def __init__(self, doctor_id, doctor_name, doctor_speciality):
        self.doctor_id = doctor_id
        self.doctor_name = doctor_name
        self.doctor_speciality = doctor_speciality
        self.patients = []  # List for saving patient (Aggregation)

    def add_patient(self, patient):
        self.patients.append(patient)

class Department:
    def __init__(self, name):
        self.name = name
        self.doctors = []  # List for saving doctor (Composition)

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

class Hospital:
    def __init__(self, name):
        self.name = name
        self.departments = []  # List for saving departemen (Composition)
        self.doctors = []  # List for all dokter
        self.patients = []  # List for all pasien

    def add_department(self, department):
        self.departments.append(department)

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def add_patient(self, patient):
        self.patients.append(patient)

    def show_departments(self):
        print(f"Departments in {self.name}:")
        for dept in self.departments:
            print(f"- {dept.name}")

    def show_doctors(self):
        print(f"Doctors in {self.name}:")
        for doc in self.doctors:
            print(f"- {doc.doctor_name} ({doc.doctor_speciality})")

    def show_patients(self):
        print(f"Patients in {self.name}:")
        for pat in self.patients:
            print(f"- {pat.medical_record.patient_name}")
# Hospital
hospital = Hospital("Nusa Putra Hospital")

# Department
dept_surgery = Department("Surgery")
dept_cardiology = Department("Cardiology")

# Adding department to hospital
hospital.add_department(dept_surgery)
hospital.add_department(dept_cardiology)

# Make a doctor list
doctor1 = Doctor(1, "Dr. Alice", "Surgeon")
doctor2 = Doctor(2, "Dr. Bob", "Cardiologist")

# Adding doctor to department
dept_surgery.add_doctor(doctor1)
dept_cardiology.add_doctor(doctor2)

# Adding doctor to hospital
hospital.add_doctor(doctor1)
hospital.add_doctor(doctor2)

# Make a patient
record1 = MedicalRecord(101, "John Doe", "Fracture", "Surgery")
patient1 = Patient(record1)

# Adding patient to doctor
doctor1.add_patient(patient1)

# Adding patient to hospital
hospital.add_patient(patient1)

# Show all departments, doctors, and patients
hospital.show_departments()
hospital.show_doctors()
hospital.show_patients()
