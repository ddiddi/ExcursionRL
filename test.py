
import numpy as np
#a=np.array([1, 2,5])
#b=np.array([3,4,5])
#print np.array_equal(a,b)
#
#a=1294
#print (np.sign(a))
#idx=np.array([])
#x=np.array([1,2,3,2,3])
#maxVal=np.amax(x)
#print maxVal 
#
#for i in range(len(x)):    
#    if x[i]==maxVal:
#        idx=np.append(idx,[i])        
#        
#idx=idx.astype(int)
#idx=np.random.permutation(idx)

import pickle

f = open('store.pckl', 'wb')
pickle.dump(object, f)
f.close()

f = open('store.pckl', 'rb')
object = pickle.load(f)
f.close()




