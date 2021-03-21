# Copying Lists using slicing lists 🤔;


animals = ['elephant', 'lion', 'tiger', "giraffe", "rhino","antelope", "leopard"]

copy_animals = animals[:] # used this line to copy the list by slicing the whole list using the [:] thus we can now make edits to the list  i.e below
copy_animals[0] ="Hyena" #😂😂😂, you gotta love lazy hyenas
print(" original animals list " ,animals) # output is ['elephant', 'lion', 'tiger', 'giraffe', 'rhino', 'antelope', 'leopard']
print(" Copied animals list " ,copy_animals) # output is ['Hyenas', 'lion', 'tiger', 'giraffe', 'rhino', 'antelope', 'leopard']