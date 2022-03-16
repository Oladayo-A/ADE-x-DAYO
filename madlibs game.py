print("I visited the prestigious Wonder Flora")
print("This garden have proven to be one of the best tourist centres in the world")
print("From the beautiful waterfall at the entrance to the little zoo on the inside")
print("A lot of beautiful flowers in their collection. Yellow Sunflowers, red roses,")
print("yellow dandelions, blue lobelias, golden yellow daffodils, golden tulips ...")
print("My Oh My, I love flowers. I wish i could visit this garden everyday. ")
print()
print("Complete the sentences with the correct option")
print('1. red   blue   green')
print("2. Lobelias   Dandelions   Sunflowers")
print("3. Flowers   Games   Money")
print('')
print("Note: Your answer should be as it is provided in the options")
print("The first letter in upper case and the rest in lower case")
print("")
print("Roses are ____")
print("_____ are blue")
print("I love ______ ")
print()
while True:
    colour = input("Choose a colour: ")
    if colour.lower()=="red":
        break
    else:
        print("Error!!! Try Again")

while True:
    flower = input("Choose a flower: ")
    if flower=="Lobelias":
        break
    else:
        print("Error!!! Try Again")

while True:
    name = input("Choose best option: ")
    if name=="Flowers":
        break
    else:
        print("Error!!! Try Again")
        continue
print()
print("Roses are " + colour.lower())
print(flower + " are blue")
print("I love " + name)
print("\n")
print("Congrats for passing the test")




