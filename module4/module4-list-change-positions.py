first = input('Enter first numnber: ')
second = input('Enter second number: ')
print('Before swapping:', first, second)
first, second = second, first
print('After swapping:', first, second)

#sorting alphabetically
top_cities = ['new york', 'los angeles', 'houston', 'phoenix']
top_cities.sort()
print(top_cities)

random_numbers = [2, 5, 0, -3, 4]
random_numbers.sort()
print(random_numbers)

random_numbers = [2, 5, 0, -3, 4]
random_numbers.sort(reverse=True)
print(random_numbers)

#list_name.sort () - sorts the original list
#sorted(list_name): gives back a new, sorted list, keeps the original unchanged

top_cities = ['new york', 'los angeles', 'houston', 'phoenix']
print(sorted(top_cities))
print(top_cities)