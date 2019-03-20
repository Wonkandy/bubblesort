import numpy as np

#array = np.genfromtxt("in.txt", dtype='int')
array = np.random.randint(0, 100, 10000)
np.savetxt("out.txt", array)
print(array)
tausche = 0
vergleiche = 0
test = 0

for x in range(len(array)-1):
    for i in range(len(array)-1):
        vergleiche += 1
        test += array[i]
        if(array[i] > array[i+1]):
            array[i],array[i+1] = array[i+1], array[i]
            tausche += 1

print(array)
print("Tausche: ", tausche)
print("Vergleiche: ", vergleiche)
print(test/len(array))

