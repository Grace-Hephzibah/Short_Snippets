import time
import sys

class Random:

    def __init__(self):
        self.size = 5
        self.i = (int(time.time()) % time.gmtime().tm_sec) % self.size
        
        self.val_param = [time.gmtime().tm_hour, time.gmtime().tm_min, time.gmtime().tm_sec]
    
    def mul(self,a,b):
        # print("Mul")
        return a*b

    def add(self,a,b):
        # print("Add")
        return a+b;

    def sub(self, a,b):
        # print("Sub")
        if a>b:
            return a-b
        else:
            return b-a
        
    def div(self, a,b):
        # print("Div")
        return a/max(b,1)

    def power(self, a,b):
        # print("Power")
        reduction_factor = 10**5
        return (a**5 + b**5) % (reduction_factor)

    def random(self, max_val = (sys.maxsize**1/2)):

        self.operations = [self.add, self.sub, self.mul, self.div, self.power]

        a = time.gmtime().tm_sec + self.i
        
        for val in self.val_param:
            a *= self.operations[self.i](a, val)
            self.i = (self.i+1) % self.size

        self.i = (self.i+9) % self.size
        return int(a)%max_val

# Testing Code
rand = Random()
for i in range(1000):
    print(rand.random(3), end = '\t')
    if (i==5):
        print()
