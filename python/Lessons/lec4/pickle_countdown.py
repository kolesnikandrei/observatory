import time
import pickle
from countdown import Countdown

timer = Countdown(30)
file_with_state = open('c_state.p', 'wb')
time.sleep(15)
pickle.dump(timer, file_with_state)
file_with_state.close()
