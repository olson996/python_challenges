# cleaner_code.py
import random

#NotImplemented
def test2(*args, **kwargs):
	try:
		match_list = []
		str_to_compare = args[0]
		str_list = kwargs['arg_list']
		for i in str_list:
			match_list.append(str_to_compare == i)
		return match_list
	except:
		pass
#NotImplemented
def mytime(*args, **kwargs):
	begin_time = datetime.datetime.now()
	print(args[0], args[1])
	for i in range(args[1]):
		print(args[0](args[2], arg_list=args[3]))
	print(datetime.datetime.now() - begin_time)
#NotImplemented
def test(*args, **kwargs):
	try:
		match_list = []
		str_to_compare = args[0]
		id_str = intern(str_to_compare)
		str_list = kwargs['arg_list']
		for i in str_list:
			id_i = intern(i)
			match_list.append(id_i is id_str)
		return match_list
	except:
		pass
#NotImplemented
def append_to(*a, **kw):
	if 'to' in kw:
		try:
			kw['to'].append(a[0])
		except:
			pass
#NotImplemented
def _match(*a, **kw):
	return_list = []
	for i in a[0]:
		if i in a[1]:
			return_list.append(i)
	return return_list
#NotImplemented
# _unique(list t1, list t2)
def _unique(*a, **kw):
	return_list = set()
	for i in a[0]:
		return_list.add(i)
	for i in a[1]:
		return_list.add(i)
	return return_list

def gen_ran_len_lst():
	"""Returns a random length list of random numbers."""
	lst = []
	for i in range(random.randrange(0, 1000)):
		lst.append(random.randrange(0, 1000))
	return lst

def _diff(*a):
	"""Returns difference between list t1, and list tn. """
	return set.difference(*tuple(map(lambda x : set(x), a)))

def if_elif_func(n=0):
	"""Perform if elif checks on n"""
	if n % 2 != 0:
		print('Weird')
	elif n % 2 == 0 and n>=2 and n<=5:
		print('Not Weird')
	elif n % 2 == 0 and n>=6 and n<=20:
		print('Weird')
	elif n % 2 == 0 and n > 20:
		print('Not Weird')
		
def read_two_ints(*a, **kw):
	"""Perform various arithmetic on two integers."""
	print(a[0] + a[1])
	print(a[0] - a[1])
	print(a[0] * a[1])
	print(a[0] // a[1])
	print(a[0] / a[1])

def square_n(*a, integer=None):
	"""Read an integer N. Print n^2 for i<N. """
	for i in range(0, integer):
		print(int(i)**2)

def leap(year=0, *a, **kw):
	"""Calculate georgian leap year. """
	year_div_4 = (year % 4) == 0
	year_div_100 = (year % 100) == 0
	year_div_400 = (year % 400) == 0
	if year_div_4:
		if year_div_100:
			if year_div_400:
				return True
			return False
		return True
	return False

if __name__ == "__main__":
	print("Cleaner code in progress - Cameron Olson")
	print("Run by typing python -i .\cleaner_code.py and try typing \
		\n'dir()' to see what cleaner functions do! \
		\nand type help(function) for more info")
