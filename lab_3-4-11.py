# John Lennon, Paul McCartney, George Harrison, and Richard Starkey (better known as Ringo Starr).

# step 1
beatles = [] # create an empty list named beatles
print("Step 1:", beatles)

# step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison") # use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison
print("Step 2:", beatles)

# step 3
for member in range(2):
    beatles.append(input("Who else was in the band? Type their name: "))
print("Step 3:", beatles)

# step 4
del beatles[-1]
del beatles[-1] # use the del instruction to remove Stu Sutcliffe and Pete Best from the list
print("Step 4:", beatles)

# step 5
beatles.insert(0, "Ringo Starr") # use the insert() method to add Ringo Starr to the beginning of the list
print("Step 5:", beatles)

# testing list legth
print("The Fab", len(beatles))