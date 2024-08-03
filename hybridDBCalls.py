import firebase_admin
from firebase_admin import db

def createFirebaseApp():
    if not firebase_admin._apps:
        creds = firebase_admin.credentials.Certificate('hybridDBServiceAccountKey.json')
        default_app = firebase_admin.initialize_app(creds, {
            'databaseURL': 'https://cs848-project-hybrid-database-default-rtdb.firebaseio.com'
        })

def getData():
    createFirebaseApp()
    userRef = db.reference("group1/users")
    print(userRef.get())
    activitiesRef = db.reference("group1/activities")
    print(activitiesRef.get())


if __name__ == '__main__':
    getData()