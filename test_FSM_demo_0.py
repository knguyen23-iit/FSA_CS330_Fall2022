import unittest


from FSM_demo_0 import Lock

class TestFSA(unittest.TestCase):
    
    # 1 - unit test for: __init__(self)
    def test_0_init(self):
        sample = Lock()
        self.assertEqual(sample.state, 0)
        self.assertEqual(sample.lock[0], 0)
        self.assertEqual(sample.lock[1], 0)
        self.assertEqual(sample.lock[2], 0)
        self.assertEqual(sample.lock[3], 0)
        self.assertEqual(sample.lock[4], 0)
        self.assertEqual(sample.lock[5], 0)
    
    #2 - unit test for: check(self)
    def test_0_check(self):
        sample = Lock()
        sample.lock = [0, 0, 0, 0, 0, 0]
        self.assertEqual(sample.check(), -1)
        sample.lock = [1, 0, 0, 0, 0, 0]
        self.assertEqual(sample.check(), 0)
        sample.lock = [1, 1, 0, 0, 0, 0]
        self.assertEqual(sample.check(), 1)
        sample.lock = [1, 1, 1, 0, 0, 0]
        self.assertEqual(sample.check(), 2)
        sample.lock = [1, 1, 1, 1, 0, 0]
        self.assertEqual(sample.check(), 3)
        sample.lock = [1, 1, 1, 1, 1, 0]
        self.assertEqual(sample.check(), 4)
        sample.lock = [1, 1, 1, 1, 1, 1]
        self.assertEqual(sample.check(), 5)
        
    #3 - unit test for: entry(self, val)
    def test_0_entry(self): 
        #test for cases where entries are strings
        #if strings are entered then nothing changes
        sample = Lock()
        sample.entry('discrete maths')
        self.assertEqual(sample.check(), -1)
        
    def test_1_entry(self): #check for entering val=5
        #enter 5 at index 0 - passcode is '5'-2-5-2-7-1
        sample0 = Lock()
        sample0.lock = [0, 0, 0, 0, 0, 0]
        sample0.entry(5)
        self.assertEqual(sample0.check(), 0)
        
        #enter 5 at index 2 - passcode is 5-2-'5'-2-7-1
        sample1 = Lock()        
        sample1.lock = [1, 1, 0, 0, 0, 0]
        sample1.entry(5)
        self.assertEqual(sample1.check(), 2)
        
        #enter 5 at wrong positions - passcode is 5-2-5-2-7-1
        sample2 = Lock()        
        sample2.lock = [1, 0, 0, 0, 0, 0]
        sample2.entry(5)
        self.assertEqual(sample2.check(), -1)
        
        sample3 = Lock()        
        sample3.lock = [1, 1, 1, 0, 0, 0]
        sample3.entry(5)
        self.assertEqual(sample3.check(), -1)
        
        sample4 = Lock()        
        sample4.lock = [1, 1, 1, 1, 0, 0]
        sample4.entry(5)
        self.assertEqual(sample4.check(), -1)
        
    def test_2_entry(self): #check for entering val=2
        #enter 2 at index 1 - passcode is 5-'2'-5-2-7-1
        sample0 = Lock()
        sample0.lock = [1, 0, 0, 0, 0, 0]
        sample0.entry(2)
        self.assertEqual(sample0.check(), 1)
        
        #enter 2 at index 3 - passcode is 5-2-5-'2'-7-1
        sample1 = Lock()        
        sample1.lock = [1, 1, 1, 0, 0, 0]
        sample1.entry(2)
        self.assertEqual(sample1.check(), 3)
        
        #enter 2 at wrong positions - passcode is 5-2-5-2-7-1
        sample2 = Lock()        
        sample2.lock = [0, 0, 0, 0, 0, 0]
        sample2.entry(2)
        self.assertEqual(sample2.check(), -1)
        
        sample3 = Lock()        
        sample3.lock = [1, 1, 0, 0, 0, 0]
        sample3.entry(2)
        self.assertEqual(sample3.check(), -1)
        
        sample4 = Lock()        
        sample4.lock = [1, 1, 1, 1, 0, 0]
        sample4.entry(2)
        self.assertEqual(sample4.check(), -1)
        
    def test_3_entry(self): #check for entering val=7
        #enter 7 at index 4 - passcode is 5-2-5-2-'7'-1
        sample0 = Lock()
        sample0.lock = [1, 1, 1, 1, 0, 0]
        sample0.entry(7)
        self.assertEqual(sample0.check(), 4)
        
        #enter 7 at wrong positions - passcode is 5-2-5-2-7-1
        sample1 = Lock()        
        sample1.lock = [0, 0, 0, 0, 0, 0]
        sample1.entry(7)
        self.assertEqual(sample1.check(), -1)
        
        sample2 = Lock()        
        sample2.lock = [1, 0, 0, 0, 0, 0]
        sample2.entry(7)
        self.assertEqual(sample2.check(), -1)
        
        sample3 = Lock()        
        sample3.lock = [1, 1, 0, 0, 0, 0]
        sample3.entry(7)
        self.assertEqual(sample3.check(), -1)
        
        sample4 = Lock()        
        sample4.lock = [1, 1, 1, 0, 0, 0]
        sample4.entry(7)
        self.assertEqual(sample4.check(), -1)
        
    def test_4_entry(self): #check for entering val=1
        #enter 1 at index 4 - passcode is 5-2-5-2-7-'1'
        sample0 = Lock()
        sample0.lock = [1, 1, 1, 1, 1, 0]
        sample0.entry(1)
        self.assertEqual(sample0.check(), -1)
        self.assertEqual(sample0.state, 1)
        
        #enter 1 at wrong positions - passcode is 5-2-5-2-7-1
        sample2 = Lock()        
        sample2.lock = [0, 0, 0, 0, 0, 0]
        sample2.entry(1)
        self.assertEqual(sample2.check(), -1)
        
        sample3 = Lock()        
        sample3.lock = [1, 0, 0, 0, 0, 0]
        sample3.entry(1)
        self.assertEqual(sample3.check(), -1)
        
        sample4 = Lock()        
        sample4.lock = [1, 1, 0, 0, 0, 0]
        sample4.entry(1)
        self.assertEqual(sample4.check(), -1)
        
        sample5 = Lock()        
        sample5.lock = [1, 1, 1, 0, 0, 0]
        sample5.entry(1)
        self.assertEqual(sample4.check(), -1)
        
        sample6 = Lock()        
        sample6.lock = [1, 1, 1, 1, 0, 0]
        sample6.entry(1)
        self.assertEqual(sample6.check(), -1)
        
    def test_5_entry(self): #check for entering val=4
        #enter 4 at index 4 - passcode is 5-2-5-2-7-'1'
        sample0 = Lock()
        sample0.lock = [1, 1, 1, 1, 1, 0]
        sample0.entry(4)
        self.assertEqual(sample0.check(), -1)
        self.assertEqual(sample0.state, 0)
        
        #enter 4 at wrong positions - passcode is 5-2-5-2-7-1
        sample2 = Lock()        
        sample2.lock = [0, 0, 0, 0, 0, 0]
        sample2.entry(4)
        self.assertEqual(sample2.check(), -1)
        
        sample3 = Lock()        
        sample3.lock = [1, 0, 0, 0, 0, 0]
        sample3.entry(4)
        self.assertEqual(sample3.check(), -1)
        
        sample4 = Lock()        
        sample4.lock = [1, 1, 0, 0, 0, 0]
        sample4.entry(4)
        self.assertEqual(sample4.check(), -1)
        
        sample5 = Lock()        
        sample5.lock = [1, 1, 1, 0, 0, 0]
        sample5.entry(4)
        self.assertEqual(sample4.check(), -1)
        
        sample6 = Lock()        
        sample6.lock = [1, 1, 1, 1, 0, 0]
        sample6.entry(4)
        self.assertEqual(sample6.check(), -1)

        
    #4 - unit tests for method: 'check_state' 
    def test_0_check_state(self):
        #check if unlocked after enter unlocking code
        sample = Lock()
        sample.entry(5)
        sample.entry(2)
        sample.entry(5)
        sample.entry(2)
        sample.entry(7)
        sample.entry(1)
        self.assertEqual(sample.check_state(),"Unlocked")
    
    def test_1_check_state(self): 
        #check if locked after enter locking code
        sample = Lock()
        sample.entry(5)
        sample.entry(2)
        sample.entry(5)
        sample.entry(2)
        sample.entry(7)
        sample.entry(4)
        self.assertEqual(sample.check_state(),"Locked")
    
    def test_2_check_state(self): 
        #lock starting state is "Locked"
        sample = Lock()
        self.assertEqual(sample.check_state(),"Locked")
        
    #5 - unit tests for method: 'run_count_intruder'
    def test_0_runCountIntruder(self):
        sample = Lock()
        self.assertGreater(sample.run_count_intruder(), 0)

if __name__ == '__main__':
    unittest.main()



        