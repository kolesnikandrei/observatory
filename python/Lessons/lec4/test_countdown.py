import pickle
import time

file_with_state = open('c_state.p', 'rb')
pickle.load(file_with_state)
time.sleep(20)
file_with_state.close()
