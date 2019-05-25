# add code snippet to save running config to a new file before comparision

# the files to be compared change to the config files for saved and running
filename1 = "doc1.txt"
filename2 = "doc2.txt"


f1 = open(filename1)
f2 = open(filename2)


print("*"*20)
print("Comparing files ", filename1, " with ", filename2, "\n")
print("*"*20)

# Reads the first line from the files
f1_line = f1.readline()
f2_line = f2.readline()

line_count = 1

# checks the file contents till EOF
while f1_line != '' or f2_line != '':

    # Strip the leading whitespaces
    f1_line = f1_line.rstrip()
    f2_line = f2_line.rstrip()


    if f1_line != f2_line:

        # If a line does not exist on file2 then mark the output with + sign
        if f2_line == '' and f1_line != '':
            print("file1+", "Line-" , line_count, f1_line)
        # otherwise output the line on file1 and mark it with ok
        elif f1_line != '':
            print("file1ok", "Line-" , line_count, f1_line)

        # If a line does not exist on file1 then mark the output with + sign
        if f1_line == '' and f2_line != '':
            print("file2+", "Line-" , line_count, f2_line)
        # otherwise output the line on file2 and mark it with ok
        elif f2_line != '':
            print("file2ok", "Line-" ,  line_count, f2_line)

    #Read the next line from the file
    f1_line = f1.readline()
    f2_line = f2.readline()


    #Increment line counter
    line_count = +1

# Close the files
f1.close()
f2.close()
