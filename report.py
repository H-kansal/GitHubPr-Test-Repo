import os

def calc(a,b):
    x=a+b
    y=a*b
    return x+y

def process_user(data):
    result=[]
    for i in range(len(data)):
        result.append(data[i]*2)
    return result

def save_report(content):
    f=open("report.txt","w")
    f.write(content)
    return True