""" 
3-7. Shrinking Guest List: You just found out that your new dinner table won’t
arrive in time for the dinner, and now you have space for only two guests.
•Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
•Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print a
message to that person letting them know you’re sorry you can’t invite them
to dinner.
•Print a message to each of the two people still on your list, letting them
know they’re still invited.
•Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end of
your program.
"""

guests = []

guests.append('jesus')
guests.append('van gogh')
guests.append('daniel fraga')

print(guests)

print(f"{guests.pop(1).title()} can't come")

guests.insert(1, 'buda')

print(guests)

print("I found a bigger table, new guests will be invited!")

guests.insert(0, "urso")
guests.insert(2, "pato")
guests.append('galinha')

print(f"{guests[0].title()} bring Di Caprio")
print(f"{guests[3].title()} bring your enlightenment.")
print(f"{guests[4].title()} bring the bitcoins.")
print(f"{guests[1].title()} bring the wine")
print(f"{guests[2].title()} YEAAAAAAAAAAAAAAAAAAAAH")
print(f"{guests[5].title()} COCORICO.")

print("I can invite only two people for dinner.")

print(f"{guests.pop().title()} You are out!!")
print(f"{guests.pop().title()} You are out!!")
print(f"{guests.pop().title()} You are out!!")
print(f"{guests.pop().title()} You are out!!")

print(f"{guests[0].title()} bring Di Caprio")
print(f"{guests[1].title()} bring the wine")

del guests[1]
del guests[0]

print(guests)