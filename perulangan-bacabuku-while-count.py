"""
Perulangan
"""

books_count = 10
print('Mom says, "Read & understand all of your books"')
books_read = 0

books_understood = 0
print(f"Number of books read {books_read}")

while books_read < books_count * 2:
    books_read = books_read + 1
    if books_understood == 9:
        print(f"Books no: {books_understood} is not yet understood")
    else:
        books_understood = books_understood + 1
        print(f"Books no: {books_understood} is understood")

print(f"Number of books understood: {books_understood}")

if books_understood == books_count:
    print('"Mom, I understand of all my books"')
else:
    print(f'"Mom, I didnt understand of all my books. '
              f'I only understand {books_understood} books"')