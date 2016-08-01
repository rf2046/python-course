count = 0

while (count < 100):

  if count%15==0:
    print ("fizzbuzz")

  elif count%3==0:
    print ("fizz")

  elif count%5==0:
    print ("buzz")

  else: print ("%d" % (count))

  count += 1