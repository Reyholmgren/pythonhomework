# Write a program that takes a text file as a parameter. The text file contains strings, one per line. The program
# should read in the text file and write out a new text file named <file>-palindromes.txt that contains only the words
# that are palindromes (the same word forward and backward).

# Creating the text file with word list to sift through

file = open("original_list.txt", "w+")
file.write("idea\n")
file.write("dad\n")
file.write("sad\n")
file.write("madam\n")
file.write("turtle\n")
file.write("kayak\n")
file.write("civic\n")
file.write("solos\n")
file.close()

# Identifying palindromes and writing to new text file (palindrome_file)

palindrome_file = open("palindrome_list.txt", "w+")
with open('original_list.txt') as org_file:
    for line in org_file:
        line = line.strip()
        line2 = line[::-1]
        if line == line2:
            palindrome_file.write(line)
            palindrome_file.write("\n")
