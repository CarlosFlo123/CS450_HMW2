'''--------------------------------------------------------------------------
Author: Carlos Flores Valero
Northwestern Polytechnic University, Fremont, CA
Date: 10/06/2019
---------------------------------------------------------------------------'''
#Ex1__________________________________________________
def fancy_printing(n):
  print(0)
  for i in range (1,26):  #Specified Range
    if (i%n == 0 or i == 1):
      print("Buzz!")
    else:
      print(i)

#fancy_printing(5)


#Ex2 __________________________________________________
def sum_num(n):
  if (n <= 0):  #Recursion --> Stop condition
    return 0
  else:
    return n + sum_num(n - 2)

#sum_num(4)
#sum_num(5)


#Ex3 __________________________________________________
def is_prime(n):
  i = n -1
  while(i > 1):
    if (n % i == 0):
      return False
    i -= 1
  return True
def cnt_primes(m):
  if (m <= 1):   #Recursion --> Stop Condition
    return 0
  elif(is_prime(m)):
      return (1 + cnt_primes(m-1))
  else:
    return (cnt_primes(m-1))

#cnt_primes(6)


#Ex4___________________________________________________
#not finished, gotta reinforce high ordr function concept
def incr(n):
  return (n + 1)
def triple(x):
  return (3*x)
def square(x):
  return (x*x)
def foo(f, n):
  def h(x):
    return f(x)
  if (n == -1):
    return 0
  else:
    return h + foo(f,n-1)

#foo(triple, 5)(1)



#Ex5___________________________________________________
def op(a, b, c):
  if ((b == 0 and c == 0) or (a == 0 and c == 0) ):
    return 0
  elif(a != 0 and b != 0):
    return (a + op(a, b-1, c))
  elif(c != 0):
    return (1 + op(a, b, c-1))

#op(2, 4, 3)
#op(0, 3, 2)
#op(3, 0, 2)


#Ex6___________________________________________________
def checking(x):
  if (x < 10):
      return True
  while (x > 1):
    tmp = x % 10
    x = x / 10
    if(tmp < x%10):
      return False
  return True

#checking(5)
#checking(11)
#checking(127)
#checking(1357)
#checking(21)
#checking(1375)


#Ex7___________________________________________________
def cal(n):
  if (n == 1):    #REcursion->Stop condition
    return 1
  elif (n == 0):  #Recursion->Stop condition
    return 0
  else:
    return n * cal(n - 2)

#cal(5)
#cal(8)


#Ex8___________________________________________________
''' itscts(f, x):
  def h(x):
    return lambda (f(x) == h(x)): True, False
  return h


at3 = itscts(square,3)
at3(triple)

#Ex9___________________________________________________
def A(n):
  if (n <= 3):
    return n
  else:
    return 1+1 * A(n-1)

A(1)
A(2)
A(3)
A(4)
'''

#Ex10___________________________________________________
def scanDigits(x):
  while (x > 1):
    if (x%10 == 7):
      return True
    x = int(x/10)
  return False

def bnc_bck_frth(k):
  index = 0
  goBack = 1
  i = 0
  while(index != k):
    index = index + 1
    if (goBack == 1):
      i = i + 1
    else:
      i = i - 1
    if (index % 7 == 0 or scanDigits(index)):
      goBack = goBack * (-1)
  return i

#bnc_bck_frth(7)
#bnc_bck_frth(8)
#bnc_bck_frth(15)
#bnc_bck_frth(21)
#bnc_bck_frth(22)
#bnc_bck_frth(30)
#bnc_bck_frth(68)
#bnc_bck_frth(69)
#bnc_bck_frth(70)
#bnc_bck_frth(71)
#bnc_bck_frth(72)
#bnc_bck_frth(100)
