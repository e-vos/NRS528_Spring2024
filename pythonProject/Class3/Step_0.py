
#####
# Step 0 - Practice tasks before we start.
#####

# Express these items as a list using list append (i.e. .append) and print it:

item1 = "data1.txt"
item2 = "data2.txt"
item3 = "data3.txt"

all_items = []

all_items.append(item1)
all_items.append(item2)
all_items.append(item3)

# Print out how many files are in the list? Hint, we can use len(NAME OF YOUR LIST)

print(len(all_items))

# Take this list of files (file_list), and using a for loop, go through each file name and add
# a new file extension (.csv) and print new_extension_file_list.

new_extension_file_list = []

for i in all_items:
    new_extension_file_list.append(i + ".csv")

print(new_extension_file_list)
