# CS848 Project
The following files contain the code used in the CS848 Project. 
It contains two files for three types of databases (nested, flat, hybrid).
## Data Generator
Each database structure has a data generator file that populates the database with sample data. The file just has to be run with a service account key to any Firebase Realtime Database and it will populate it with that data.
## DB Calls
Each database structure also has a DBCalls file that retrieves data from every API route for that corresponding database. The file also has to be run with the same service account key used for the data generator file and it will retrieve the data accordingly.
## Firebase CLI Profiler
In order to measure the speed and bandwidth of each of the database structures, the following link can be followed to install and use the CLI profiler: https://firebase.google.com/docs/database/usage/profile
## Replication Instructions
To test out each type of database, the service account key has to be added to the directory from any Firebase project (this confidential JSON file is not allowed to be pushed to Github so you will have to create your own). Once the service account key is added to the folder, it needs to be added to the 'creds' section and the right database URL also needs to be added in right below. After that, the code can be run and the database will be populated with the sample data. Next, the CLI profiler can be turned on and the DB Calls file can be run with the same 'creds' and database URL to measure the speed and bandwidth usage of each of the database structures.
