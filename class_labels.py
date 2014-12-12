import sys
from edit_distance import edit_distance
import itertools

def extract_labels(fp):
	cl_labels = []
	for i in fp:
		if i != '\n':

			data = i.split('\t')

			# lemma
			lemma = data[2]
	
			# contains the token
			token = data[1]
			
			# opens a file and appends the tokens
			'''with open('training_tokens.txt','a') as t:
				t.write(token + ' ' + lemma + '\n')
			'''

			# find the edit_distance between token and its lemma
			# appends the class labels
			cl_labels.append(edit_distance(token, lemma))
				
	return cl_labels

def main():
	f = open(sys.argv[1])
	f = f.readlines()
	class_labels = []

	for each_file in f:

		each_file = each_file[:-1]
		fp = open(each_file)

		# extracts [token, suffixes, POS, length, character_type(alpha, digit, alphanum), class_labels]
		cl = extract_labels(fp)

		cl.sort()
		cl = list(cl for cl,_ in itertools.groupby(cl))	
		
		#print "##########",each_file
		for i in cl:
			class_labels.append(i)
		#print cl
		#print "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
		#print class_labels
		

	class_labels.sort()
	class_labels = list(class_labels for class_labels,_ in itertools.groupby(class_labels))

	for i in class_labels:
		print i
	print
	print "No. of unique class labels: ",len(class_labels)
		
if __name__ == '__main__':
	main()
