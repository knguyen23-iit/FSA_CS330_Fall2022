# FSM Security Device by Ky Nguyen
This is a small project demonstrating a FSM-based Security Device for CS 330 - Discrete Maths at IIT.



This Project was written using Python. It has only been tested on Windows.


Description for each files:

The class for the Security Device is in: FSM_demo_0.py

The unit tests for the Security Device is in: test_FSM_demo_0.py

The program to test how many times it takes the intruder to break the lock is in: FSM_interactive_0.py

The program for you to use the Security Device is: FSM_interactive_1.py

Unlock using: 525271. Lock using: 525274.

Memo

https://drive.google.com/file/d/1ByPDu5WmlMwzZ7HbZj7Sh936hom3OVmJ/view?usp=sharing


Step 1: Clone this repository to your machine
      
      https://github.com/knguyen23-iit/FSM_KyNguyen.git


Step 2: Open Command Prompt on your machine with Windows

Step 3: Install pip      
      Enter these in Command Prompt:
      
      curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
      
      python get-pip.py


Step 4: Install "coverage.py" for unit test coverage report
      
Enter this in Command Prompt to install "coverage.py" :
            
     pip install coverage
      

Step 5: Run  the files

a. Change directory to the files that were cloned to your machine
      
      cd /d *filepath
      

b. Run the executables
   
   This is the class for the Security Device:
   
      coverage run FSM_demo_0.py
      
   This is for the unit tests:
      
      coverage run test_FSM_demo_0.py
   
   Then run this to generate coverage report:
       
      coverage report -m
      

Step 6: Try out the interactive executables

Interactive Executable 1: 
It will return how many entries the intruder have to enter to break the lock by entering uniformly distributed random numbers.
          
      coverage run FSM_interactive_0.py
            
    
Interactive Executable 2: 
You can enter the number to try to lock or unlock the Security Device. 

     coverage run FSM_interactive_1.py
                     
