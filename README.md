# Python-Flask-Application-on-Kubernetes-with-MongoDB
This project involves deploying a Python + Flask application on Kubernetes with a MongoDB database. The Flask application performs CRUD operations on a MongoDB collection.
Prerequisites
•	Docker installed on your local machine
•	Docker Desktop installed with Kubernetes enabled
•	kubectl command-line tool installed
•	Python installed locally

1. Setting Up the Environment
Environment Preparation:
•	Install Docker Desktop (with Kubernetes enabled), and kubectl .
•	Create a folder for your project and ensure you have Python installed locally.
Project Structure:
•	Create the necessary files for your project, including a requirements.txt file to list the dependencies your project needs (Flask and pymongo).
2. Creating the Flask Application
Flask App Creation:
•	We created a Python script (app.py) for our Flask application. This script sets up routes to perform CRUD operations (Create, Read, Update, Delete) on a MongoDB collection. It connects to MongoDB, handles incoming HTTP requests, and interacts with the database to perform the required operations.
Dockerizing the App:
•	We created a Dockerfile to containerize our Flask application. The Dockerfile specifies the base image, installs the necessary dependencies, copies the application code, and defines how to run the app.
3. Creating the MongoDB Deployment
MongoDB Setup on Kubernetes:
•	Defined a MongoDB StatefulSet configuration to ensure a persistent and stable setup of MongoDB. This configuration includes details on how to create a MongoDB pod with persistent storage.
•	Also, created a service for MongoDB to make it accessible within the Kubernetes cluster.




4. Deploying the Flask Application on Kubernetes
Deployment Configuration:
•	Defined a deployment configuration for our Flask application. This includes specifying the Docker image to use, the number of replicas, and the port on which the application will run.
•	Created a service to expose our Flask application, allowing it to be accessible via a specific port.
Applying Configurations:
•	Use kubectl commands to apply the MongoDB StatefulSet and Flask deployment configurations to your Kubernetes cluster. This will create the necessary pods and services.






5. Verifying the Deployment
Check Deployment Status:
•	Used kubectl commands to check the status of the pods and services, ensuring that everything is running as expected.
Detailed Pod Information:
•	Described the MongoDB and Flask pods to get detailed information about their status and configuration.















6. ACCESSING THE WEB PAGE
Port Forwarding:
•	Set up port forwarding to access our Flask application locally. This allows you to interact with the application as if it were running on your local machine.

