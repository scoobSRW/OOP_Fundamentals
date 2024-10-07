class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0

    def add_participant(self):
        self.participant_count += 1
        print(f"Participant added. Current count: {self.participant_count}")

    def get_participant_count(self):
        return self.participant_count

event = Event("City Marathon", "2024-10-15")

event.add_participant()
event.add_participant()

current_count = event.get_participant_count()
print(f"Total participants in {event.name}: {current_count}")
