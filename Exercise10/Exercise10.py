def anti_vowel(text):
  new_word = ""
  vowels = "ieaouIEAOU"
  for letter in text:
    if letter not in vowels:
      new_word = new_word + letter
  return new_word    

print (anti_vowel("Hey You!"))
