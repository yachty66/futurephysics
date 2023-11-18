with open('data.txt', 'r') as f:
    lines = f.readlines()

# Remove leading hyphen and space from each line
lines = [line.lstrip('- ') for line in lines]

# Write the modified lines back to the file
with open('data.txt', 'w') as f:
    f.writelines(lines)