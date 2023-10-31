class Hobby:
    def __init__(self, name, description, related_equipment):
        self.name = name
        self.description = description
        self.related_equipment = related_equipment
        self.citizens = []  # List of citizens interested in this hobby

class Event:
    def __init__(self, name, date, location):
        self.name = name
        self.date = date
        self.location = location
        self.participants = []  # List of citizens attending the event

class FinnishCitizen:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        self.hobbies = []  # List of hobbies
        self.events_attending = []  # List of events to attend
        self.social_connections = []  # List of other FinnishCitizen objects

    def add_hobby(self, hobby):
        self.hobbies.append(hobby)
        hobby.citizens.append(self)

    def remove_hobby(self, hobby):
        self.hobbies.remove(hobby)
        hobby.citizens.remove(self)

    def add_event(self, event):
        self.events_attending.append(event)
        event.participants.append(self)

    def remove_event(self, event):
        self.events_attending.remove(event)
        event.participants.remove(self)

    def add_social_connection(self, citizen):
        self.social_connections.append(citizen)

    def remove_social_connection(self, citizen):
        self.social_connections.remove(citizen)

# Sample Usage
if __name__ == "__main__":
    # Create hobbies
    skiing = Hobby("Skiing", "Enjoy the Finnish winters on skis", "Ski equipment")
    fishing = Hobby("Ice Fishing", "Catch fish through a hole in the ice", "Fishing rod")
    berry_picking = Hobby("Berry Picking", "Harvest wild berries in the Finnish forests", "Basket")

    # Create events
    event1 = Event("Winter Sports Festival", "2023-02-15", "Rovaniemi")
    event2 = Event("Summer Picnic", "2023-06-20", "Helsinki")

    # Create Finnish citizens
    citizen1 = FinnishCitizen("Alice", 28, "Helsinki")
    citizen2 = FinnishCitizen("Bob", 35, "Tampere")

    # Associate citizens with hobbies and events
    citizen1.add_hobby(skiing)
    citizen1.add_event(event1)

    citizen2.add_hobby(fishing)
    citizen2.add_hobby(berry_picking)
    citizen2.add_event(event2)

    # Add social connections
    citizen1.add_social_connection(citizen2)

    # Display information
    print("Citizen 1 Hobbies:", [hobby.name for hobby in citizen1.hobbies])
    print("Citizen 2 Events:", [event.name for event in citizen2.events_attending])
    print("Citizen 1 Social Connections:", [connection.name for connection in citizen1.social_connections])
