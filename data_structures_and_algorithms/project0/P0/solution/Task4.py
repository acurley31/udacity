"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

all_outgoing = set()
all_others = set()
for call in calls:
    outgoing = call[0]
    answering = call[1]
    all_outgoing.add(outgoing)
    all_others.add(answering)

for text in texts:
    for i in range(2):
        all_others.add(text[i])

telemarketers = all_outgoing - all_others
telemarketers_list = sorted(telemarketers)
print('These numbers could be telemarketers: ')
for number in telemarketers_list:
    print(number)


