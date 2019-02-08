import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
def prior_decision():
   print("When players don't know eachother they decide spontaneously.")
   plt.figure(1)
   plt.subplot(121)
   plt.title('Peter')
   plt.xlabel('x')
   plt.ylabel('alpha')
   t = np.arange(0.0, 1.0, 0.01)
   s = -0.5*np.cos(np.pi*t)+0.5
   line, = plt.plot(t, s, lw=2)
   plt.ylim(-1.3,1.3)
   plt.grid(True)
   plt.subplot(122)
   plt.title('Paul')
   plt.xlabel('y')
   plt.ylabel('beta')
   t = np.arange(0.0, 1.0, 0.01)
   s = np.sin(0.5*np.pi*t)
   line, = plt.plot(t, s, lw=2)
   plt.ylim(-1.3,1.3)
   plt.grid(True)
   plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,wspace=0.35)
   plt.show()

#--------------------------------
#--------------------------------
#--------------------------------
def optimal():
   print("when Peter starts the game his threshold will be smaller than Paul's.")
   c=5
   def integrand(y, a, x):
       return (1+((1-(np.sin(a*y)))+(c+1)*np.sign(x-y)*(np.sin(a*y))))

   a = 0.5*np.pi
   x = 0.01
   k=range(0,10,1)
   l=np.zeros(10)
   m=0
   for x in k:
      I,err = quad(integrand, 0, 1, args=(a,x*0.1))
      print('x:','{0:2f}'.format(x*0.1),' Q:','{0:2f}'.format(I))
      l[m]=I
      m=m+1
      if(l[m-1]<0):
         n=m
   p0=(n-1)*0.1
   print('n::',n,'\nx*:','{0:3f}'.format(p0))    
   #-----------------------------------------------------------------
   p=(1/(2*(c+1)))*(p0*(c+2)+c)
   print('y*:','{0:3f}'.format(p))   

#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
def payoff():
    print("Payoff:\nUsing b* we find Paul's minimal loss.\nPeter's strtegy:Maximizing the minimal loss of Paul.")
    print("a*&b* shows that payoff for the first player will be negative.")
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
print('-------Poker_Chapter5_Vladimir Mazalov-------')
print('-------Programming_By_Yousef-----------------')
print('Please write your question number or exit(e).')
question_num=input("1-What is prior decision?\n2-what is optimal?\n3-Explaine about payoff?\n")
print('question_num:',question_num,'\n')
#-----------------------------------------------------------------------
while(question_num!='e'):
    os.system("clear")
    if(question_num=='1'):
      prior_decision()
      print("**************************************************************************************")
      print("...********************************************************************************...")
      print("**************************************************************************************")
      question_num=input("1-What is prior decision?\n2-what is optimal?\n3-Explaine about payoff?\n")
    elif(question_num=='2'):
      optimal()
      print("**************************************************************************************")
      print("...********************************************************************************...")
      print("**************************************************************************************")
      question_num=input("1-What is prior decision?\n2-what is optimal?\n3-Explaine about payoff?\n")
    elif(question_num=='3'):
      payoff()
      print("**************************************************************************************")
      print("...********************************************************************************...")
      print("**************************************************************************************")
      question_num=input("1-What is prior decision?\n2-what is optimal?\n3-Explaine about payoff?\n")



      
