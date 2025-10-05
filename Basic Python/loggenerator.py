# 1 -> Generate log without class

import logging
from logging import handlers, StreamHandler

#log define krna pdega
log = logging.getLogger() #yha pe maine log variable ko logger me convert kr diya ab log logger jaisa kaam krega
log.setLevel(logging.DEBUG) #yha pe is logger ka level set kr diya by default warning hota h maine debug kr diya

#log console pe handle krne keliye handler bnana h 
def consolehandler():
    #sbse phle streamhandler ka use krna pdega console pe data print krne keliye
    #yha pe maine x ko ek Streamhandler bnaya hu 
    x = logging.StreamHandler()     
    x.setLevel(logging.DEBUG)   #ab x console me kon kon se data dalenga DEBUG Level tk ke data dalega
    f1 = logging.Formatter('%(asctime)s - %(name)s - %(message)s') #fromat assign kr rha hu console pe kaise print hoga
    x.setFormatter(f1)
    log.addHandler(x) # x ko maine log ke ander daal diya h 
    return log

def filehandler():
    #sabse phle file handler add krna pdega
    y = handlers.RotatingFileHandler(filename='demo.log', maxBytes=400, backupCount=3)
    y.setLevel(logging.DEBUG)
    f2 = logging.Formatter('%(asctime)s -  %(message)s')
    y.setFormatter(f2)
    log.addHandler(y)
    return y

consolehandler()
filehandler()

for i in range(200):
    log.info('i am so not so good')




# 2 -> Generate log with class

import logging
from logging import handlers, StreamHandler

#class ke ander sb kuch krna h object bnana h aur us object ko property dena h fir class ko call krna h
class loggenerator():
    def __init__(self,log_level):
        self.log = logging.getLogger()
        self.log.setLevel(log_level)
    
    def consolehandler(self):
        x = logging.StreamHandler()
        x.setLevel(logging.DEBUG)
        f1 = logging.Formatter('%(asctime)s - %(name)s - %(message)s') #fromat assign kr rha hu console pe kaise print hoga
        x.setFormatter(f1)
        self.log.addHandler(x)
        return self # yha pe object return ho rha h isiliye baaki handler bhi aa skte h 
    
    def filehandler(self):
        y = handlers.RotatingFileHandler(filename='modbuslog', maxBytes=1000, backupCount=10)
        y.setLevel(logging.DEBUG)
        f2 = logging.Formatter('%(asctime)s - %(name)s - %(message)s') #fromat assign kr rha hu console pe kaise print hoga
        y.setFormatter(f2)
        self.log.addHandler(y)
        return self # yha pe bhi object return ho rha h to baake aur handler is chain me aa skte h 
    
    def returnlog(self):
        return self.log # yha pe ek logger return ho rha ab chain ni aayega, direct log(logger) hi return ho rha h

log = loggenerator(logging.DEBUG).consolehandler().filehandler().returnlog() # yha pe returnlog() me logger return hua isiliye log ko logger mila 

for i in range(1000):
    log.info(f"bro all are running: {i}")



# 3 -> Basic of logging and log 

import logging

logging.basicConfig(
    filename='Amber',
    level= logging.DEBUG,
    format= '%(asctime)s %(name)s  %(message)s'
)
x = logging.getLogger()

for i in range(8):
    x.info('finallywooooo')