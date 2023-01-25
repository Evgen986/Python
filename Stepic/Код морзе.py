# Напишите программу для кодирования текстового сообщения в соответствии с кодом Морзе.

letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..',
         '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-',
         '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
dict_morse = dict(zip(letters, morse))
print(*[dict_morse[el] for el in input().upper() if el in dict_morse.keys()])

