#******************************************************************************************************************************************
# TITLE     : SIMPY_NINEFLOW_SIMULATION
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


#******************************************************************************************************************************************
# SUMMARY
#******************************************************************************************************************************************
# This is the main module to run the discrete time simulation to show 9 flows of PCBs in the SMT-PCB Assembly Line
# The assembly line consists of following machines:
# - Line-Loader (LDR)
# - Screen-Printer (SPR)
# - Pick-and-Place1 (PP1)
# - Pick-and-Place2 (PP2)
# - Reflow-Oven (RFO)
#  
# Main Steps:
# - Generate input csv file with required number of PCBs
# - For each PCB, The csv file contains entry and exit times in LDR, SPR, PP1, PP2 and RFO machines
# - Create PCB objects for each of the PCBs
# - Generate a random vector which consists of as many random variables as the number of PCBs, according to the given probability masss
#   function (pmf). The random variable can take values in {1,2,3,4,5,6,7,8,9} with probabilities p1, p2, ..., p9
# - The random variable = 1 represents flow01, etc...
# - Depending on the random variable generated for the given PCB, determine the flow and delete the respective machine entries
# - Instantiate all machines each with queue capacity = 1
# - Schedule and run the simpy simulation
# - Display the statistics at PCB-level and at machine-level
#******************************************************************************************************************************************


#Import the standard python libraries
import simpy
import queue
import numpy  as np
import pandas as pd
import importlib

#Import application-specific python modules
import PCB
import Machine
import routine_generate_random_vector
import routine_pattern_decoder

#Re-import the application-specific python modules
importlib.reload(PCB)
importlib.reload(Machine)
importlib.reload(routine_generate_random_vector)
importlib.reload(routine_pattern_decoder)

#Generate input csv file
import generate_input_csv_file
importlib.reload(generate_input_csv_file)

#Define the simpy emvironment for simulation
env = simpy.Environment()

#Read the PCB-level data structure csv file
print('Reading the input csv file...')
dt_inpcsvfile = pd.read_csv('dtregpcb_csv_file.csv')
print('Number of records in csv file =', len(dt_inpcsvfile))

#Create a list of PCB objects
pcbobj = []
for i in range (0,len(dt_inpcsvfile)):
    pcbobj.append               \
    (PCB.PCB                    \
    (i                          \
    ,dt_inpcsvfile.ldr_entry[i] \
    ,dt_inpcsvfile.ldr_exit[i]  \
    ,dt_inpcsvfile.spr_entry[i] \
    ,dt_inpcsvfile.spr_exit[i]  \
    ,dt_inpcsvfile.pp1_entry[i] \
    ,dt_inpcsvfile.pp1_exit[i]  \
    ,dt_inpcsvfile.pp2_entry[i] \
    ,dt_inpcsvfile.pp2_exit[i]  \
    ,dt_inpcsvfile.rfo_entry[i] \
    ,dt_inpcsvfile.rfo_exit[i]  \
    )
    )
#end-for

print('max value =', np.max(np.max(dt_inpcsvfile)))

#Maximum simulation time
MAX_SIM_TIME = np.max(np.max(dt_inpcsvfile)) + 10

print('-------------------------------------------------------------------')
print('INITIAL PCB-LEVEL INFORMATION')
print('-------------------------------------------------------------------')
for i in range(0,len(dt_inpcsvfile)):
    pcbobj[i].print_parms()
#end-for
print('-------------------------------------------------------------------')


#Generate random vector to enforce different flows
NUM_SAMPLES   = len(dt_inpcsvfile)   #Number of samples to be generated
RV_RANGE_SIZE = 9                    #Number of distinct values the random variable takes

#Array of desired probabilities
p_arr = np.array([0.2,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1])

#Reference array of distinct values that the random variable takes
ref_rvarr = np.array(range(1,(RV_RANGE_SIZE+1)))

return_code,return_message,rv_arr,phat_arr = routine_generate_random_vector.generate_random_vector(ref_rvarr,p_arr,NUM_SAMPLES)

if (return_code != '0000'):
    print('Error while calling the routine : generate_random_vector')
    print('Return_Code    =', return_code)
    print('Return_Message =', return_message)
    exit()
#end-if

#Update the PCB paramaters according to the generted random variable
for i in range(0,len(dt_inpcsvfile)):
    pcbobj[i].update_parms(np.asscalar(rv_arr[i]))
    pcbobj[i].update_pattern()
#end-for

print(' ')
print('-------------------------------------------------------------------')
print('MACHINE INSTANTIATION')
print('-------------------------------------------------------------------')
ldr = Machine.Machine(env,'LDR','Line-Loader   ',1)
spr = Machine.Machine(env,'SPR','Screen-Printer',1)
pp1 = Machine.Machine(env,'PP1','PickandPlace1 ',1)
pp2 = Machine.Machine(env,'PP2','PickandPlace2 ',1)
rfo = Machine.Machine(env,'RFO','Reflow-Oven   ',1)
print('-------------------------------------------------------------------')

print('      ')
print('-------------------------------------------------------------------')
print('MACHINE BEHAVIOR')
print('-------------------------------------------------------------------')

for i in range(0,len(dt_inpcsvfile)-1):
    
    if (pcbobj[i].ldr_entry >= 0) & (pcbobj[i].ldr_exit >= 0):
        env.process(ldr.behavior(env,pcbobj[i].pcb_id,pcbobj[i].ldr_entry,pcbobj[i].ldr_exit,pcbobj[i+1].ldr_entry))
        
    if (pcbobj[i].spr_entry >= 0) & (pcbobj[i].spr_exit >= 0):    
        env.process(spr.behavior(env,pcbobj[i].pcb_id,pcbobj[i].spr_entry,pcbobj[i].spr_exit,pcbobj[i+1].spr_entry))
    
    if (pcbobj[i].pp1_entry >= 0) & (pcbobj[i].pp1_exit >= 0):
        env.process(pp1.behavior(env,pcbobj[i].pcb_id,pcbobj[i].pp1_entry,pcbobj[i].pp1_exit,pcbobj[i+1].pp1_entry))
    
    if (pcbobj[i].pp2_entry >= 0) & (pcbobj[i].pp2_exit >= 0):
        env.process(pp2.behavior(env,pcbobj[i].pcb_id,pcbobj[i].pp2_entry,pcbobj[i].pp2_exit,pcbobj[i+1].pp2_entry))
    
    if (pcbobj[i].rfo_entry >= 0) & (pcbobj[i].rfo_exit >= 0):
        env.process(rfo.behavior(env,pcbobj[i].pcb_id,pcbobj[i].rfo_entry,pcbobj[i].rfo_exit,pcbobj[i+1].rfo_entry))

#end-for

i += 1
if (pcbobj[i].ldr_entry >= 0) & (pcbobj[i].ldr_exit >= 0):
    env.process(ldr.behavior(env,pcbobj[i].pcb_id,pcbobj[i].ldr_entry,pcbobj[i].ldr_exit,MAX_SIM_TIME))

if (pcbobj[i].spr_entry >= 0) & (pcbobj[i].spr_exit >= 0):
    env.process(spr.behavior(env,pcbobj[i].pcb_id,pcbobj[i].spr_entry,pcbobj[i].spr_exit,MAX_SIM_TIME))

if (pcbobj[i].pp1_entry >= 0) & (pcbobj[i].pp1_exit >= 0):    
    env.process(pp1.behavior(env,pcbobj[i].pcb_id,pcbobj[i].pp1_entry,pcbobj[i].pp1_exit,MAX_SIM_TIME))

if (pcbobj[i].pp2_entry >= 0) & (pcbobj[i].pp2_exit >= 0):    
    env.process(pp2.behavior(env,pcbobj[i].pcb_id,pcbobj[i].pp2_entry,pcbobj[i].pp2_exit,MAX_SIM_TIME))

if (pcbobj[i].rfo_entry >= 0) & (pcbobj[i].rfo_exit >= 0):    
    env.process(rfo.behavior(env,pcbobj[i].pcb_id,pcbobj[i].rfo_entry,pcbobj[i].rfo_exit,MAX_SIM_TIME))


env.run(until=MAX_SIM_TIME)

print('-----------------------------------------')
print('PCB-IDs processed by different machines')
print('-----------------------------------------')
print('LDR ||', ldr.pcbid_proc_list)
print('SPR ||', spr.pcbid_proc_list)
print('PP1 ||', pp1.pcbid_proc_list)
print('PP2 ||', pp2.pcbid_proc_list)
print('RFO ||', rfo.pcbid_proc_list)
print('-----------------------------------------')

print(' ')
print('------------------------------------------------------------------------')
print('PCB FLOW CLASSIFICATION')
print('------------------------------------------------------------------------')
for i in range(0,len(dt_inpcsvfile)):
    print('PCB-ID :', pcbobj[i].pcb_id, '|', routine_pattern_decoder.pattern_decoder(pcbobj[i].pcb_pattern))
#end-for
print('------------------------------------------------------------------------')
