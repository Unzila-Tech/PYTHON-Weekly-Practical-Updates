# Read first file
with open("file1.txt", "r") as file:
    lines1 = file.readlines()

# Read second file
with open("file2.txt", "r") as file:
    lines2 = file.readlines()

# Find middle line of first file
middle = len(lines1) // 2

# Find last line of second file
last = len(lines2) - 1

# Swap the lines
lines1[middle], lines2[last] = lines2[last], lines1[middle]

# Write updated content to first file
with open("file1.txt", "w") as file:
    file.writelines(lines1)

# Write updated content to second file
with open("file2.txt", "w") as file:
    file.writelines(lines2)

print("Contents swapped successfully.")

print("\nFirst file after swapping:")
for line in lines1:
    print(line, end="")

print("\nSecond file after swapping:")
for line in lines2:
    print(line, end="")