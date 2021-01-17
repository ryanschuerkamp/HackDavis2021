wings = {'EW':'East Wing','SW': 'South Wing', 'WW': 'West Wing', 'NW':'North Wing'}



class Patient:
    def __init__(self,name,age,stay,condition):
        self.name = name
        self.age = age
        # stay will be how many days patient stays at hospital
        self.stay = stay
        # will make different locations of the hospital
        self.location = 'Not placed yet'
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
        self.wing = wings[wing]
        self.patients = []
        self.occupancy = False
        self.bedding = False
    def add_patient(self,patient):
        self.patients.append(patient)
        patient.location = self.wing +','+ f'Room {self.number}'
        self.occupancy = True
        

    def __len__(self):
        return len(self.patients)
    def __str__(self):
        return f'Room {self.number} on {self.wing} ' +'\n'+f'patient: {str(self.patients[0])}'
        
   
# the hospital will contain all the rooms and inturn all the patients
# let's say we want a hospital with 50 rooms on each wing for 200 room total
class Hospital:
    def __init__(self):
        self.rooms = []
        for x in range(50):
            for y in wings:
                self.rooms.append(Room(x,y))
    def __len__(self):
        return len(self.rooms)
    
# create patient classes from csv of database
sep = ','
with open('patients.csv','r') as f:
    f.readline()
    patient_list = []
    for x in f:
        x = x.strip().split(sep)
        name = x[0]
        age = int(x[1])
        stay = int(x[2])
        condition = x[3]
        patient_list.append(Patient(name,age,stay,condition))

# using this batch of patients we add them to the hospital rooms. for simplicity i added them to fill the rooms in order
i = 0
for x in patient_list:
    my_hospital.rooms[i].add_patient(x)
    i += 1
    
   
        
