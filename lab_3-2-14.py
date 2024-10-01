blocks = int(input("Enter the number of blocks: "))

height = 0 # the height is measured by the number of fully completed layers

while blocks > height: # if the builders don't have a sufficient number of blocks and cannot complete the next layer,
    height += 1
    blocks += 1 # increments the number of blocks the builders have
    
else:
    pass # they finish their work immediately

print("The height of the pyramid:", height) # outputs the height of the pyramid that can be built using the blocks
