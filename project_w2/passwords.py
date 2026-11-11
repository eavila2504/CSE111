#I added a few print statements to inform the user about the password requirements they are missing.
print("Welcome to our Password strength checker!")
LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]
def main ():
    password = input("Please enter your password: ")
    strength = password_strength(password) 
    print(f"Your password strength is: {strength}/5")   
    restart = input("would you like to check another password ? (press q to quit): ")
    if restart.lower() !=  "q":
        main()
    else: 
        print("Thank you for using the password strength checker. Stay safe!")

def word_in_file(word, filename, case_sensitive = False):
    with open (filename, "r", encoding="utf-8") as file:
        for line in file:
            file_word = line.strip()
            if not case_sensitive:
                file_word = file_word.lower()
                word = word.lower()
            if word == file_word:
                return True 
    return False 
   
def word_has_character(word, character_list):
    for char in character_list:
        if char in word:
            return True
    return False 

def word_complexity(word):
    complexity = 0 
    if word_has_character(word, LOWER): 
        complexity += 1
    else: 
        print("password should have at least a lowercase letter to be safe")
    if word_has_character(word, UPPER):
        complexity += 1
    else: 
        print("password should have at least an uppercase letter to be safe")
    if word_has_character(word, DIGITS):
        complexity += 1
    else: 
        print("password should have at least a digit letter to be safe")
    if word_has_character(word, SPECIAL):
        complexity += 1
    else: 
        print("password should have at least a special digit to be safe")
    return complexity 

def password_strength(password, min_length = 10, strong_length = 16):
    if len(password) < min_length:
         print("Password is too short")
         return 0
    if word_in_file(password, "wordlist.txt"):
        print("Password is a dictionary word and is not secure")
        return 0
    if word_in_file(password, "toppasswords.txt"):
        print("Password is a common password and is not secure")
        return 0
    complexity = word_complexity(password)
    if len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password ")
        return 5
    return min (1 + complexity, 5)

if __name__ == "__main__":
    main()
