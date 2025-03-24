class MedicalRecord:
    def __init__(self, record_id, diagnose, treatment):
        self.record_id = record_id
        self.diagnose = diagnose
        self.treatment = treatment

class Patient:
    def __init__(self, patient_id, patient_name):
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.medical_records = []  # List to store patient's medical records
        self.assigned_doctor = None  # Doctor assigned to the patient
        self.assigned_department = None  # Department where the patient is treated

    def add_medical_record(self, record):
        """Adds a medical record to the patient"""
        self.medical_records.append(record)

    def assign_doctor(self, doctor):
        """Assigns a doctor to the patient"""
        self.assigned_doctor = doctor

    def assign_department(self, department):
        """Assigns a department to the patient"""
        self.assigned_department = department

    def get_details(self):
        """Displays patient, doctor, and department information"""
        doctor_name = self.assigned_doctor.doctor_name if self.assigned_doctor else "Not Assigned"
        department_name = self.assigned_department.department_name if self.assigned_department else "Not Assigned"

        print(f"Patient: {self.patient_name}")
        print(f"Doctor: {doctor_name}")
        print(f"Department: {department_name}")
        print("Medical Records:")
        for record in self.medical_records:
            print(f"  - Record ID: {record.record_id}, Diagnose: {record.diagnose}, Treatment: {record.treatment}")
        print("\n")

class Doctor:
    def __init__(self, doctor_id, doctor_name, doctor_speciality):
        self.doctor_id = doctor_id
        self.doctor_name = doctor_name
        self.doctor_speciality = doctor_speciality
        self.patients = []  # List of patients handled by the doctor

    def add_patient(self, patient):
        """Adds a patient to the doctor's patient list"""
        self.patients.append(patient)
        patient.assign_doctor(self)  # Connects the patient with the doctor

    def list_patients(self):
        """Displays the doctor's patient list"""
        print(f"{self.doctor_name} handles patients:")
        for patient in self.patients:
            print(f"  - {patient.patient_name}")
        print("\n")

class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.doctors = []  # List of doctors in the department

    def add_doctor(self, doctor):
        """Adds a doctor to the department"""
        self.doctors.append(doctor)

class Hospital:
    def __init__(self, hospital_name):
        self.hospital_name = hospital_name
        self.departments = []  # List of departments in the hospital

    def add_department(self, department):
        """Adds a department to the hospital"""
        self.departments.append(department)

# ======= Example Usage =======

# Create Departments
dept_cardiology = Department("Cardiology")
dept_neurology = Department("Neurology")

# Create Doctors
doctor1 = Doctor(101, "Dr. A", "Cardiology")
doctor2 = Doctor(102, "Dr. B", "Neurology")

# Add doctors to departments
dept_cardiology.add_doctor(doctor1)
dept_neurology.add_doctor(doctor2)

# Create Patients
patient1 = Patient(1, "John Doe")
patient2 = Patient(2, "Jane Doe")

# Create Medical Records
record1 = MedicalRecord(201, "Heart Attack", "Bypass Surgery")
record2 = MedicalRecord(202, "Migraine", "Pain Reliever Medication")

# Add medical records to patients
patient1.add_medical_record(record1)
patient2.add_medical_record(record2)

# Assign patients to doctors and departments
doctor1.add_patient(patient1)
doctor2.add_patient(patient2)

patient1.assign_department(dept_cardiology)
patient2.assign_department(dept_neurology)

# View patient details
patient1.get_details()
patient2.get_details()

# View doctor's patient list
doctor1.list_patients()
doctor2.list_patients()