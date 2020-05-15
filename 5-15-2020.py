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

def mytime(*args, **kwargs):
	begin_time = datetime.datetime.now()
	print(args[0], args[1])
	for i in range(args[1]):
		print(args[0](args[2], arg_list=args[3]))
	print(datetime.datetime.now() - begin_time)


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

def append_to(*a, **kw):
	if 'to' in kw:
		try:
			kw['to'].append(a[0])
		except:
			pass
	
def _match(*a, **kw):
	return_list = []
	for i in a[0]:
		if i in a[1]:
			return_list.append(i)
	return return_list

# _unique(list t1, list t2)
def _unique(*a, **kw):
	return_list = set()
	for i in a[0]:
		return_list.add(i)
	for i in a[1]:
		return_list.add(i)
	return return_list

# _custom(list t1, list t2)
def _diff_bare(*a, **kw):
	for i in a[0]:
		if i not in a[1]:
			print(i)

def fun1(*a, **kw):
	if n % 2 != 0:
		print('Weird')
	elif n % 2 == 0 and n>=2 and n<=5:
		print('Not Weird')
	elif n % 2 == 0 and n>=6 and n<=20:
		print('Weird')
	elif n % 2 == 0 and n > 20:
		print('Not Weird')
		
def fun2(*a, **kw):
	print(a[0] + a[1])
	print(a[0] - a[1])
	print(a[0] * a[1])

def fun3(*a, **kw):
	"""Read two integers and print two lines."""
	print(a[0] // a[1])
	print(a[0] // a[1])

def fun4(*a, integer=None, *kw):
""" Read an integer N. For all non-negative integers i < N, print i^2 """
	
	for i in range(0, integer):
		print(int(i)**2)


def leap(*a, **kw):
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

def fun5(*a, **kw):
	#set A
	a_set = set()
	sets = [a_set]*n