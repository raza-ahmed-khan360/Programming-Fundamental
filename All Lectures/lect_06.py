#split() method

no1,no2= input("Enter 2 numbers comma separated:").split(",")
print(no1,no2)

dd,mm,yyyy=input("Enter date separated by/:").split("/")
print(dd,mm,yyyy)

text = "Hello World!"
print(text.split())

csv="apple,banana,dates"
print(csv.split(","))

data = "one,two,three,four,five"
print(data.split(",",3))

multiline = "line1\nline2\nline3"
print(multiline.split("\n"))

sentence = "Hello    how are you!"
print(sentence.split())

no1,no2= map(eval, input("Enter nos:").split())
print(no1+no2)

a=5
print("a=",a, sep="0000", end="\n\n")
print("a=",a, sep="0", end=" ")

f=open("D:\\BS-Software Engineering\\OneDrive - SSUET\\Attachments\\Programming Fundamental\\All Lectures\\first.txt", "w")
print("Hello World of Python", file=f)
f.close()

import time
print("Example with Flush")
for i in range(10):
    print("*", end=" ", flush=True)
    time.sleep(0.5)
print("\nDone")

print(eval("(2 % 2) + (2 * 2) - (2 / 2)"))