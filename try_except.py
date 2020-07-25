num = input ('Enter num')
try :
  ival = int(num)
except :
  ival = -1

if ival > 0 :
  print ('nice work')
else :
  print ('not num')
