import pickle

data = ('some', 'object', 'to', 'test', 'pickle')

with open('tin.bin', 'wb') as tin:
    pickle.dump(data, tin)

with open('tin.bin', 'rb') as tin:
    restored_data = pickle.load(tin)

print(type(restored_data))
print(restored_data)
