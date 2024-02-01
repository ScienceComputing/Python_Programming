import csv

def read_patient_library():
    with open('patient_library.csv', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            print("Patient ID:", row[0])
            print("Name:", row[1])
            print("Age:", row[2])
            print("Diagnosis:", row[3])
            print()

def add_patient():
    patient_id = input("Enter Patient ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    diagnosis = input("Enter Diagnosis: ")

    with open('patient_library.csv', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == patient_id:
                print("This patient already exists in the library.")
                return

    with open('patient_library.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([patient_id, name, age, diagnosis])
    print("Patient added successfully.")

def search_patient():
    patient_id = input("Enter Patient ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    diagnosis = input("Enter Diagnosis: ")

    with open('patient_library.csv', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row == [patient_id, name, age, diagnosis]:
                return True
    return False

# Main menu
while True:
    print("Patient Data Library Management")
    print("1. Read Library")
    print("2. Add Patient")
    print("3. Search Patient")
    print("4. Exit")
    
    choice = input("Select an option: ")

    if choice == '1':
        read_patient_library()
    elif choice == '2':
        add_patient()
    elif choice == '3':
        if search_patient():
            print("Patient found in the library.")
        else:
            print("Patient not found in the library.")
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
