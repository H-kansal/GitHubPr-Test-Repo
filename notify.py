import requests

class N:
    
    def send(self,user,msg):
        url="https://api.example.com/send"

        payload={
            "user":user,
            "message":msg
        }

        r=requests.post(url,json=payload)

        if r.status_code==200:
            return True

        return False


def notify_all(users):

    service=N()

    for u in users:
        service.send(u,"Welcome")

    return True