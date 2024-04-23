""" 
3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
through 3-7 (pages 41–42), use len() to print a message indicating the number
of people you’re inviting to dinner.
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

print(len(guests))