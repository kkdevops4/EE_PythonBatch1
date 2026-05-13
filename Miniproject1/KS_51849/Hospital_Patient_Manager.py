
triage_dict = {
    "Level_1": ["heart attack","brain stroke","severe trauma","respiratory failure"],
    "Level_2": ["chest pain","stroke symptoms","pneumonia","altered mental status","ketoacidosis"],
    "Level_3": ["asthma attack","appendicitis","high fever","fractures","migraine"],
    "Level_4": ["minor fracture","sprain","skin infection","vomiting","diarrhea","urinary tract infection"],
    "Level_5": ["cold","minor cut","hypertension","prescription refills"],
}

patients = []

doctors = ["Dr.Chadda", "Dr.Gupta", "Dr.Sharma"]
doc_index = 0


def get_triage(age, symptom):
    symptom = symptom.lower()

    for level in triage_dict:
        if symptom in triage_dict[level]:
            return level

    if age > 60:
        return "Level_2"
    elif age < 10:
        return "Level_3"
    else:
        return "Level_5"


name = input("Enter name: ")
age = int(input("Enter age: "))
symptom = input("Enter symptom: ")

triage = get_triage(age, symptom)

doctor = doctors[len(patients) % len(doctors)]

patient = {
    "name": name,
    "age": age,
    "symptom": symptom,
    "triage": triage,
    "doctor": doctor
}

patients.append(patient)

print("\nPatient Added")
print("Name:", name)
print("Triage Level:", triage)
print("Assigned Doctor:", doctor)