def search(search: str):
	try:
		data = open('database.xls', 'r')

		for item in data:
			array = item.split(',')
			if array[0] == search:
				data.close()
				return array[1]
		data.close()
		return None
	except Exception as e:
		print(e)
		return False


def write(data: str):
	try:
		f = open('database.xls', 'a')
		f.write(f'{data}\n')
		f.close()
		return True
	except Exception as e:
		print(e)
		return False

res = search("oxford")
# res = write('oxford, royaume uni')
print(res)