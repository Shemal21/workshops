__author__ = 'jc350024'
temp_file = open ("temp.txt", "w")

print ("first line", file=temp_file)
print ("second line", file=temp_file)
print ("third line", file=temp_file)
print ("fourth line", file=temp_file)
print ("SHEMAL IS AWESOME \m/", file=temp_file)
temp_file.close()
print('===')
print()
temp_file = open("temp.txt", "r")
for line in temp_file:
    line = line.strip()
    print (line)
temp_file.close()
print('===')
temp_file=open("temp.txt", "r")
my_str = temp_file.read()
print(my_str)
temp_file.close()

print('===')
temp_file = open("temp.txt", "r")
lines = temp_file.readlines()
print(lines)
temp_file.close()

print('===')
my_list = ['first line\n', 'second line\n', 'third line\n', 'fourth line\n', 'SHEMAL IS AWESOME \\m/\n']
out_file = open("out.txt", "w")
out_file.writelines(my_list)
out_file.close()


