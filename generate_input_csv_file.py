#******************************************************************************************************************************************
# TITLE     : GENERATE_INP_CSV_FILE
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

#Create a csv file with the required number of PCB records to run the digital twin

print('*****ENTRY INTO GENERATE_INPUT_CSV_FILE*****')

import csv
import numpy  as np
import pandas as pd

NUM_RECORDS = 100

inp_csv_file = pd.DataFrame(columns=['ldr_entry','ldr_exit','spr_entry','spr_exit','pp1_entry','pp1_exit','pp2_entry','pp2_exit','rfo_entry','rfo_exit'])

ldr_entry = 1;  ldr_exit  = 3;
spr_entry = 5;  spr_exit  = 7;
pp1_entry = 9;  pp1_exit  = 11;
pp2_entry = 13; pp2_exit  = 15;
rfo_entry = 17; rfo_exit  = 19;

for i in range(0,NUM_RECORDS):
    if (i > 0):
        ldr_entry += 3
        ldr_exit  += 3
        spr_entry += 3
        spr_exit  += 3
        pp1_entry += 3
        pp1_exit  += 3
        pp2_entry += 3
        pp2_exit  += 3
        rfo_entry += 3
        rfo_exit  += 3
    #end-if
    
    data = pd.DataFrame([[ldr_entry,ldr_exit,spr_entry,spr_exit,pp1_entry,pp1_exit,pp2_entry,pp2_exit,rfo_entry,rfo_exit]],columns=inp_csv_file.columns)
    inp_csv_file = inp_csv_file.append(data)
    del data
#end-for

inp_csv_file = inp_csv_file.reset_index()
inp_csv_file = inp_csv_file.iloc[:,1:len(inp_csv_file.columns)]

inp_csv_file.to_csv('dtregpcb_csv_file.csv',index=False)

print('Number of records =', NUM_RECORDS)
print('*****EXIT FROM GENERATE_INPUT_CSV_FILE*****')