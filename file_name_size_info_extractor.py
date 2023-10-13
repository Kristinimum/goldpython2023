import os
file_info = []
current_dir = os.getcwd()

for file in os.listdir(current_dir):
    file_location = os.path.realpath(file)
    file_size = os.path.getsize(file)
    file_info.append({'path': file_location, 'size': file_size})
    
print(*file_info, sep='\n')
print(current_dir)

