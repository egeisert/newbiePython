#Basic tuple code
vowels = ('A', 'E', 'I', 'O', 'U')
print(vowels[0], vowels[1], vowels[2],vowels[3], vowels[4]) # Prints individual letters

#Next set of prints all print same output
#Prints as a tuple, not as a string
print(vowels)
print(vowels[0:])
print(vowels[:])

print(vowels[1:3]) #Prints only ('E', 'I')

#Prints each vowel to new line
#x is set to the value at each index 
for x in vowels:
    print(x,  end = " ") #end = " " changes the behavior to append " " instead of \n to string
print() # a way to clear the " " from end

#Typical iteration of index i
for i in range(len(vowels)):
    print(vowels[i])

complex = (0,  0+1j,  1,  1+1j)

print(complex)
print("x * x")
for x in complex:
    print(x*x,  end = " ") # prints the complex number times itself

print()

print(complex[0:]) # prints list forwards
print(complex[::-1]) # prints list backwards
