class Sender(object):
    def __init__(self):
        self.__senderEmail = 'sender@gmail.com' # Change here
        self.__senderpwd   = 'XXXXXX'           # Type password here
    
    def get_email(self):
        return self.__senderEmail
    
    def get_senderpwd(self):
        return self.__senderpwd 

class Receiver(object):
    def __init__(self,fname,lname,email,pin,date):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.pincd = pin
        self.date  = date


SendMain = Sender()

## Make Receiver objects
rcv1 = Receiver('Firstname','Lastname','receiveremail@gmail.com','413512','06-05-2021')
rcv2 = Receiver('Firstname','Lastname','receiveremail@gmail.com','413003','06-05-2021')

## Append in Users
Users = [rcv1, rcv2]