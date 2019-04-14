# A program that calculates the next time window that the user should eat depending on the time it current protocol is and the fasting protocol to follow

import datetime

protocol = ''

while protocol.lower() != 'a' and protocol.lower() != 'b' and protocol.lower() != 'c':
    print('Enter fasting protocol to follow')
    print('A) 12 hours')
    print('B) 16 hours')
    protocol = input('C) 20 hours\n')

protocol = protocol.lower()

if protocol == 'a':
    protocol = datetime.timedelta(hours=12)

elif protocol == 'b':
    protocol = datetime.timedelta(hours=16)

elif protocol == 'c':
    protocol = datetime.timedelta(hours=20)

start = datetime.datetime.now()

print(start.year())
