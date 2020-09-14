#sleep_in
#The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
#sleep_in(False, False) → True
#sleep_in(True, False) → False
#sleep_in(False, True) → True
def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False

#monkey_trouble
#We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
#monkey_trouble(True, True) → True
#monkey_trouble(False, False) → True
#monkey_trouble(True, False) → False
def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  if not a_smile and not b_smile:
    return True
  return False

#sum_double
#Given two int values, return their sum. Unless the two values are the same, then return double their sum.
#sum_double(1, 2) → 3
#sum_double(3, 2) → 5
#sum_double(2, 2) → 8
def sum_double(a, b):
  if a != b:
    return a+b
  if a == b:
    return (a+b)*2
  
#diff21
#Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
#diff21(19) → 2
#diff21(10) → 11
#diff21(21) → 0
def diff21(n):
  if n<21:
    if n-21 <0:
      return (n-21)*-1
    else:
      return n-21
  else:
    if n-21 <0:
      return (n-21)*-1*2
    else:
      return (n-21)*2


#parrot_trouble
#We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.
#parrot_trouble(True, 6) → True
#parrot_trouble(True, 7) → False
#parrot_trouble(False, 6) → False
def parrot_trouble(talking, hour):
  if (talking == True) and ((hour < 7) or (hour>20)):
    return True
  else:
    return False
  
#near_hundred
#Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
#near_hundred(93) → True
#near_hundred(90) → True
#near_hundred(89) → False  
def near_hundred(n):
  if (abs(100 - n) <= 10) or (abs(200 - n) <=10):
    return True
  else:
    return False
 
