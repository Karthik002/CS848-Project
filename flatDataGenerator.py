import uuid
import firebase_admin
from firebase_admin import db
import random
from datetime import datetime, timedelta

def createFirebaseApp():
    if not firebase_admin._apps:
        creds = firebase_admin.credentials.Certificate('flatDBServiceAccountKey.json')
        default_app = firebase_admin.initialize_app(creds, {
            'databaseURL': 'https://cs848-project-flat-database-default-rtdb.firebaseio.com'
        })

def addData(user):
    createFirebaseApp()
    userRef = db.reference("users")
    sessionRef = db.reference("sessions")
    activityRef = db.reference("activities")
    stateRef = db.reference("states")

    user_id = str(uuid.uuid4())
    userRef.child(user_id).set({"name": user})

    data = createJSONData(datetime(2011, 1, 11), datetime(2020, 12, 29), user_id)
    sessionRef.update(data["sessions"])
    activityRef.update(data["activities"])
    stateRef.update(data["states"])

def createJSONData(startDate, endDate, user_id):
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
    activities = {}
    states = {}
    current_date = startDate

    while current_date < endDate:
        start_time = current_date + timedelta(hours=random.randint(0, 23), minutes=random.randint(0, 59))
        session_duration = timedelta(hours=random.randint(1, 3), minutes=random.randint(0, 59))
        end_time = start_time + session_duration

        session_id = str(uuid.uuid4())
        sessions[session_id] = {
            'user_id': user_id,
            'start_time': start_time.strftime('%Y-%m-%d %H:%M:%S'),
            'end_time': end_time.strftime('%Y-%m-%d %H:%M:%S')
        }

        num_activities = random.randint(3, 6)
        selected_activities = random.sample(activities_list, k=num_activities)

        activity_duration = session_duration / num_activities
        activity_start_time = start_time

        for activity in selected_activities:
            activity_end_time = activity_start_time + activity_duration
            activity_id = str(uuid.uuid4())
            
            activity_states = []
            state_start_time = activity_start_time
            state_id = 1

            while state_start_time < activity_end_time:
                state_duration = timedelta(seconds=random.randint(300, 900))
                state_end_time = min(state_start_time + state_duration, activity_end_time)
                state_entry_id = str(uuid.uuid4())
                states[state_entry_id] = {
                    'activity_id': activity_id,
                    'state_id': state_id,
                    'start_time': state_start_time.strftime('%Y-%m-%d %H:%M:%S'),
                    'end_time': state_end_time.strftime('%Y-%m-%d %H:%M:%S')
                }
                activity_states.append(state_entry_id)
                state_start_time = state_end_time
                state_id += 1

            activities[activity_id] = {
                'session_id': session_id,
                'name': activity,
                'start_time': activity_start_time.strftime('%Y-%m-%d %H:%M:%S'),
                'end_time': activity_end_time.strftime('%Y-%m-%d %H:%M:%S'),
                'states': activity_states,
                'score': str(random.randint(1, 100))
            }
            activity_start_time = activity_end_time

        current_date += timedelta(days=random.randint(2, 4))

    return {"sessions": sessions, "activities": activities, "states": states}

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
