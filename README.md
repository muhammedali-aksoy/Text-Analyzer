# 📝 Text Analyzer

**Created:** 17 August 2025  

A simple Python program that counts the number of **characters** and **words** in a text entered by the user.  

## ✨ Features

- 🆎 Count the **total number of characters** in a text.  
- 🔤 Count the **total number of words** in a text.  
- 🐍 Beginner-friendly Python project.  

## 🚀 How to Use

1. Run the Python file `Text_Analyzer.py`.  
2. Enter any text when prompted.  
3. The program will display the number of characters and words.  

## 💻 Code

```python
user_text = input("Enter a text: ")
num_characters = len(user_text)
num_words = len(user_text.split())

print("Number of characters:", num_characters)
print("Number of words:", num_words)

## 📂 File

[📄 Download or view Text_Analyzer.py](./Text_Analyzer.py)
