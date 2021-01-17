pip install pony
db = Database()

wings = {'EW':'East Wing','SW': 'South Wing', 'WW': 'West Wing', 'NW':'North Wing'}
# create a Patient entity
class Patient(db.Entity):
    name = Required(str)
    age = Required(int)
    stay = Required(int)
    location = Optional('Room')
    condition = Required(str)
    visits = Required(bool)
        

# create a room Entity
class Room(db.Entity):
    number = Required(int)
    wing = Required(str)
    patients = Set(Patient)
    building = Optional('Hospital')
    

class Hospital(db.Entity):
    rooms = Set(Room)
    

db.bind(provider='sqlite', filename=':memory:')

db.generate_mapping(create_tables=True)

Functions:
with db_session:
  #create a Hospital with 40 rooms
    River_Hospital = Hospital()
    for x in range(10):
        for y in wings:
            created_room = Room(number=x, wing = y)
            River_Hospital.rooms.add(created_room)
   # create patients and assign to each room
    i = 0
    for x in patient_list:
        x.location = list(River_Hospital.rooms)[i]
        i+= 1
     
        


  
