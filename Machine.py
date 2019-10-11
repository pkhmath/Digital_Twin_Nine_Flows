#******************************************************************************************************************************************
# TITLE     : MACHINE
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

import queue
import numpy as np

class Machine:
    
    def __init__(self,env,machine_id,machine_name,max_queue_length):
        self.machine_id       = machine_id
        self.machine_name     = machine_name
        self.max_queue_length = max_queue_length
        
        #Create queue object
        self.qobj = queue.Queue(max_queue_length)
        
        #Create an empty list for PCB-Ids that have been processed by the machine
        self.pcbid_proc_list = []
        
        print(env.now, '|| Constructor of', self.machine_id, '|', self.machine_name, '| Max Queue Length =', self.max_queue_length)
    #end-proc
    
    def behavior(self,env,curr_pcb_id,curr_pcb_entry,curr_pcb_exit,next_pcb_entry):     
        
        print(env.now, '||', self.machine_id, '|', 'Curr-PCB-ID =', curr_pcb_id, '|', 'Curr-PCB-Entry =', curr_pcb_entry, '|', 'Curr-PCB-Exit =', curr_pcb_exit, '|', 'Next-PCB-Entry =', next_pcb_entry)
    
        if (env.now < curr_pcb_entry):
            self.machine_state = 'IDLE'
            print(env.now, '||', self.machine_id, '|', 'Machine state =', self.machine_state)
            print('-------------------------------------------------------------------')
            yield env.timeout(curr_pcb_entry - env.now)
        #end-if    
        
        if (self.machine_state == 'IDLE'):
            self.qobj.put(curr_pcb_id)
            self.machine_state = 'PROCESSING'
            print(env.now, '||', self.machine_id, '| Added PCB', curr_pcb_id, 'to queue | Current queue size =', self.qobj.qsize(), '| Machine state =', self.machine_state)
            yield env.timeout(curr_pcb_exit - curr_pcb_entry)
        #end-if
        
        if (self.machine_state == 'PROCESSING'):
            removed_pcb_id = self.qobj.get()
            self.pcbid_proc_list = np.append(self.pcbid_proc_list,removed_pcb_id)
            self.machine_state = 'IDLE'
            print(env.now, '||', self.machine_id, '| Removed PCB', removed_pcb_id, 'from queue | Current queue size =', self.qobj.qsize(), '| Machine state =', self.machine_state) 
            if (next_pcb_entry >= 0):
                yield env.timeout(next_pcb_entry - curr_pcb_exit)
            else:
                yield env.timeout(0)
            #end-if    
        #end-if  
        
    #end-proc

#end-class