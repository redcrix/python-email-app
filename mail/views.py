from django.shortcuts import render
from .forms import MailForm
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from validate_email import validate_email

def mail(request):
    if request.POST:
        form=MailForm(request.POST)
        if form.is_valid():
            #data=form.save()
            e = validate_email(str(form.cleaned_data['sender'].lower()), verify=True)
            if e==True:
                msg = MIMEMultipart()
                msg['From'] = str(form.cleaned_data['sender'].lower())
                msg['To'] = str(form.cleaned_data['to'].lower())
                msg['Subject'] = str(form.cleaned_data['subject'])
                msg.attach(MIMEText(str(form.cleaned_data['body']), 'plain'))
                text = msg.as_string()
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.ehlo()
                server.login(str(form.cleaned_data['sender'].lower()), str(form.cleaned_data['password']))
                server.sendmail(str(form.cleaned_data['sender'].lower()), str(form.cleaned_data['to'].lower()), text)
                server.quit()
                return render(request, 'mail.html',
                              {'form': form, 'result': 'Email sent'})
            else:
                return render(request, 'mail.html',
                              {'form': form, 'result': 'Something went wrong'})
    else:
        form = MailForm()
        return render(request, 'mail.html', {'form': form})
