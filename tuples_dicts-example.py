school_class = {} # create an empty dictionary for the input data; the student's name is used as a key, while all the associated scores are stored in a tuple (the tuple may be a dictionary value - that's not a problem at all)

while True: # enter an "infinite" loop (don't worry, it'll break at the right moment)
    name = input("Enter the student's name: ") # read the student's name here
    if name == '': # if the name is an empty string ()
        break # leave the loop
    
    score = int(input("Enter the student's score (0-10): ")) # ask for one of the student's scores (an integer from the range 0-10)
    if score not in range(0, 11): # if the score entered is not within the range from 0 to 10
	    break # leave the loop
    
    if name in school_class: # if the student's name is already in the dictionary
        school_class[name] += (score,) # lengthen the associated tuple with the new score (note the += operator)
    else:
        school_class[name] = (score,) # if this is a new student (unknown to the dictionary), create a new entry - its value is a one-element tuple containing the entered score
        
for name in sorted(school_class.keys()): # iterate through the sorted students' names
    adding = 0 # initialize the data needed to evaluate the average (sum and counter)
    counter = 0
    for score in school_class[name]: # we iterate through the tuple,
        adding += score # taking all the subsequent scores and updating the sum,
        counter += 1 # together with the counter
    print(name, ":", adding / counter) # evaluate and print the student's name and average score