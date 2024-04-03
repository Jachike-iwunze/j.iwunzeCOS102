print(' Welcome to the Class and here is the list and information of our boys and girls  ')

boys_data = {'Chinedu ': '19      5.7      74',
             'Liam    ': '16      5.9      87',
             'Wale    ': '18      5.8      75',
             'Gbenga  ': '17      6.1      68',
             'Abiola  ': '20      5.9      66',
             'Kola    ': '19      5.5      78',
             'Kunle   ': '16      6.1      87',
             'George  ': '18      5.4      98',
             'Thomas  ': '17      5.8      54',
             'Wesley  ': '19      5.7      60'}

girls_data = {'Evelyn ': '17      5.5      80',
             'Jessica': '16      6.0      85',
             'Somto  ': '17      5.4      70',
             'Edith  ': '18      5.9      70',
             'Liza   ': '16      5.6      76',
             'Madona ': '18      5.5      66',
             'Waje   ': '17      6.1      87',
             'Tola   ': '20      6.0      95',
             'Aisha  ': '19      5.7      50',
             'Latifa ': '17      5.5      49'}

print('Name     | Age      | Height     | Scores       ')
for name, data in boys_data.items():
    age, height, scores = data.split()
    print(f"{name:<5} | {age:<8} | {height:<10} | {scores}")

print('\nGirls:')
print('Name    | Age   | Height  | Scores    ')
for name, data in girls_data.items():
    age, height, scores = data.split()
    print(f"{name:<5} | {age:<6} | {height:<7} | {scores}")
