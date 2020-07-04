file=open("yosapa.txt","r")
str=file.read()
print(len(str))

file=open("yosapa1.txt","r")
str1=file.read()
print(len(str1))

if str==str1:
    print("el texto coincide")
else:
    print("el texto no coincide")
file.close()
    









