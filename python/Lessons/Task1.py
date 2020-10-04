import sys
import builtins






universes = sys.argv[1].strip('][').split(',')
l = len(universes)
universes = [int(x) for x in universes]


peaks = []
if universes[0]>= universes[1]:
    peaks.append(0)
if universes[l-1]>= universes[l-2]:
    peaks.append(l-1)

for i in range(1,l-1 ):
    #print(i)
    if universes[i]>=universes[i+1] and universes[i]>=universes[i-1]:
        peaks.append(i)

#print(peaks)
vac_sum = 0

for i in range(len(peaks)):
    vac_sum  += int(universes[peaks[i]])

print(vac_sum)


