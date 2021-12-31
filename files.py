"""
Files in Python
open ur files for the shortest time possible
"""
"""
open the file for reading, 
print out the contents
asks user for the name
open the file for writing 
and write the user name into the file 
"""
my_file = open('data.txt', 'r') #open a file for reading only
#the operating system has stored somewhere in the memory that has its file open
file_content = my_file.read() #reads the contents of a file as a single string & assigns it to file_content

my_file.close()

print(file_content)

user_name = input('Enter your name: ')

my_file_writing = open('data.txt', 'w') #erases the contents of the file and anything we write will override
content = my_file_writing.write(user_name)

my_file_writing.close()
print(content)



