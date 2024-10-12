# TODO Найдите количество книг, которое можно разместить на дискете
v_discet = 1.44 * 1024 * 1024
v_symbols_1_book = 100 * 50 * 25 * 4

count_books = int(v_discet // v_symbols_1_book)

print("Количество книг, помещающихся на дискету:", count_books)
