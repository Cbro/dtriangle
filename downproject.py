#start
import pdb, sys, numpy as np, pickle, multiprocessing as mp
#sys.path.append('python-emd-master')
#from emd import emd

load_file = sys.argv[1]

with open(load_file) as f:
    [X, BOW_X, y, C, words] = pickle.load(f)
n = np.shape(X)

ctr =0

word_file  = open("wfile.txt", 'w')
label_file = open("lfile.txt", 'w')

for doc in X:
	#if ctr > 0:
	#	break

	num_row = int(np.shape(doc)[0])
	num_col = int(np.shape(doc)[1])

	print " --------------------------------"
	print ' Number of Rows = %d' %(num_row)
	print ' Number of Cols = %d' %(num_col)
	# We need the output of each column in this matrix
	for i in range(num_col):
		word_vec = doc[:,i]
		# Get each dimension in the word vector 
		for w_i in word_vec:
			#print w_i
			word_file.write('%.10f ' % (w_i))
		word_file.write("\n")
				
		label_file.write('%d\n' %  (y[ctr]) )

	
	print " --------------------------------\n"
	ctr += 1

#print "----- Words -------"
#print words
#print "----- Labels (C) ----"
#print C
#print "----- Labels (y) ----"
#print y


word_file.close()
label_file.close()
