# https://py.checkio.org/mission/most-wanted-letter/solve/
# https://www.tutorialspoint.com/python/python_basic_operators.htm

def counter(data):
	main = []
	lst = []
	lst_2 = []
	result = None
	for ex in sorted(data.lower()):
		if ex.isalpha():
			main.append(ex)
	
	main = "".join(main)

	print(main)

	for letter in main:
		lst.extend(letter.split())

	print(lst)
	for solo in lst:
		lst_2.append(lst.count(solo))

	print(lst_2)

	if (len(lst) == len(set(lst)) and lst[0] == "a"):	
		result = "a"
	elif len(lst) == len(set(lst)):
		result = lst[0]
	else:
		result = lst[lst_2.index(max(lst_2))]

	return result

torrent = input("Enter letters:")

print(counter(torrent))
