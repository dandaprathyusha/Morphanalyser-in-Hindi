import sys
from morphanalysis import *

def main():
	f = open(sys.argv[1])
	f = f.readlines()

	for each_file in f:
		each_file = each_file[:-1]
		fp = open(each_file)
		fp = fp.readlines()

		# morph_tags contains : [id_num, word_pres, POS, L, G, N, P, C]
		morph_tags = morph(fp)
		'''for m in morph_tags:
			print m
		print'''

		# features contains ; [id_num, word_pres, POS, all suffixes of lenth <= 7, \
		#						G_prev1, G_prev2, G_prev3, \
		#						N_prev1, N_prev2, N_prev3, \
		#						P_prev1, P_prev2, P_prev3, \
		#						C_prev1, C_prev2, C_prev3, \
		#						G_next1, N_next1, P_next3, C_next3]
		features = token_suffix_gnpc(morph_tags)

		## features contains ; [id_num, word_pres, POS, all suffixes of lenth <= 7, \
		#						G_prev1, G_prev2, G_prev3, \
		#						N_prev1, N_prev2, N_prev3, \
		#						P_prev1, P_prev2, P_prev3, \
		#						C_prev1, C_prev2, C_prev3, \
		#						G_next1, N_next1, P_next3, C_next3, \
		#						word_prev, word_next]
		features = word_forms(features)



		# features contains ; [id_num, word_pres, POS, all suffixes of lenth <= 7, \
		#						G_prev1, G_prev2, G_prev3, \
		#						N_prev1, N_prev2, N_prev3, \
		#						P_prev1, P_prev2, P_prev3, \
		#						C_prev1, C_prev2, C_prev3, \
		#						G_next1, N_next1, P_next3, C_next3, \
		#						word_prev, word_next, \
		#						length_current_word, chartype_cuurent_word]
		features = len_chartype(features)

		for each_feature in features:
			for f in each_feature[1:]:
				if f != each_feature[-1]:
					print str(f)+',',
				else:
					print str(f),
			print
	
		
if __name__ == '__main__':
	main()
