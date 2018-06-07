#https://py.checkio.org/mission/all-the-same/solve/

def all_the_same(elements) -> bool:
	#print(elements)
	result = None
	dod = set(elements)
	if len(dod) == 1:
		result = True
	elif len(dod) == 0:
		result = True
	else:
		result = False
	return result
	
print(all_the_same([1, 1, 1]))


from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    result = None
	dod = set(elements)
	if len(dod) == 1:
		result = True
	elif len(dod) == 0:
		result = True
	else:
		result = False
	return result


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")