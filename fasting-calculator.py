# A program that calculates the next time window that the user should eat depending on the time it current protocol is and the fasting protocol to follow

############################ MAKE IT SO THAT THE USER CAN ENTER SPECIFIC HOURS INSTEAD OF PRESET###############################################

######### PROGRAM COULD SEND A TEXT MESSAGE OR A NOTIFICATION TO CELLPHONE WHEN THERE IS LITTLE TIME LEFT TO BREAK THE FAST ###################

############################ COULD LINK TO VARIOUS RESOURCES TO LEARN ABOUT HOW TO BREAK A FAST IN A SAFE, HEALTHY AND PROPER MANNER IN ORDER TO GAIN GOOD RESULTS FROM THE DIET##############################################

############################ LINK TO A FOOD DATABASE TO GET INFO ON GOOD FOODS TO CONSUME WHEN BREAKING A FAST AS WELL AS RECOMMENDED FOODS BASED ON GOALS(I.E. PRICE OF MEAL, MUSCLE GAINS, FAT LOSS, ETC.)################################################

############################ USER COULD SELECT TIME TO COMMENCE THE FASTING PERIOD AS A MEANS TO APPROXIMATE WHEN THE FAST WILL END. fOR EXAMPLE, IF ITS 2PM AND I WANT TO SEE WHEN I SHOULD BREAK MY FAST IF I START THE FAST AT 6PM THEN, DEPENDING ON THE PROTOCOL, IT SHOULD GIVE ME AN APPROXIMATE TIME OF WHEN I SHOULD BREAK MY FAST################################################

import datetime

####
# Add a try/except to allow user flexibility of how much to fast. Can be hours or days (if the latter then a warning will be included to warns against possibility of adverse effects of an exaggeretly long fast
####

protocol = ''

# If 'protocol' variable is anything but a, b or c then the loop will continue
while protocol.lower() != 'a' and protocol.lower() != 'b' and protocol.lower() != 'c':
    print('Enter fasting protocol to follow')
    print('A) 12 hours')
    print('B) 16 hours')
    print('C) 20 hours')
    protocol = input()

protocol = protocol.lower()

# Temporary menu
if protocol == 'a':
    protocol = datetime.timedelta(hours=12)

elif protocol == 'b':
    protocol = datetime.timedelta(hours=16)

elif protocol == 'c':
    protocol = datetime.timedelta(hours=20)


# Start date and time of the fast

# Figure out how to input the time with AM/PM for the sart of the fasting time
print('Do you wish to begin fast now or later?')
print('Enter zero (0) to begin now, otherwise enter the time in 12-hour format to begin fast')
while True:
    try:
        start = int(input('Begin @: '))

        if start > 12 or start < 1:
            print('Invalid 12-hour format')
            continue

        break
    except:
        print('Invalid input')
start = datetime.datetime.now()

# Print the start date as day of the week, month with day number, followed by hour and minutes in 12-hour notation
message = "start date is {:%A, %B %d, %I:%M %p}"

print(message.format(start))
