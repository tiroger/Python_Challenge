import csv
import os
import re

# Creating the file path for the data file
file_path = os.path.join('..', 'raw_data', 'paragraph_1.txt')

# Opening and reading the text file
text_file = open(file_path, 'r')
read_text = str(text_file.read())

# Splitting the string into a list of words using space as delimiter
word_list = read_text.split(' ')

# Splitting the string into a list of sentences using ./?/! as delimiter
sentence_list = re.split("(?<=[.!?]) +", read_text)

# Calculating the lenght of each list
aprox_word_count = len(word_list)
aprox_sentence_count = len(sentence_list)

word_lengths = []
sentence_lengths = []

for i in range(len(word_list)):
	word_lengths.append(len(word_list[i]))

for sentence in sentence_list:
        words = sentence.split(' ')
        sentence_lengths.append(len(words))

# Calculating the average sentence length
avg_sentence_length = round(sum(sentence_lengths) / len(sentence_lengths), 1)

# Calculating the average word length
avg_word_len = round(sum(word_lengths) / len(word_lengths), 1)

# Printing results table
print("Paragraph Analysis")
print("------------------------------")
print("Approximate Word Count: " + str(aprox_word_count))
print("Approximate Sentence Count: " + str(aprox_sentence_count))
print("Average Letter Count: " + str(avg_word_len))
print("Average Sentence Length: " + str(avg_sentence_length))
print("------------------------------")

# Creating the output path for the txt file
output_path = os.path.join('..', 'Output', 'pyparagraph_analysis.txt' )

# Open the output file using "write" mode. 
# Specify the variable to hold the contents
with open(output_path, 'w', newline='') as paragraph_analysis:

    # Write the desired text
    paragraph_analysis.writelines("Paragraph Analysis" +'\n')
    paragraph_analysis.writelines("------------------------------" +'\n')
    paragraph_analysis.writelines("Approximate Word Count: " + str(aprox_word_count) +'\n')
    paragraph_analysis.writelines("Approximate Sentence Count: " + str(aprox_sentence_count) +'\n')
    paragraph_analysis.writelines("Average Letter Count: " + str(avg_word_len) +'\n')
    paragraph_analysis.writelines("Average Sentence Length: " + str(avg_sentence_length) +'\n')
    paragraph_analysis.writelines("------------------------------" +'\n')

# Opening the output file in r mode and printing to terminal
with open(output_path, 'r') as readfile:
    print(readfile.read())

