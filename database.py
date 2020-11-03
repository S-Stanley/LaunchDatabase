def search(search: str, table: str):
	try:
		data = open(f'{table}.xls', 'r')
		for item in data:
			array = item.split(',')
			if array[0] == search:
				data.close()
				return array[1].replace(' ', '').capitalize()
		data.close()
		return None
	except Exception as e:
		print(e)
		return False

def write(data: str, table: str):
	try:
		f = open(f'{table}.xls', 'a')
		f.write(f'{data}\n')
		f.close()
		return True
	except Exception as e:
		print(e)
		return False

def create_table(name: str):
	try:
		f = open(f'{name}.xls', 'w')
		return True
	except Exception as e:
		print(e)
		return False

res = search('bonjour', 'langue')
# res = write("salut, français", "langue")
# res = create_table("langue")
print(res)