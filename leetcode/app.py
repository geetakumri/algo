# read a file

my_file = open('data.txt', 'r')
file_content = my_file.read()

my_file.close()

print(file_content)

# write in a file - overwrite the exisy=ting file content
user_name = input('Enter you name : ')

my_file_writing = open('data.txt','w')
my_file_writing.write(user_name)

my_file_writing.close()

