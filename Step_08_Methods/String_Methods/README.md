### 📝 Python String Methods – Easy Explanation  

String methods help us manipulate text easily. Below are some useful string methods with examples! 🚀  

#### 🔹 Creating a String  
```python
name = "Hadiqa Gohar"
print(name)  # Output: Hadiqa Gohar
```  

#### 🔹 Converting Case  
1️⃣ **`upper()`** – Converts all characters to uppercase  
   ```python
   uppercase = name.upper()
   print(uppercase)  # Output: HADIQA GOHAR
   ```  

2️⃣ **`lower()`** – Converts all characters to lowercase  
   ```python
   lowercase = name.lower()
   print(lowercase)  # Output: hadiqa gohar
   ```  

3️⃣ **`capitalize()`** – Capitalizes only the first letter  
   ```python
   capitalized = name.capitalize()
   print(capitalized)  # Output: Hadiqa gohar
   ```  

4️⃣ **`title()`** – Capitalizes the first letter of each word  
   ```python
   titled = name.title()
   print(titled)  # Output: Hadiqa Gohar
   ```  

#### 🔹 Modifying Strings  
5️⃣ **`strip()`** – Removes spaces from the beginning and end  
   ```python
   stripped = name.strip()
   print(stripped)  # Output: Hadiqa Gohar
   ```  

6️⃣ **`replace()`** – Replaces a word in the string  
   ```python
   replaced = name.replace("Hadiqa", "Hello")
   print(replaced)  # Output: Hello Gohar
   ```  

#### 🔹 Splitting & Joining  
7️⃣ **`split()`** – Splits the string into a list  
   ```python
   words = name.split()
   print(words)  # Output: ['Hadiqa', 'Gohar']
   ```  

8️⃣ **`join()`** – Joins list elements into a string  
   ```python
   joined = " _ ".join(words)
   print(joined)  # Output: Hadiqa _ Gohar
   ```  

#### 🔹 Searching in Strings  
9️⃣ **`find()`** – Finds the index of a word  
   ```python
   index = name.find("Gohar")
   print(index)  # Output: 7
   ```  

🔟 **`count()`** – Counts occurrences of a character  
   ```python
   count_a = name.count("a")
   print(count_a)  # Output: 3
   ```  

💡 **String methods help in formatting, modifying, and analyzing text efficiently! 🏆**
