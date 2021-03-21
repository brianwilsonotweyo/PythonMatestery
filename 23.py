# Slicing Lists🔪⚔🗡

# here you specify where you'd like to start the slice and where you'd like the slicing to end 🍰🍕
animals = ['elephant', 'lion', 'tiger', "giraffe", "rhino","antelope", "leopard"]

print(animals[1:4]) # this will slice the indexes between 1 and 4 and will only print out everthing in between with index 1 included and 4 left out i.e output will be ['lion', 'tiger', 'giraffe']
print(animals[1:]) # this slices from index 1 and leaves index 0 out with everthing else after 1 included out put is ['lion', 'tiger', 'giraffe', 'rhino', 'antelope', 'leopard']
#we can also reverse the slice from right to left i.e 
print(animals[-5:]) #this starts from index -5  which is "lion " in the reverse order and prints out every element after it i.e out put is ['tiger', 'giraffe', 'rhino', 'antelope', 'leopard'] 
