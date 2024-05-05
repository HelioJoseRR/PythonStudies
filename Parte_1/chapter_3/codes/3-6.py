""" 
3-6. More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
•Start with your program from Exercise 3-4 or 3-5. Add a print() call to the
end of your program, informing people that you found a bigger table.
•Use insert() to add one new guest to the beginning of your list.
•Use insert() to add one new guest to the middle of your list.
•Use append() to add one new guest to the end of your list.
•Print a new set of invitation messages, one for each person in your list.
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

print(f"{guests[1].title()} bring the wine.")
print(f"{guests[3].title()} bring your enlightenment.")
print(f"{guests[4].title()} bring the bitcoins.")
print(f"{guests[0].title()} bring Di Caprio")
print(f"{guests[2].title()} YEAAAAAAAAAAAAAAAAAAAAH")
print(f"{guests[5].title()} COCORICO.")

