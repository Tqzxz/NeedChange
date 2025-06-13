

from mxnet import autograd, nd
import random
from time import time
import d2lzh

class ML_pipeline:

    def __init__( self, ):

        self.data_set = None 
        self.labels   = None 
    
    def vector_calculation_test( self, ):

        ## Create Two 1000 dim Vectors
        a = nd.ones(shape=1000)
        b = nd.ones(shape=1000)

        ## Common way to do the vector addition "One by One"
        t1 = time()
        c = nd.ones(shape=1000)
        for i  in range(1000):
            c[i] = a[i] + b[i]
        t2 = time()

        ## Faster way to do the addition
        d = a + b
        t3 = time()
        
        print(f"Common addition takes {t2 - t1}\nvecotrized_opeartion just takes {t3 - t2}")

        return 

    def linear_regrassion( self, ):
        
        # Generate Original Data-Set
        self.linear_regrassion_generate_data_set()

        # Virtualise data
        d2lzh.set_figsize()
        d2lzh.plt.scatter( self.data_set.asnumpy(), self.labels.asnumpy(), 1)


    def linear_regrassion_generate_data_set( self, ):
        
        feature_nm = 2
        data_nm    = 1000

        default_w  = [2, -3.4]
        default_b  = 4.2

        ## random_data is a 1000 by 2 tensors
        self.data_set = nd.random.normal(scale=1, shape=(data_nm,feature_nm))

        self.labels  = default_w[0] * self.data_set[:,0] + default_w[1] * self.data_set[:,1] + default_b

        self.labels  += nd.random.normal(scale=0.01, shape=(self.labels.shape))

        return 
    

if __name__ == "__main__":

    ml_test = ML_pipeline()
    ml_test.linear_regrassion()
