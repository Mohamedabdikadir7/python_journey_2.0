text_file = open('/home/mohamedabdikadir/development/code/phase_3/python_folder/file_name.txt', 'w')
text_file.write("Hello, World!\n")
text_file.close()

## using with it opens and closes automatically
with  open("/home/mohamedabdikadir/development/code/phase_3/python_folder/file.txt" , 'w') as textfile:
 textfile.write("abdi is good boy")
##   If a file already exists and we use the mode='w' the file will be overwritten.
with  open("/home/mohamedabdikadir/development/code/phase_3/python_folder/file.txt" , mode='w' ) as textfile:
 textfile.write("abdi is bad boy")

 r = open('/home/mohamedabdikadir/development/code/phase_3/python_folder/r.txt' , 'w') 
 r.write(" r is written")
 r.close()

 with open('/home/mohamedabdikadir/development/code/phase_3/python_folder/t.txt' , 'w') as t:
  t.write(" t is going home")

 with open('/home/mohamedabdikadir/development/code/phase_3/python_folder/t.txt' , mode='w') as t:
  t.write("t is not  going home")
with open('/home/mohamedabdikadir/development/code/phase_3/python_folder/t.txt','r') as f:
 content = f.read()
print(content)
with open('/home/mohamedabdikadir/development/code/phase_3/python_folder/t.txt', 'r') as f:
    # Read the content of the file
    content = f.read()
    # Print the content
    print(content)