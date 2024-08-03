import firebase_admin
from firebase_admin import db

def createFirebaseApp():
    if not firebase_admin._apps:
        creds = firebase_admin.credentials.Certificate('nestedDBServiceAccountKey.json')
        default_app = firebase_admin.initialize_app(creds, {
            'databaseURL': 'https://cs848-project-nested-db-default-rtdb.firebaseio.com'
        })

def getData(user):
    createFirebaseApp()
    sessionRef = db.reference("group1/users/" + user)
    print(sessionRef.get())


if __name__ == '__main__':
    createFirebaseApp()
    getData("Percy Jackson")
    getData("Annabeth Chase")
    getData("Grover Underwood")
    getData("Jason Grace")
    getData("Piper Mclean")
    getData("Leo Valdez")
    getData("Frank Zhang")
    getData("Hazel Levesque")
    getData("Nico Di Angelo")
    getData("Thalia Grace")
    getData("Harry Potter")
    getData("Hermione Granger")
    getData("Ron Weasley")
    getData("Severus Snape")
    getData("Albus Dumbledore")
    getData("Ginny Weasley")
    getData("Sirius Black")
    getData("Draco Malfoy")
    getData("Tom Riddle")
    getData("Cedric Diggory")