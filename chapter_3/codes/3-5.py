"""
3-5. Changing Guest List: You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.
•Start with your program from Exercise 3-4. Add a print() call at the end of
your program, stating the name of the guest who can’t make it.
•Modify your list, replacing the name of the guest who can’t make it with the
name of the new person you are inviting.
•Print a second set of invitation messages, one for each person who is still in
your list.
"""

guests = []

guests.append('jesus')
guests.append('van gogh')
guests.append('daniel fraga')

print(guests)

print(f"{guests.pop(1).title()} can't come")

guests.insert(1, 'buda')

print(guests)
print(f"{guests[0].title()} bring the wine.")
print(f"{guests[1].title()} bring your enlightenment")
print(f"{guests[2].title()} bring the bitcoins")


