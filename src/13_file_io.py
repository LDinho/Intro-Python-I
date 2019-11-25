"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE

with open('foo.txt', 'r') as foo:  # when using 'with', file is auto closed
    data = foo.read()
    print(data)
# foo.closed
# foo.close()
# foo.read()  # this will fail


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

with open("bar.txt", "w") as example:
    example.write("Python\n")
    example.write("may be \n")
    example.write("about a snake or coding.")
new_file = open("bar.txt")
data = new_file.read()
print(data)
new_file.close()

# print(new_file.read())
