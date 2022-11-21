# FSA by Ky Nguyen
This is a small project demonstrating a Security Device for CS 330 - Discrete Maths at IIT. 

Unlock using: 525271. Lock using: 525274.





Step 1: Clone this repository to your machine
      https://github.com/knguyen23-iit/FSA_CS330_Fall2022.git

Step 2: Open Command Prompt on your machine with Windows

Step 3: Run tests and producing coverage report:

          Installing pip by enter:
          curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    
          Then enter this:
          python get-pip.py
          
          Then install coverage.py by entering: "pip install coverage"

          Using "cd /d *filepath" to change the directory to the files that were cloned onto your machine

          Enter "coverage run FSA_demo_0.py" to run the FSA class

          Enter "coverage run test_FSA_demo_0.py" to run the unit tests

          Enter "coverage report -m" for it to produce a coverage report

Executable 1: 
          
            Enter "coverage run FSA_interactive_0.py" to run the executable
            It will return how many entries the intruder have to enter to break the lock by entering random numbers.
    
Executable 2: 

            Enter "coverage run FSA_interactive_1.py" to run the executable
            You can enter the number to try to lock or unlock the lock.          
