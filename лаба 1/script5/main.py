# Напишите скрипт, который позволяет ввести с клавиатуры текст
# предложения и сформировать новую строку на основе исходной, в
# которой все слова, начинающиеся с большой буквы, приведены к
# верхнему регистру. Слова могут разделяться запятыми или пробелами.
# Например, если пользователь введет строку «город Донецк, река
# Кальмиус», результирующая строка должна выглядеть так: «город
# ДОНЕЦК, река КАЛЬМИУС»
# import re


text = input('Enter a text: ')
lst = text.split()
end = ""

for val in lst:
  if (val.istitle()): end += " " + val.upper()
  else:
    end += " " + val


print(end)


