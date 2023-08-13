# Gas Utility Company - Bynry Backend Challenge

## Overview
Welcome to the Gas Utility Company application, developed for the Bynry Backend hiring challenge. This application streamlines service requests and customer interactions for a gas utility company.

## Admin Side
The admin side is designed to manage service requests and maintain their status. Key features include:
- Access to all service requests.
- Update request statuses with notes.
- Admin users are separate and not created through signup.

## User Side
The user side empowers customers with convenient service request submission and tracking. It offers:
- User login and signup pages.
- Access to personal information.
- Easy service request submission with file attachments.
- Real-time tracking of service request statuses.

## Steps to run the project

Please run the following commands to run the project-
```
    python django_web_app/manage.py makemigrations

    python django_web_app/manage.py migrate

    python django_web_app/manage.py runserver
```

> The first two commands in our case are not compulsory as we have pushed all the required files. 

Please create a super user to access the admin side. The command to create one is - 

```
    python manage.py createsuperuser
```

### Submitted By -
For any inquiries or collaboration opportunities, feel free to reach out to:

**Karikay Bansal**

**kartikay.bansal2014@gmail.com**

### Note -

Efforts have been made to come up with a solution good enough in the given time frame. The solution is not perfect but it holds firm against all the mentioned requirements and has been tested for the same. Please have a look and any feedback is well appreciated!
