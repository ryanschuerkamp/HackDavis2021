class Patient:
    def __init__(self,name,age,stay,location,condition):
        self.name = name
        self.age = age
        # stay will be how many days patient stays at hospital
        self.stay = stay
        # will make different locations of the hospital
        self.location = location
        # the type of illnesses
        self.condition = condition
        
        self.available = True
        # if the patient has a certain disease a method will change their eligibility for visits 
        self.visits = True
        
    
    def __str__(self):
        return f'{self.name} has a stay of {self.stay} days'
    def __len__(self):
        return self.stay
 
class Room:
    # room will either be empty or full
    # a room will have a location and  other stuff like beds,furniture.
    # for simplicity we will make one room have only one patient
    def __init__(self,number, wing):
        self.number = number
        self.wing = locations[wing]
        self.patients = []
        self.occupancy = False
    def add_patient(self,patient):
        self.patients.append(patient)
        self.occupancy = True
    def __len__(self):
        return len(self.patients)
    def __str__(self):
        return f'Room {self.number} on {self.wing} ' +'\n'+f'patient: {str(self.patients[0])}'
        
