text = "The quick brown fox jumps over the lazy dog"


def text_length():
  len_text = 0
  for letter in text:
    if letter != " ":
      len_text += 1
  return len_text

def text_length_full():
  len_text_full = 0
  for letter in text:
    len_text_full += 1
  return len_text_full

def text_word_count():
  word_count = 0
  for word in text:
    if word == " ":
      word_count += 1
  return word_count + 1
# Не удаляйте код ниже, он нужен для вызова и тестирования функции

print(text_length())
print(text_length_full())
print(text_word_count())