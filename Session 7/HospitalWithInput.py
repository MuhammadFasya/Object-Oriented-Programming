class MedicalRecord:
    def __init__(self, record_id, diagnosis, treatment):
        self.record_id = record_id
        self.diagnosis = diagnosis
        self.treatment = treatment

class Patient:
    def __init__(self, patient_id, patient_name):
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.medical_records = []
        self.assigned_doctor = None
        self.assigned_department = None

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
        """Displays patient information"""
        doctor_name = self.assigned_doctor.doctor_name if self.assigned_doctor else "Not Assigned"
        department_name = self.assigned_department.department_name if self.assigned_department else "Not Assigned"

        print("\n--- Patient Information ---")
        print(f"Patient: {self.patient_name}")
        print(f"Doctor: {doctor_name}")
        print(f"Department: {department_name}")
        print("Medical Records:")
        for record in self.medical_records:
            print(f"  - ID: {record.record_id}, Diagnosis: {record.diagnosis}, Treatment: {record.treatment}")
        print("\n")

class Doctor:
    def __init__(self, doctor_id, doctor_name, doctor_speciality):
        self.doctor_id = doctor_id
        self.doctor_name = doctor_name
        self.doctor_speciality = doctor_speciality
        self.patients = []

    def add_patient(self, patient):
        """Adds a patient to the doctor's list"""
        self.patients.append(patient)
        patient.assign_doctor(self)

    def diagnose_patient(self, record_id, diagnosis):
        """Determines treatment based on diagnosis"""
        treatment = self.determine_treatment(diagnosis)
        return MedicalRecord(record_id, diagnosis, treatment)

    def determine_treatment(self, diagnosis):
        """Simple rule-based system for determining treatment"""
        treatment_rules = {
            "Flu": "Paracetamol & Rest",
            "Heart Attack": "Bypass Surgery",
            "Diabetes": "Healthy Diet & Insulin",
            "Migraine": "Painkillers & Relaxation",
            "Hypertension": "Exercise & Blood Pressure Medication"
        }
        return treatment_rules.get(diagnosis, "Further Consultation Required")

class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.doctors = []

    def add_doctor(self, doctor):
        """Adds a doctor to the department"""
        self.doctors.append(doctor)

class Hospital:
    def __init__(self, hospital_name):
        self.hospital_name = hospital_name
        self.departments = []

    def add_department(self, department):
        """Adds a department to the hospital"""
        self.departments.append(department)

    def find_doctor_by_id(self, doctor_id):
        """Finds a doctor by ID"""
        for department in self.departments:
            for doctor in department.doctors:
                if doctor.doctor_id == doctor_id:
                    return doctor
        return None  

    def list_departments(self):
        """Displays available departments"""
        print("\n--- List of Departments ---")
        for i, department in enumerate(self.departments, start=1):
            print(f"{i}. {department.department_name}")
        print("\n")

    def list_doctors(self):
        """Displays available doctors"""
        print("\n--- List of Doctors ---")
        for department in self.departments:
            for doctor in department.doctors:
                print(f"ID: {doctor.doctor_id} | Name: {doctor.doctor_name} | Specialization: {doctor.doctor_speciality}")
        print("\n")

# ======= Hospital Setup =======
hospital = Hospital("Healthy Life Hospital")

# Create Departments
dept_cardiology = Department("Cardiology")
dept_neurology = Department("Neurology")

# Create Doctors
doctor1 = Doctor(101, "Dr. A", "Cardiology")
doctor2 = Doctor(102, "Dr. B", "Neurology")

# Add doctors to departments
dept_cardiology.add_doctor(doctor1)
dept_neurology.add_doctor(doctor2)

# Add departments to hospital
hospital.add_department(dept_cardiology)
hospital.add_department(dept_neurology)

# ======= Patient Input Feature =======
print("\n*** Welcome to the Healthy Life Hospital System ***\n")

# Input patient data
patient_id = int(input("Enter Patient ID: "))
patient_name = input("Enter Patient Name: ")
patient = Patient(patient_id, patient_name)

# Display available doctors
hospital.list_doctors()
doctor_id = int(input("Select Doctor ID: "))
chosen_doctor = hospital.find_doctor_by_id(doctor_id)

if chosen_doctor:
    chosen_doctor.add_patient(patient)
    print(f"Patient {patient_name} has been assigned to {chosen_doctor.doctor_name}.")
else:
    print("Doctor not found!")

# Display available departments
hospital.list_departments()
dept_choice = int(input("Select Department Number: "))

if 1 <= dept_choice <= len(hospital.departments):
    chosen_department = hospital.departments[dept_choice - 1]
    patient.assign_department(chosen_department)
    print(f"Patient {patient_name} has been assigned to the {chosen_department.department_name} department.")
else:
    print("Invalid department!")

# Input patient diagnosis
record_id = int(input("Enter Medical Record ID: "))
diagnosis = input("Enter Diagnosis: ")

# Doctor determines treatment based on diagnosis
record = chosen_doctor.diagnose_patient(record_id, diagnosis)
patient.add_medical_record(record)

# Display final patient details
patient.get_details()
