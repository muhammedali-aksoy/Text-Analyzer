#Ask the user to enter a text
user_text=input("Enter a text:")
#Calculate the number of the characters
number_characters=len(user_text)
#Calculate the number of the words
number_words=len(user_text.split())
#Print the results
print("Number of characters:",number_characters)
print("Number of words:",number_words)