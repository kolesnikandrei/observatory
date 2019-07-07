import re


file = open('regex_sum_210026.txt')
s = 0

all = re.findall('([\d]+)',file.read())
#print(sum(all))
for d in all:	
		s += int(d)

print(s)
