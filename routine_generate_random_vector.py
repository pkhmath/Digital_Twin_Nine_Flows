#******************************************************************************************************************************************
# TITLE     : ROUTINE_GENERATE_RANDOM_VECTOR
# AUTHOR    : PRAKASH HIREMATH M
# DATE      : SEP-OCT 2019
# INSTITUTE : INDIAN INSTITUTE OF SCIENCE
#******************************************************************************************************************************************


#******************************************************************************************************************************************
# VERSION HISTORY
#******************************************************************************************************************************************
# DATE (YYYY-MM-DD) | AUTHOR              | COMMENTS
#------------------------------------------------------------------------------------------------------------------------------------------
# 2019-10-11        | PRAKASH HIREMATH M  | Initial version
#******************************************************************************************************************************************

#Procedure to generate random vector of desired number of samples and probability
import random
import numpy as np

def generate_random_vector(ref_rvarr,p_arr,NUM_SAMPLES):
    
    #Validation on length of arrays
    if (len(p_arr) != len(ref_rvarr)):
        return_code    = '0001'
        return_message = 'Size of probability array and size of reference random variable array are different'
        print(return_code, '|', return_message)
        return return_code,return_message,0.0,0.0
    #end-if
    
    #Validation of sum of elements in probability array 
    if (np.round(np.sum(p_arr),1) != 1.0):
        return_code    = '0002'
        return_message = 'Probabilities donot sum up to unity'
        print(return_code, '|', return_message)
        print('Sum =', np.sum(p_arr))
        return return_code,return_message,0.0,0.0
    #end-if
    
    RV_RANGE_SIZE = len(ref_rvarr)
    rv_arr = [] #Initialization of random variable array
    for i in range(0,NUM_SAMPLES):
        rnum = random.uniform(0.0,1.0)
    
        low_sum  = 0.0
        high_sum = 0.0
        for j in range(0,RV_RANGE_SIZE):
            high_sum += p_arr[j] 
            if ((rnum > low_sum) & (rnum <= high_sum)):
                rvar = ref_rvarr[j]
            #end-if
            low_sum+= p_arr[j]
        #end-for    
    
        rv_arr = np.append(rv_arr,rvar)
    #end-for

    phat_arr = np.zeros(RV_RANGE_SIZE)
    for j in range (0,RV_RANGE_SIZE):
        phat_arr[j] = np.sum(rv_arr == ref_rvarr[j]) / NUM_SAMPLES
        print(j, 'p_arr =', p_arr[j], '| phat_arr =', phat_arr[j])
    #end-for
    
    return_code    = '0000'
    return_message = 'Successful'
    print(return_code, '|', return_message)
    return return_code,return_message,rv_arr,phat_arr

#end-proc