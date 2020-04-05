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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
seen = []
count = 0
for text in texts:
    for i in range(2):
        if text[i] not in seen:
            seen.append(text[i])
            count += 1

for call in calls:
    for i in range(2):
        if call[i] not in seen:
            seen.append(call[i])
            count += 1

print('There are {} different telephone numbers in the records.'.format(count))


