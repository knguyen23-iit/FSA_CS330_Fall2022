from FSA_demo_0 import Lock
import random

sample = Lock()
times = sample.run_count_intruder()
print("It takes the intruder", times, "seconds to break the lock.")


