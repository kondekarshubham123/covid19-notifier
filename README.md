# covid19-vaccine-notifier


### Functions

`emailsend(user,data)`      :-- 📧 Mail Notifier 

`dummySend(user,data)`      :-- 🖥️ Display data on termial/cmd  

`songNotify(user, data)`    :-- 🔊 Song notifier 


You can use any of these function from `code.py:ln 22`

### Usage

1. Download repository & locate it

    ```markdown
    $ git clone https://github.com/kondekarshubham123/covid19-vaccine-notifier.git
    $ cd covid19-vaccine-notifier
    ```


2. Make copy of `credential_temp.py` and rename it to `credential.py`

    ```markdown
    $ mv credential_temp.py credential.py
    ```


3. Type your gmail email-id and password in `credential.py`

    ```markdown
    class Sender(object):
    def __init__(self):
        self.__senderEmail = 'sender@gmail.com' # Change here
        self.__senderpwd   = 'XXXXXX'           # Type password here
    ```
    
    and make sure you allow [Less secure app](https://myaccount.google.com/lesssecureapps) from your gmail.
    

4. Create users and append Receiver object to Users list

    ```markdown
    Example: 
    
    rcv1 = Receiver('Firstname','Lastname','receiveremail@gmail.com','Pincode','DD-MM-YYYY')
    rcv2 = Receiver('Firstname','Lastname','receiveremail@gmail.com','Pincode','DD-MM-YYYY')
    .
    .
    .
    
    Users = [rcv1,rcv2,...]
    ```
    
And thats all.


5. Final step run `code.py`.

    ```markdown
    python3 code.py
    ```
