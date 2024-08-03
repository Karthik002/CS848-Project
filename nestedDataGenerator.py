import uuid
import firebase_admin
from firebase_admin import db
import random
from datetime import datetime, timedelta

def createFirebaseApp():
    if not firebase_admin._apps:
        creds = firebase_admin.credentials.Certificate('nestedDBServiceAccountKey.json')
        default_app = firebase_admin.initialize_app(creds, {
            'databaseURL': 'https://cs848-project-nested-db-default-rtdb.firebaseio.com'
        })

def addData(user):
    createFirebaseApp()
    sessionRef = db.reference("group1/users/" + user + "/sessions")
    data = createJSONData(datetime(2023, 7, 11), datetime(2024, 6, 29))
    sessionRef.set(data)

def createJSONData(startDate, endDate):
    activities_list = [
        "Cafe", "Cafe2", "Cafe3", "ChattingWithAFriend", "ChattingWithANeighbor", 
        "ClassroomActivity", "CrossTheStreet", "CrowdedClassroom", "CrowdedClassroom2", 
        "DentalOffice", "DriveThru", "EmotionalRegulationExam", "GivingDirections", 
        "GroceryStore", "GroceryStore2", "GuestsAreComing", "InitiatingAConversation", 
        "InitiatingAConversation2", "MechanicShop", "NavigatingABusRoute", "OrderABurger", 
        "OrderACombo", "Pharmacy", "Prosody", "Prosody2", "QuietLibrary", "QuietLibrary2", 
        "SchoolSchedule", "SchoolSchedule2", "StrangerDanger", "StrangerDanger2", 
        "TalkWithAFriend", "TeamChanges", "ToyTakenAway", "UnderstandingIntentions", 
        "WhatsInTheBox"
    ]

    sessions = {}
    current_date = startDate

    while current_date < endDate:
        start_time = current_date + timedelta(hours=random.randint(0, 23), minutes=random.randint(0, 59))
        session_duration = timedelta(hours=random.randint(1, 3), minutes=random.randint(0, 59))
        end_time = start_time + session_duration

        num_activities = random.randint(1, 4)
        selected_activities = random.sample(activities_list, k=num_activities)

        activity_duration = session_duration / num_activities
        activity_start_time = start_time
        activities = []

        for activity in selected_activities:
            activity_end_time = activity_start_time + activity_duration
            states = []
            state_start_time = activity_start_time

            while state_start_time < activity_end_time:
                state_duration = timedelta(seconds=random.randint(2, 30))
                state_end_time = min(state_start_time + state_duration, activity_end_time)
                states.append({
                    'state_id': str(uuid.uuid4()),
                    'start_time': state_start_time.strftime('%Y-%m-%d %H:%M:%S'),
                    'end_time': state_end_time.strftime('%Y-%m-%d %H:%M:%S')
                })
                state_start_time = state_end_time

            activities.append({
                'name': activity,
                'start_time': activity_start_time.strftime('%Y-%m-%d %H:%M:%S'),
                'end_time': activity_end_time.strftime('%Y-%m-%d %H:%M:%S'),
                'states': states,
                'score': str(random.randint(1, 100))
            })
            activity_start_time = activity_end_time

        sessions[f'{uuid.uuid4()}-{str(current_date)[:10]}'] = {
            'start_time': start_time.strftime('%Y-%m-%d %H:%M:%S'),
            'end_time': end_time.strftime('%Y-%m-%d %H:%M:%S'),
            'activities': activities
        }

        current_date += timedelta(days=random.randint(2, 4))

    return sessions

if __name__ == '__main__':
    createFirebaseApp()
    addData("Percy Jackson")
    addData("Annabeth Chase")
    addData("Grover Underwood")
    addData("Jason Grace")
    addData("Piper Mclean")
    addData("Leo Valdez")
    addData("Frank Zhang")
    addData("Hazel Levesque")
    addData("Nico Di Angelo")
    addData("Thalia Grace")
    addData("Harry Potter")
    addData("Hermione Granger")
    addData("Ron Weasley")
    addData("Severus Snape")
    addData("Albus Dumbledore")
    addData("Ginny Weasley")
    addData("Sirius Black")
    addData("Draco Malfoy")
    addData("Tom Riddle")
    addData("Cedric Diggory")
