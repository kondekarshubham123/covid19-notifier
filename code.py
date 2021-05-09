import sys
import time
import json
import requests
import threading
from Notifier import emailsend,dummySend,notifiybysong
from credential import Users



def User_check(user):
    while True:
        time.sleep(10)
        api= "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode="+user.pincd+"&date="+user.date
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        response = requests.get(api, headers = headers)
        op = json.loads(response.text)
        if op['sessions'] == []:
            pass
        else:
            #dummySend(user,op)
            notifiybysong(user,op)
            sys.exit()

for use in Users:
    # User_check(use)
    t1 = threading.Thread(target=User_check, args=(use,))
    t1.start()