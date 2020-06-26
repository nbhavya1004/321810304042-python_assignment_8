# 321810304042-python_assignment_8 


# Bhavyasree N - 321810304042


#     1.     Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string...

# type-1 :
	
def swap(a,b) :
	new_a = b[:3] + a[3:]
	new_b = a[:3] + b[3:]
	return new_a + '  ' + new_b
print(swap('abc','xyz'))

# type-2 :
	
def swap(a,b) :
  new_a = b[:2] + a[2:]
  new_b = a[:2] + b[2:]
  return new_a + ' ' + new_b
print(swap('abc', 'xyz'))





#     2.     Write a Python program to remove a newline in Python...

# type-1 :

str1 = "Python\n"
print(str1)
print(str1.strip())

# type-2 :

str1 = "Python\n"
print(str1)
print(str1.rstrip())





#     3.     Write a Python program to perform Deletion of a character...

# type-1 :

s1 = "Hello Python"
print(s1)
print(s1[:4] + s1[5:])

# type-2 :
	
s1 = "Python"
print(s1)
print(s1[:5])

# type-3 :

s1="apple"
print(s1)
print(s1[1:])





#     4.     Write a program to print every character of a string entered by user in a new line using loop...

s1="mango"
for i in s1:
	print(i)
	
	