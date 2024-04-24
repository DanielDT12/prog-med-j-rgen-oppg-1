# oppgave 1

myString = "This is a test" # Start string
myString += " " # myString = myString + " "
myString += "string" # Legger til "string" etter at det er lagt til " "

# print(myString)

x = 4
y = 10
z = y

x -= y # x = x - y === -6

# print(x)

# oppgave 2
### har prøvd et par av liste methodene.

myList = ["test", "list", "with", "strings"]
myListA = ["testA", "listA", "withA", "stringsA"]
myListB = ["testB", "listB", "withB", "stringsB"]
myListC = ["testC", "listC", "withC", "stringsC"]
myListD = ["testD", "listD", "withD", "stringsD", "stringsD", "stringsD", "stringsD", ]

myListA.append("extra") ### Legger til data i slutten av liste
myListB.clear() ### Tømmer liste for data


print(myList) ### printer bare en default liste i terminalen
print(myListA) ### printer listen med "extra" lagt til siden den har en append() over
print(myListB) ### printer et tomt array siden det er brukt en clear() method på den
print(myListC.index("withC")) ### Sjekker hvor denne stringen ligger i lista, "withC" ligger nummer 3 i listen men den printer 2 i terminalen, det er siden lister starter indexen på 0 istedet for 1
print(myListD.count("stringsD")) ### printer ut hvor mange av "stringsD" strings som er inne i listen i dette tilfellet er det 4 strings som er "stringsD"

# oppgave 3

minText = "Python is a high-level programming language known for its simplicity and versatility. It is widely used in various fields such as web development, data analysis, artificial intelligence, and scientific computing."

for text in minText:
    print(text)

for text in minText.splitlines():
    print(text)

for text in minText.split():
    print(text)

for i in range(0, 101):
    print(i)

### Hvis man skal printe tall fra 0 til 100, må vi spesifisere (0, 101) siden tallet null telles
### og 0 til 101 betyr start fra 0 og gå opp til 101 tall. 0 til 101 tall er 0 til 100.