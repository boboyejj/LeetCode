# Machine Learning Assistant

Machine Learning Assistant is a labeling tool for researchers to upload their own unlabeled data to be labelled by other users of the platform know as labelers. This platform will allow researchers to specify details about the labels they need to ensure the usefulness and uniformity of the resulting data set.

The following are the instructions of how to install and run the application for Mac and Windows users.

## For Mac User

#### Clone Repository
Go the the target folder in which you want to clone the repository, and then:

`git clone http://cmsc435.garrettvanhoy.com/nubbify/machine-learning-assistant.git`

#### Environment Setup 

`python3 -m venv venv`

`. venv/bin/activate`

#### Install flask
> Note: If on the master branch execute this before the following commands: 

> `pip install -e ../..`)

`pip install -e .`

#### Specify application and environment

`export FLASK_APP=flaskr`

`export FLASK_ENV=development`

#### Initialize database

`flask init-db`

#### Run Application

`flask run`

Then the application is running on  http://127.0.0.1:5000/


## For Windows User

#### Clone Repository
Go the the target folder in which you want to clone the repository, and then:

`git clone http://cmsc435.garrettvanhoy.com/nubbify/machine-learning-assistant.git`

#### Environment Setup 

`py -3 -m venv venv`

`venv\Scripts\activate.bat`

#### Install Flask

>Note: If on the master branch execute this before the following commands: 

>`pip install -e ../..`

`pip install -e .`

#### Specify application and environment

`set FLASK_APP=flaskr`

`set FLASK_ENV=development`

#### Initialize database

`flask init-db`

#### Run Application

`flask run`

Then the application is running on  http://127.0.0.1:5000/


## Testing the Application

`pip install '.[test]'`

`pytest`

 
