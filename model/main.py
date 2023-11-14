from model.clasick import Pinguin

input_valuer = [
    ['Storage_1', 'Lviv'],
    ['Striy', 'Lviv'],
    ['Storage_2', 'Storage_1'],
    ['Kiyv', 'Lviv'],
    ['Ternopil', 'Harkiv'],
    ['Storage_3', 'Ternopil'],
    ['Ternopil', 'Lviv']
]

test = Pinguin(input_valuer)




print(test.all_storage_graph())