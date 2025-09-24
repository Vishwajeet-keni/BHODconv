# Main Functions 
def D2B(D): # Decimal to Binary
    D=int(D) 
    if D==0:
     return"0"
    B=""
    while D>0:
        rem=D%2  #remainder
        B=str(rem)+B
        D//=2
    return B
def B2D(B): # Binary to Decimal 
   D=0 
   pow=0 #power
   for bit in reversed(B):
      D+=int(bit)*(2**pow)
      pow+=1
   return D
def B2H(B): # Binary to Hexadecimal
   while (len(B)%4)!=0:
       B="0"+B
   H=""
   Hb="0123456789ABCDEF"
   for i in range(0,len(B),4):
      val=B2D(B[i:i+4])  # grouping 4 element then runing it throught B2D
      H+=Hb[val]
   return H
def B2O(B): # Binary to Octal 
   while (len(B)%3)!=0:
       B="0"+B
   O=""
   for i in range(0,len(B),3):
      oDig=str(B2D(B[i:i+3])) # grouping 3 element and pushing through B2D
      O+=oDig
   return O
def H2B(H): # Hexadecimal to Binary
   B=""
   hMap={"0":"0000","1":"0001","2":"0010","3":"0011",
         "4":"0100","5":"0101","6":"0110","7":"0111",
         "8":"1000","9":"1001","A":"1010","B":"1011",
         "C":"1100","D":"1101","E":"1110","F":"1111"}
   for digit in H.upper():
      B+=hMap[digit]
   return B 
def O2B(O): # Octal to Binary
   B=""
   oMap={"0":"000","1":"001","2":"010","3":"011",
         "4":"100","5":"101","6":"110","7":"111",}
   for digit in O:
      B+=oMap[digit]
   return B
# Sub Function
def D2H(D): # Decimal to Hexadecimal
   H=B2H(D2B(D))
   return H
def D2O(D): # Decimal to Octal
   O=B2O(D2B(D))
   return O
def H2D(H): # Hexadecimal to Decimal 
   D=B2D(H2B(H))
   return D
def O2D(O): # Octal to Decimal
   D=B2D(O2B(O))
   return D
def H2O(H): # Hexadecimal to Octal
   O=B2O(H2B(H))
   return O
def O2H(O): # Octal to Hexadecimal 
   H=B2H(O2B(O))
   return H