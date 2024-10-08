immutable_var = 1, 'Dima', 14, 'Arkadii'
print('Immutable_var:', immutable_var)
# immutable_var[0] = 52 # - Если мы введем эту команду в код то появится ошибка которая сообщит нам, что кортеж не поддерживает назначение  элементов, так как кортеж является неизменяемым элементом.
mutable_list = [23, 133, True, 'Знать']
mutable_list[1] = 'Жираф'
mutable_list[2] = 72.13
print('Mutable_list:', mutable_list)