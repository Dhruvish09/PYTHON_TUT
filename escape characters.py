#This example use for print  word with 's
txt = 'It\'s alright.'
print(txt) 

txt = "This will insert one \\(backslash)."
print(txt) 

#Mostly use below escape

#This example print strings in new lines: 
# o/p:Hello
#     World!
txt = "Hello\nWorld!"
print(txt) 

#This example add TAB between two words: o/p:Hello   World!
txt = "Hello\tWorld!"
print(txt) 

#This example erases one character (backspace): o/p:HellWorld!
txt = "Hello\bWorld!"
print(txt) 

#A backslash followed by three integers will result in a octal value: o/p:Hello 
txt = "\110\145\154\154\157"
print(txt) 

#A backslash followed by an 'x' and a hex number represents a hex value: o/p:Hello 
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 
