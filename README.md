## ezVote is a flexible and easy-to-use voting system application for clients as well as for administrator to set-up poll(s) with admin privileges and a seperate page.

#### The app can be accessed at localhost:8000

* To start the application:

1. Clone this repo to your local machine
2. cd into the project repo
3. Run the following commands in terminal:

`virtualenv venv`
`source venv/bin/activate`
`pip3 install -r requirements.txt`

4. Now run the following command to Create a superuser(admin):

`python manage.py createsuperuser`

**_In the prompt, enter username, email and password for admin account_**

5. To initialize the application, run:
`python manage.py runserver`

**_Make sure that you have python3, pip3 and virtualenv installed in host machine._**
