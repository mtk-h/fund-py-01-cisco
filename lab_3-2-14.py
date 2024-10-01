blocks = int(input("Enter the number of blocks: "))

height = 0 # the height is measured by the number of fully completed layers
layer = 0

while layer < blocks: # if the builders don't have a sufficient number of blocks and cannot complete the next layer,
    layer += 1
    blocks -= height # increments the number of blocks the builders have
    height += 1
    
# else:
#     pass # they finish their work immediately

print("The height of the pyramid:", height) # outputs the height of the pyramid that can be built using the blocks
