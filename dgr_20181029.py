"""
def thing():
    print("Hello")
    print("Fun")

thing()
print("Zip")
thing()


big = max("Hello world")
print(big)
w


print(float(99)/100)


i = 42
type(i)
f = float(i)
print(f)
type(f)
print(1 + 2 * float(3)/4-5)


sval = "123"
type(sval)
ival = int(sval)
type(ival)
print(ival + 1)
nsv = "hello bob"
niv = int(nsv)


x = 5
print("Hello")

def print_lyrics():
    print("I am a lumberjack, and i am okay.")
    print("I sleep all night and i work all day.")

print("Yo")
print_lyrics()
x = x + 2
print(x)


def greet(lang):
    if lang == "es":
        print("Hola")
    elif lang == "fr":
        print("Bonjour")
    else:
        print("Hello")
greet("en")
greet("es")
greet("fr")


def greet():
    return "Hello"

print(greet(),"Glenn")
print(greet(),"Sally")


def greet(lang):
    if lang == "es":
        print("Hola")
    elif lang == "fr":
        print("Bonjour")
    else:
        return "Hello"
print(greet("en"),"Glenn")
print(greet("es"),"Sally")
print(greet("fr"),"Michael")
"""

def addtwo(a, b):
    added = a + b
    return added

x = addtwo(3, 5)
print(x)
