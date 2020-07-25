# ^ Match the start of d line
# X = start of d line
# . match any character
# * many times
# :

##############################3
#Extracting data

import re
x = 'My 2 favorite number are 19 and 42'
y = re.findall ('[0-9]+', x)
print(y)

y = re.findall ('[AEIOU]+', x)
print(y)

#########################

# data is a email
y = re.findall('\S+@\S+', x)
print(y)

###########################

words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])

###########################
import re
lin = 'From cwen@iupui.edu Thu Jan  3 16:34:40 2008'
y =  re.findall ('@([^ ]*)', lin)
print (y)

##############################

import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand :
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM - Condidence: ([0-9]+)', line)
    num = float(stuff[0])
    numlist.append(num)

print('Maximum: ', max(numlist))


^	Matches the beginning of a line
$	Matches the end of the line
.	Matches any character
\s	Matches whitespace
\S	Matches any non-whitespace character
*	Repeats a character zero or more times
*?	Repeats a character zero or more times (non-greedy)
+	Repeats a character one or more times
+?	Repeats a character one or more times (non-greedy)
[aeiou]	Matches a single character in the listed set
[^XYZ]	Matches a single character not in the listed set
[a-z0-9]	The set of characters can include a range
(	Indicates where string extraction is to start
)	Indicates where string extraction is to end
