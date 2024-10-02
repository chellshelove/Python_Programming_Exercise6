# Get input string from the user
input_string = input("Enter a string: ")

# Initialize the compressed string and a count variable
compressed_string = ""
count = 1

# Loop through the string and compress
for i in range(1, len(input_string)):
    if input_string[i] == input_string[i - 1]:
        count += 1
    else:
        compressed_string += input_string[i - 1] + str(count)
        count = 1

# Add the last character and its count
compressed_string += input_string[-1] + str(count)

# Print the compressed string
print("Compressed string:", compressed_string)