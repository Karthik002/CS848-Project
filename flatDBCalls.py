import firebase_admin
from firebase_admin import db

def createFirebaseApp():
    if not firebase_admin._apps:
        creds = firebase_admin.credentials.Certificate('flatDBServiceAccountKey.json')
        default_app = firebase_admin.initialize_app(creds, {
            'databaseURL': 'https://cs848-project-flat-database-default-rtdb.firebaseio.com'
        })

def getData():
    createFirebaseApp()
    userRef = db.reference("users")
    print(userRef.get())
    sessionsRef = db.reference("sessions")
    print(sessionsRef.get())
    activitiesRef = db.reference("activities")
    print(activitiesRef.get())
    statesRef = db.reference("states")
    print(statesRef.get())


if __name__ == '__main__':
    getData()