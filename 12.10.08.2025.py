# Reading a text file
# read mode & write mode  & append mode
# 1. locate the file and tell which mode you want to connect
# 2. location: can be absolute location or relative
# 3. perform the operations
# 4. close the connection

file_handle = open("file1.txt","a+") # default mode is "r"
# write: write() writelines()
txt1 = '''Twinkle Twinkle Little Star
How I wonder 
What you are
Up Above the world
so high
'''
if file_handle.writable():
   file_handle.write(txt1)
else:
    print('Sorry, File cant be written')
file_handle.close()

file_handle = open("file1.txt","r")
if file_handle.readable():
    content = file_handle.readlines()
    print("readlines:\n",content)
    file_handle.seek(0)
    print("==========  READING THE CONTENT AS A SINGLE CONTENT")
    content = file_handle.read(35)
    print(content)
file_handle.close()
