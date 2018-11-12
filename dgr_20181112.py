"""
fhand = open("mbox.txt")
print(fhand)


stuff = "Hello\nWorld!"
stuff
"Hello\nWorld!"
print(stuff)
stuff ="X\nY"
print(stuff)
len(stuff)


xfile = open("mbox.txt")
for cheese in xfile:
    print(cheese)


fhand = open("mbox.txt")
count = 0
for line in fhand:
    count = count + 1
print("Line Count:", count)


fhand = open("mbox-short.txt")
inp = fhand.read()
print(len(inp))
print(inp[:20])


fhand = open("mbox-short.txt")
for line in fhand:
    if line.startswith("j:"):
        print(line)
"""

fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()

count = 0
for line in fhand:
    if line in fhand:
        if line.startswith("Subject:"):
        count = count + 1
print("There were", count, "subject line in", fname)
