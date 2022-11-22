from FSA_demo_0 import Lock
import random

sample = Lock()
times = sample.run_count_intruder()
print("Estimated 1,000,000 seconds on average for intruder to break the lock.")
print("It takes the intruder", times, "seconds to break the lock.")


