import random
lst = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l"]
p1 = str(random.choice(lst))
p2 = str(random.choice(lst))
p3 = str(random.choice(lst))
p4 = str(random.choice(lst))
p5 = str(random.choice(lst))
p6 = str(random.choice(lst))
p7 = str(random.choice(lst))
p8 = str(random.choice(lst))
p9 = str(random.choice(lst))
p10 = str(random.choice(lst))
p11 = str(random.choice(lst))
p12 = str(random.randint(-10, 10))
print(p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12)
q = input("Would you like to keep this? ")
if q == "yes":
    wut = input("What is this password for? ")
    f = open("pw.txt", "a")
    f.write("\n\n" + wut + ": " + p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12)
    f.close()
    #finished
