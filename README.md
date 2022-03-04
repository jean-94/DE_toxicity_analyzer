# DE_toxicity_analyzer
A repository for "Data Engineering 2" project. It is a text toxicity analyzer

THe model need to be downloaded [here](https://github.com/unitaryai/detoxify/releases/download/v0.1-alpha/toxic_original-c1212f89.ckpt) and place in the Backend folder.

## Goals :

- The application is a toxicity monitor, where the user inputs a piece of text, and the application should be able to infer if the text is toxic or not.
- The text language used must be English
- The application should have a web interface with an input form and a submit button, where users can input their potentially toxic text, and hit submit, then the statistics about the text’s toxicity are displayed.
- Every functional part of the application must be tested for proper functionality.
- The application must be able to handle 100 requests per minute.
- The application must be easily deployable.
- The application must be properly monitored after deployment, we want to be able to quickly find any issue that might cause performance problems or down time.

## Project architecture :

- DE_toxicity_analyzer : the root directory of the project
  - Frontend : folder that contains the frontend files
    - Dockerfile : Docker image of the frontend
    - app.py : Frontend app in python flask
    - templates : contains the html of the docker
      - site.html : front and functionalities  of the website
  - Backend : folder that contains the backend files
    - Dockerfile : Docker image of the backend
    - app.py : Backend server in python flask
    - toxic_original-c1212f89.ckpt : Model for toxicity analyses
  - prometheus : Folder to setup prometheus
    - prometheus.yml : file that configure prometheus
    - rules.yml : file to configure the alertmanager into prometheus
  - alertmanager : Folder to setup alertmanager
    - alertmanager.yml : file to configure the alertmanager
  - docker-compose.yaml : requirements of the docker-compose
  - Jenkinsfile : File to create and update Jenkins pipeline
  - UITest.py : unittests for the application

## How to set up the project :

- Git clone the project into a directory using the following command : `git@github.com:theo-f-marechal/DE_toxicity_analyzer.git`

- Install docker

- ``docker-compose build`` in the folder to build the website

- ``docker-compose up`` in the folder to test the website

- To launch the tests, you have to pip install :

  - flask
  - detoxify
  - statistics
  - requests

  



