#start
import pdb, sys, numpy as np, pickle, multiprocessing as mp
import matplotlib.pyplot as plt

from sklearn.metrics.pairwise import pairwise_distances
#sys.path.append('python-emd-master')
#from emd import emd

np.set_printoptions(threshold=np.inf)

load_file = sys.argv[1]

with open(load_file) as f:
    [X, BOW_X, y, C, words] = pickle.load(f)
n = np.shape(X)

ctr =0

word_file  = open("wfile.txt", 'w')
label_file = open("lfile.txt", 'w')
docid_file = open("dfile.txt", 'w')

hashtbl = {}

word_vec_list = []
for doc in X:
	#if ctr > 10:
	#	break

	num_row = int(np.shape(doc)[0])
	num_col = int(np.shape(doc)[1])

	print " --------------------------------"
	print ' Number of Rows = %d' %(num_row)
	print ' Number of Cols = %d' %(num_col)
	# We need the output of each column in this matrix
	
	

	for i in range(num_col):
		word_vec = doc[:,i]
		#word_vec = float(word_vec)
		word_vec = word_vec.astype(np.float)
		#print "---word vector---"
		#print word_vec
		
		key = '%s|%s|%s' % (word_vec[0], word_vec[1], word_vec[2]) 
		print "*%s*" % (key)

		if key in hashtbl:
			print "found key so skip"
		else:
			word_vec_list.append( word_vec ) 	
			hashtbl[key] = 1	


		# Get each dimension in the word vector 
		#for w_i in word_vec:
			#print w_i
		#	word_file.write('%.10f ' % (w_i))
		#word_file.write("\n")
				
		#label_file.write('%d\n' %  (y[ctr]) )
		#docid_file.write('%d\n' %  (ctr))

	print " --------------------------------\n"
	ctr += 1

word_vec_darray = np.vstack(word_vec_list)
print word_vec_darray.dtype

print "---- final word vec list --- "
print word_vec_darray
print np.shape(word_vec_darray)

#
# Let us compute pairwise euclidean distances now!
#
D = pairwise_distances(word_vec_darray, metric='euclidean')
print "----- D ----- "
print D
print np.shape(D)


fig, ax = plt.subplots()
heatmap = ax.pcolor(D, cmap=plt.cm.Blues)
# put the major ticks at the middle of each cell
#ax.set_xticks(np.arange(D.shape[0])+0.5, minor=False)
#x.set_yticks(np.arange(D.shape[1])+0.5, minor=False)

# want a more natural, table-like display
#ax.invert_yaxis()
#ax.xaxis.tick_top()

plt.show()


#print "----- Words -------"
#print words
#print "----- Labels (C) ----"
#print C
#print "----- Labels (y) ----"
#print y


word_file.close()
label_file.close()
docid_file.close()