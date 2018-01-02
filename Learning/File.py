# f = open('1.xtx', 'w', encoding='utf8')
# f = open('1.xtx', 'a', encoding='utf8')
f = open('1.xtx', 'r/ r+(r,w)/ w+(w,r)/a+(a,r)', encoding='utf8')
# f.read(3)
# f.write("abc")
# f.readlines()  # Read all of file and return a List with keeping '\n' .etc
for i in f:
    print(i)    # Suggest that using this way to read file line y line. It's iterator
# string .strip .lstrip .rstrip will delete the '\n', '\t' , '\r', ' '
f.tell()    # output the position of pointer, add 1 for a figure and 3 for chinese character
# May be affected by encoding
f.seek(0)   # Back to the start
f.flush()
print("abc", end='', flush=True)
f.truncate()    # What's this? Google it.
f.close()
with open("1.txt", 'r') as f_read, open("2.txt, 'w'") as f_write:
    for line in f_read
        f_write.write(line)


