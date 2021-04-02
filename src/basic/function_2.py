from datetime import datetime

def f1(x):
    a = 3 
    b = 5
    y = a * x + b

    return y


def f2(x):
    a = 3 
    b = 5
    return (x - b) / a


def triple(x) :
    return x * x * x

def showToday() :
    return datetime.today()

