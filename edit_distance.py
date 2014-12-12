def edit_distance(word1, word2):
	
	if word1 == word2:
		return []

	len_1=len(word1)
	len_2=len(word2)


	# the matrix whose last element ->edit distance
	# intializes matrix to 0
	x =[[0]*(len_2+1) for _ in range(len_1+1)]

	# initialization of base case values
	for i in range(0,len_1+1): 
		x[i][0]=i

	for j in range(0,len_2+1):
		x[0][j]=j

	# stores all the possible edit_distance path in the form (op, from_index, to_index)
	edit_path = []
	# stores op, from char, to char
	edit_char = []

	# calculates the edit distance
	for i in range (1,len_1+1):
		for j in range(1,len_2+1):
			
			from_index = []	# from (i,j)
			to_index = []	# to (k,l)

			if word1[i-1] == word2[j-1]:
				x[i][j] = x[i-1][j-1]
				from_index.append(i-1)
				from_index.append(j-1)
				edit_path.append('no_op')
				edit_char.append('no_op')
				#print "no op"
			else :
				if x[i][j-1] < x[i-1][j] and x[i][j-1] < x[i-1][j-1]:
					x[i][j] = x[i][j-1] + 1
					from_index.append(i)
					from_index.append(j-1)
					edit_path.append('i')
					edit_char.append('i')
					#print 'i1'

				elif x[i-1][j] < x[i][j-1] and x[i-1][j] < x[i][j-1]:
					x[i][j] = x[i-1][j] + 1
					from_index.append(i-1)
					from_index.append(j)
					edit_path.append('d')
					edit_char.append('d')
					#print 'd1'

				else:
					x[i][j] = x[i-1][j-1] + 1
					from_index.append(i-1)
					from_index.append(j-1)
					edit_path.append('s')
					edit_char.append('s')
					#print 'r1'

			edit_char.append(word1[i-1])
			to_index.append(i)
			to_index.append(j)
			edit_char.append(word2[j-1])
			edit_path.append(from_index)
			edit_path.append(to_index)

				#x[i][j]= min(x[i][j-1], x[i-1][j], x[i-1][j-1]) + 1 # insertion, deletion, substitution

	#--------------------------------------------------------------------#
	'''
	# way in which matrix was filled [op, from_index, to_index]
	for i in range(len(edit_path)):
		if i != 0 and i%3 == 0:
			print 
		print edit_path[i],
		print edit_char[i], 
	print 
	
	#--------------------------------------------------------------------#
	# prints the edit_distance matrix
	for i in range(0, len_1+1):
		for j in range(0, len_2+1):
			x[i][j]#print x[i][j],
		#print
	
	#--------------------------------------------------------------------#
	# prints the final edit_distance
	print "I AM edit_distance: ", x[i][j]
	'''
	#--------------------------------------------------------------------#

	# finds the shortest path -> op stores the operations
	op = []
	# o -> a tempory list to store ['operation', 'character', 'index']
	o = []
	# to look for [i,j]
	look_for = edit_path[-2]

	# appends the operation to be performed
	if edit_path[-3] == 's':
		# of format ['s','x','y',i']
		# substitute 'x' with 'y' at index 'i'
		o.append(edit_path[-3])
		o.append(edit_char[-2])
		o.append(edit_char[-1])

	elif edit_path[-3] == 'i':
		# of format ['i','x','i']
		# substitute 'x' at index 'i'
		o.append(edit_path[-3])
		o.append(edit_char[-1])

	elif edit_path[-3] == 'd':
		# of format ['d',i]
		# delete at index 'i'
		o.append(edit_path[-3])
	else:
		
		# of format ['i','x','index']
		# insert 'x' at index 'i'
		o.append(edit_path[-3])
		o.append(edit_char[-2])

	op.append(o)	

	# stores the diffrenec in length
	if len_2 > len_1:
		l = len_2 - len_1
	else:
		l = len_1 - len_2

	# finds the shortest path
	while True:
		o = []
		#print word1, word2

		if look_for[0] == 0:
			while look_for[0] == 0:
				o = []
				if look_for[1] == 0:
					break;
				else:
					o.append('i')
					if len_2 > len_1:
						o.append(word2[l-1])
					else:
						o.append(word1[l-1])

					look_for[1] = look_for[1]-1
					l = l-1
					op.append(o)

		elif look_for[1] == 0:
			while look_for[1] == 0:
				o = []
				if look_for[0] == 0:
					break;
				else:
					o.append('d')

					look_for[0] = look_for[0]-1
					op.append(o)


		if look_for == [0,0]:
			break;

		i = edit_path.index(look_for)

		if edit_path[i-2] == 'd' or edit_path[i-2] == 'no_op':
			o.append(edit_path[i-2])
			#o.append(edit_char[i-1])
		elif edit_path[i-2] == 's':
			o.append(edit_path[i-2])
			o.append(edit_char[i-1])
			o.append(edit_char[i])
		else:
			o.append(edit_path[i-2])
			o.append(edit_char[i])
		op.append(o)

		i = i-1
		look_for = edit_path[i]
	
	#--------------------------------------------------------------------#

	# operations to apply from the end of the string
	operations = []
	'''print op'''
	for i in range(len(op)):
		flag = 0
		o = ''
		for each_op in op[i] :
			if each_op == 'no_op':
				flag = 1
				break;
			o = o + each_op + ' '
		if flag == 1:
			continue

		o = o + str(i+1)
		operations.append(o)
	'''print operations'''

	#--------------------------------------------------------------------#
	
	
	return operations

'''
e = edit_distance('god','good')
print e
'''
