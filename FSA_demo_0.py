import random

class Lock:
    def __init__(self): #525271 and 525274
        self.lock = [0, 0, 0, 0, 0, 0]
        self.state = 0

    def check(self):
        ret=-1
        for i in range(len(self.lock)-1):
            if self.lock[i]==1 and self.lock[i+1]==0:
                ret = i
                break
            elif self.lock[len(self.lock)-1]==1:
                ret = 5
                break
        return ret
        
    def entry(self, val):
        try:
            val = int(val)
        except:
            val = -2 
        if val==5:
            if self.check()==-1:
                self.lock[0]=1
            elif self.check()==1:
                self.lock[2]=1
            else:
                self.lock=[0]*6
        if val==2:
            if self.check()==0:
                self.lock[1]=1
            elif self.check()==2:
                self.lock[3]=1
            else:
                self.lock=[0]*6
        if val==7:
            if self.check()==3:
                self.lock[4]=1
            else:
                self.lock=[0]*6
        if val==1:
            if self.check()==4:
                self.state = 1
                self.lock=[0]*6
            else:
                self.lock=[0]*6
                
        if val==4:
            if self.check()==4:
                self.state = 0
                self.lock=[0]*6
            else:
                self.lock=[0]*6
                
    def check_state(self):
        if self.state==0:
            return "Locked"
        elif self.state==1:
            return "Unlocked"
    
    def run_count_intruder(self):
        count = 0
        while self.state==0:
            i = random.randint(0, 9)
            self.entry(i)
            count+=1
        return count
    
    
    

            
   
