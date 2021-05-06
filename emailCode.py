import smtplib
from credential import SendMain
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def emailsend(user,data):
    
    mail_content = '''Hello,
    Below are the list of covid centers.\n
    
    '''
    # print(mail_content)
    # print(user,data)

    lis = '\n----------------------\n'
    for hos in data['sessions']:
        # print(hos['name'],hos['address'],hos['state_name'],hos['pincode'],hos['fee_type'],hos['date'],hos['available_capacity'],
        # hos['fee'],hos['min_age_limit'],hos['vaccine'])
        
        lis += "Hospital name       :   " +hos['name']                    + '\n'
        lis += "Hospital Pincode    :   " +str(hos['pincode'])            + '\n'
        lis += "Fee type            :   " +str(hos['fee_type'])           + '\n'
        lis += "Available Capacity  :   " +str(hos['available_capacity']) + '\n'
        lis += "Age Limit           :   " +str(hos['min_age_limit'])      + '\n'
        lis += "Vaccine type        :   " +hos['vaccine']                 + '\n'
        lis += '----------------------\n'
    
    mail_content += lis

    #The mail addresses and password
    sender_address = SendMain.get_email()
    sender_pass = SendMain.get_senderpwd()

    receiver_address = user.email

    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Vaccine Update !!'   #The subject line
    
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))

    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()

    print('Mail Sent to ',user.email)


def dummySend(user,data):
    
    mail_content = '''Hello,
    Below are the list of covid centers.\n
    
    '''
    # print(mail_content)
    # print(user,data)

    lis = '\n----------------------\n'
    for hos in data['sessions']:
        # print(hos['name'],hos['address'],hos['state_name'],hos['pincode'],hos['fee_type'],hos['date'],hos['available_capacity'],
        # hos['fee'],hos['min_age_limit'],hos['vaccine'])
        
        lis += "Hospital name       :   " +hos['name']                    + '\n'
        lis += "Hospital Pincode    :   " +str(hos['pincode'])            + '\n'
        lis += "Fee type            :   " +str(hos['fee_type'])           + '\n'
        lis += "Available Capacity  :   " +str(hos['available_capacity']) + '\n'
        lis += "Age Limit           :   " +str(hos['min_age_limit'])      + '\n'
        lis += "Vaccine type        :   " +hos['vaccine']                 + '\n'
        lis += '----------------------\n'

    print(mail_content+lis)