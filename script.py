var1 = 100
if var1:
   print "1 - Got a true expression value"
   print var1
else:
   print "1 - Got a false expression value"
   print var1

var2 = 0
if var2:
   print "2 - Got a true expression value"
   print var2
else:
   print "2 - Got a false expression value"
   print var2

print "Good bye!"

var = 100
if var == 200:
    print '1 - Got a true expression value'
    print var
elif var == 150:
    print '2 - Got a true expression value'
    print var
elif var == 100:
    print '3 - Got a true expression value'
    print var
else:
    print '4 - Got a false expression value'
    print var

print 'Good bye!'
    

'''count = 0
while count < 9:
    print 'The count is: ' , count
    count = count + 1

print 'Good bye'

var = 1
while var == 1:
    num = raw_input('Enter a number: ')
    print 'You entered: ', num 
print 'Goode bye!'
'''


count = 0
while count < 5:
    print count, ' is less tha 5'
    count += 1
else:
    print count, ' is not less than 5'