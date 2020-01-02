# email-app
Django app for sending emails with the help of SMTP server

This project is composed of python script and django webapp for sending email to anyone with the help of SMTP server.

Here, we uses google smtp server for sending mails.

Steps to setup this project (run this in your terminal or cmd):

> 1. If you are using google smtp server then you have to first disable the less secure apps option from your sender email account or use this link for help https://support.google.com/a/answer/6260879?hl=en
> 2. clone the repository by command < git clone https://github.com/redcrix/email-app.git >
> 3. use command < cd email-app >
> 4. run install.py by command < python install.py > it will install all the libraries which are required to run this project.
> 5. After the whole libraries install now its time to start the webapp.
> 6. Use command < python manage.py runserver > for starting the webapp.








Note: If their is an problem in running the install.py file then use the manual commands which are writen below.

pip install validate_email

pip install secure-smtplib

pip install email-to

pip3 install py3DNS  





It is not necessary to create virtual environment for running this webapp.



>>>>>for mac and linux use python3 and pip3 in place of python and pip.
