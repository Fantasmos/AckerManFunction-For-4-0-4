import sys
import math

last_out = ''

def print(message):
   global last_out
   last_out = message
   msg = str(message).replace("- 3 + 3", '')
   sys.stdout.write(msg +'\n')

def StringOutputAckermansFunction (input1 ,input2):
 
   if (input1 == 0):
       print( str(input1) + "+ 1")
       return
   if (input2 == 0):
       StringOutputAckermansFunction(input1 - 1, 1)
       return
   if (input1 == 1):
       print (str(input2) + "+ 2")
       return
   if (input1 == 2):
       print ("(2 * " + str(input2) + ") + 3")
       return
   if (input1 == 3):
       if (input2 == None):
           print ("2^("+ last_out + " + 3)" + "- 3")
       else:
           print ("(2^( " + str(input2) + " + 3 ))" + "- 3")
      
       return
   if (input1 == 4):
       StringOutputAckermansFunction(input1 - 1, StringOutputAckermansFunction(input1, input2 - 1))
       return

for x in range (0, 5):
  
   StringOutputAckermansFunction(4, x)

   print("Answer when m is " + str(x) + " = " + last_out)
