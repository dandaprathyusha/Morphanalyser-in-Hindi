# [id_num, word_pres, POS, L, G, N, P, C]
def morph(fp):
	morph = []
	for i in fp:
		m = []
		if i != '\n':
			tokens = i.split('\t')
			
			# <num, word_pres, POS, L, G, N, P, C>
			lgnpc = tokens[5].split('|')

			# appends the id_num
			m.append(tokens[0])
			# appends the word_pres		 
			m.append(tokens[1])
			# appends the POS of word_pres
			m.append(tokens[3])
			# appends the Lemma of word_pres
			m.append(lgnpc[0].split('-')[1])
			# appends the Gender of word_pres
			m.append(lgnpc[2].split('-')[1])
			# appends the Number of word_pres
			m.append(lgnpc[3].split('-')[1])
			# appends the Person of word_pres
			m.append(lgnpc[4].split('-')[1])
			# appends the Case of word_pres
			m.append(lgnpc[5].split('-')[1])

			# [id_num, word_pres, POS, L, G, N, P, C]
			morph.append(m)

	return morph			


# appends the id_num, token, suffixes and gnpc
# extracts G,N,P,C (in order) for previous 3 words and 1 next word
def token_suffix_gnpc(morph_tags):

	features = []
	for each_m in morph_tags:

		m = []
		# gets the present index
		present_index = morph_tags.index(each_m)

		#--------------------------------------------------------------------------

		#appends the id_num
		m.append(each_m[0])

		# appends the current word and all its suffixes
		#current word
		token = each_m[1]
		m.append(token)

		# appends the POS
		POS = each_m[2]
		m.append(POS)

		# suffixes till length 7
		no_suf = 0
		for i in range(len(token)-1,0,-1):
			# append suffixes with length < 7
			if no_suf <= 7:
				m.append(token[i:])
				no_suf = no_suf + 1
		rem_suf = 7-no_suf
		while rem_suf > 0:
			m.append(0)
			rem_suf = rem_suf-1


		#--------------------------------------------------------------------------

		# GNPC of previous 3 words
		if each_m[0] >= '1':
			id_num = int(each_m[0])
			window_size = 4
			start_index = id_num - window_size
				
			if start_index < 0:
				start_index = 0

			# loop to append previous 3 g, n, p, c tags
			p = present_index
			i = id_num - 1
			
			gender = []
			number = []
			person = []
			case = []

			# print "##################", morph_tags[p][0], morph_tags[p][1]
			while i > start_index:
				# print morph_tags[p-1][1]
				g = morph_tags[p-1][4]
				n = morph_tags[p-1][5]
				per = morph_tags[p-1][6]
				c = morph_tags[p-1][7]

				if g == '':
					gender.append(0)
				else:
					gender.append(g)
				if n == '':
					number.append(0)
				else:
					number.append(n)
				if per == '':
					person.append(0)
				else:
					person.append(per)
				if c == '':
					case.append(0)
				else:
					case.append(c)

				i = i - 1
				p = p - 1
			# print
			rem_gnpc = 3-len(gender)
			while rem_gnpc > 0:
				gender.append(0)
				number.append(0)
				person.append(0)
				case.append(0)
				rem_gnpc = rem_gnpc - 1

			for j in range(len(gender)):
				m.append(gender[j])

			for j in range(len(number)):
				m.append(number[j])

			for j in range(len(person)):
				m.append(person[j])

			for j in range(len(case)):
				m.append(case[j])

			# to append GNPC of next word
			p = present_index
			if p+1 != len(morph_tags):		
				if morph_tags[p+1][0] != '1':
					g = morph_tags[p+1][4]
					n = morph_tags[p+1][5]
					per = morph_tags[p+1][6]
					c = morph_tags[p+1][7]
		
					if g == '':
						m.append(0)
					else:
						m.append(g)
					if n == '':
						m.append(0)
					else:
						m.append(n)
					if per == '':
						m.append(0)
					else:
						m.append(per)
					if c == '':
						m.append(0)
					else:
						m.append(c)
				else:
					m.append(0)
					m.append(0)
					m.append(0)
					m.append(0)
			else:
				m.append(0)
				m.append(0)
				m.append(0)
			m.append(0)

		features.append(m)

	return features


# appends the word_prev and word_next
def word_forms(features):
	for i in range(len(features)):
		
		if i-1 >= 0 and features[i][0] != '1':
			word_prev = features[i-1][1]
		else:
			word_prev = 0

		if i+1 != len(features):
			if features[i+1][0] != '1':
				word_next = features[i+1][1]
			else:
				word_next = 0

		features[i].append(word_prev)
		features[i].append(word_next)

	return features


# appends the length and chartype
def len_chartype(features):
	for f in features:
		# length of token
		token = f[1]
		len_tok = len(token)
		f.append(len_tok)

		# check the character type
		if token.isalpha():
			f.append('alpha')
		elif token.isdigit():
			f.append('digit')
		else:
			f.append('alphanum')

	return features
