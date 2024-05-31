import os

#Setting path variables
path = "inputs/"
file_names = ["a", "b", "c"]

#Merging content of files
content = ""
for file_name in file_names:
  file = open(path+file_name+".txt", "r")
  content += file.read()+"\n"

#Writing content to new txt file
merged_file_path = "merged_file.txt"
merged_file = open(merged_file_path, "w")
merged_file.write(content)
merged_file.close()

#Informing the user of successful finishing of the script
print("The files have been merged into {}".format(merged_file_path))