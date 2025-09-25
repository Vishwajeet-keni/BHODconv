import BHODconv as Conv
re_run=""
def valid_input():
 global re_run
 x=input("Enter_proper_sufix_for_type_of_input_|"  
         "\n.bin: Binary      .eg(Enter-> 1011.bin)" 
         "\n.hex: Hexadecimal .eg(Enter-> A5.hex)"   
         "\n.oct: Octal       .eg(Enter-> 856.oct)"  
         "\n.dec: Decimal     .eg(Enter-> 245.dec)"  
         "\nInput: ").upper()
 # catching Error in input
 try:
     print("\n______________________________________"
           "\nInput_Error_Handler:"
           "\n--------------------------------------")
     if x.endswith(".BIN") or x.endswith(".HEX") or x.endswith(".OCT") or x.endswith(".DEC"):
         print("Valid Input")
         re_run=""
     else:
         re_run=input("Invalid Input"
                      "\nCode Terminated"
                      "\n--------------------------------------"
                      "\nWant to run the program again(Y/N):").upper()
 finally:
     if re_run=="Y":
        print("Re running program..."
              "\n______________________________________")
        x=valid_input()
        return x 
     elif re_run=="N":
          print("Exiting program..."
                "\n______________________________________")
     else:
        print("______________________________________")
        return x
def valid_required_output(x):
 global re_run
 if x.endswith(".BIN"):
     y=input("\nEnter_type_of_output_you_require_|" 
             "\n.hex: Hexadecimal .eg(Enter-> .hex)"
             "\n.oct: Octal       .eg(Enter-> .oct)"
             "\n.dec: Decimal     .eg(Enter-> .dec)"
             "\nOutput: ").upper()
 elif x.endswith(".HEX"):
    y=input("\nEnter_type_of_output_you_require__|" 
            "\n.bin: Binary      .eg(Enter-> .bin)"
            "\n.oct: Octal       .eg(Enter-> .oct)"
            "\n.dec: Decimal     .eg(Enter-> .dec)"
            "\nOutput: ").upper()
 elif x.endswith(".OCT"):
    y=input("\nEnter_type_of_output_you_require__|" 
            "\n.bin: Binary      .eg(Enter-> .bin)"
            "\n.hex: Hexadecimal .eg(Enter-> .hex)"
            "\n.dec: Decimal     .eg(Enter-> .dec)"
            "\nOutput: ").upper()
 elif x.endswith(".DEC"):
    y=input("\nEnter_type_of_output_you_require__|" 
            "\n.bin: Binary      .eg(Enter-> .bin)"
            "\n.hex: Hexadecimal .eg(Enter-> .hex)"
            "\n.oct: Octal       .eg(Enter-> .oct)"
            "\nOutput: ").upper()
# catching Error in required ourput request
 try:
     print("\n___________________________________"
          "\nRequired_Output_Error_Handler:"
          "\n-----------------------------------")
     if y.endswith(".BIN") or y.endswith(".HEX") or y.endswith(".OCT") or y.endswith(".DEC"):
        print("Valid Input")
        re_run=""
     else:
        re_run=input("Invalid Input"
                     "\nCode Terminated"
                     "\n-----------------------------------"
                     "\nWant to run the program again(Y/N):").upper()
 finally:
     if re_run=="Y":
        print("Re running program..."
              "\n___________________________________")
        y=valid_required_output(x)
        return y 
     elif re_run=="N":
          print("Exiting program..."
                "\n___________________________________")
     else:
        print("___________________________________")
        return y
def required_output(x,y):
#bin-->hex,oct,dec
 if x.endswith(".BIN") and y==".HEX":
     x=(x[:-4]) #removes last 3 terms
     y=Conv.B2H(x)
     print(f"\nYour Input: {x}.bin      \
             \nRequired Output: {y}.hex")
 elif x.endswith(".BIN") and y==".OCT":
     x=(x[:-4])
     y=Conv.B2O(x)
     print(f"\nYour Input: {x}.bin      \
             \nRequired Output: {y}.oct")
 elif x.endswith(".BIN") and y==".DEC":
     x=(x[:-4])
     y=Conv.B2D(x)
     print(f"\nYour Input: {x}.bin      \
             \nRequired Output: {y}.dec")
        
#hex-->bin,oct,dec
 elif x.endswith(".HEX") and y==".BIN":
     x=x[:-4]
     y=Conv.H2B(x)
     print(f"\nYour Input: {x}.hex      \
             \nRequired Output: {y}.bin")
 elif x.endswith(".HEX") and  y==".OCT":
     x=x[:-4]
     y=Conv.H2O(x)
     print(f"\nYour Input: {x}.hex      \
             \nRequired Output: {y}.oct")
 elif x.endswith(".HEX") and  y==".DEC":
     x=x[:-4]
     y=Conv.H2D(x)
     print(f"\nYour Input: {x}.hex      \
             \nRequired Output: {y}.dec")
        
#oct-->bin,hex,dec
 elif x.endswith(".OCT") and y==".BIN":
     x=x[:-4]
     y=Conv.O2B(x)
     print(f"\nYour Input: {x}.oct      \
             \nRequired Output: {y}.bin")
 elif x.endswith(".OCT") and  y==".HEX":
     x=x[:-4]
     y=Conv.O2H(x)
     print(f"\nYour Input: {x}.oct      \
             \nRequired Output: {y}.hex")
 elif x.endswith(".OCT") and  y==".DEC":
     x=x[:-4]
     y=Conv.O2D(x)
     print(f"\nYour Input: {x}.oct      \
             \nRequired Output: {y}.dec")
        
#dec-->bin,hex,oct
 elif x.endswith("DEC") and y==".BIN":
     x=x[:-4]
     y=Conv.D2B(x)
     print(f"\nYour Input: {x}.dec      \
             \nRequired Output: {y}.bin")
 elif x.endswith("DEC") and  y==".HEX":
     x=x[:-4]
     y=Conv.D2H(x)
     print(f"\nYour Input: {x}.dec      \
             \nRequired Output: {y}.hex")
 elif x.endswith("DEC") and  y==".OCT":
     x=x[:-4]
     y=Conv.D2O(x)
     print(f"\nYour Input: {x}.dec      \
             \nRequired Output: {y}.oct")

x=valid_input()
y=valid_required_output(x) 
required_output(x,y)

re_run=str(input("--------------------------------------"
             "\nWant to run the program again?(y/n): ").lower())
print("___________________________________")
if re_run=="y":
    x=valid_input()
    y=valid_required_output(x) 
    required_output(x,y)
