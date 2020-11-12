

# def first(word):
# 	print(len(word) // 2)
# 	return word[0]
# def last(word):
# 	return word[-1]
# def middle(word):
# 	return word[1:-1]

# print(first('middle'))
# print(last('middle'))
# print(middle('middle'))


def is_palindome(word):
	left = 0
	right = len(word)
	middle = len (word) // 2 
	
	left_result = word[left:middle]
	right_result = (word[middle + 1:right])
	right_result = right_result[::-1]

	print(left_result == right_result)




is_palindome('redivider')

