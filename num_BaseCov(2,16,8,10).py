import BHODconv as Conv

x=input("Enter_proper_sufix_for_type_of_input_|"  \
      "\n.bin: Binary      .eg(Enter-> 1011.bin)" \
      "\n.hex: Hexadecimal .eg(Enter-> A5.hex)"   \
      "\n.oct: Octal       .eg(Enter-> 856.oct)"  \
      "\n.dec: Decimal     .eg(Enter-> 245.dec)"  \
      "\nInput: ").upper()
if x.endswith("BIN"):
    x=(x[:-4]) #removes last 3 terms 
    y=input("\nEnter_type_of_output_you_require_|" \
            "\n.hex: Hexadecimal .eg(Enter-> .hex)"\
            "\n.oct: Octal       .eg(Enter-> .oct)"\
            "\n.dec: Decimal     .eg(Enter-> .dec)"\
            "\nOutput: ").upper()
    if y==".HEX":
        y=Conv.B2H(x)
        print(f"\nYour Input: {x}.bin      \
                \nRequired Output: {y}.hex")
    elif y==".OCT":
        y=Conv.B2O(x)
        print(f"\nYour Input: {x}.bin      \
                \nRequired Output: {y}.oct")
    elif y==".DEC":
        y=Conv.B2D(x)
        print(f"\nYour Input: {x}.bin      \
                \nRequired Output: {y}.oct")