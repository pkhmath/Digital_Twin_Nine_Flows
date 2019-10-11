#******************************************************************************************************************************************
# TITLE     : PCB
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

NEG_NUM = -1000

class PCB:
    def __init__(self,pcb_id,ldr_entry,ldr_exit,spr_entry,spr_exit,pp1_entry,pp1_exit,pp2_entry,pp2_exit,rfo_entry,rfo_exit):
        self.pcb_id      = pcb_id
        self.ldr_entry   = ldr_entry
        self.ldr_exit    = ldr_exit
        self.spr_entry   = spr_entry
        self.spr_exit    = spr_exit
        self.pp1_entry   = pp1_entry
        self.pp1_exit    = pp1_exit
        self.pp2_entry   = pp2_entry
        self.pp2_exit    = pp2_exit
        self.rfo_entry   = rfo_entry
        self.rfo_exit    = rfo_exit
        
        self.pcb_pattern = 00000
        if (self.ldr_entry >= 0): self.pcb_pattern += 10000 
        if (self.spr_entry >= 0): self.pcb_pattern += 1000
        if (self.pp1_entry >= 0): self.pcb_pattern += 100
        if (self.pp2_entry >= 0): self.pcb_pattern += 10
        if (self.rfo_entry >= 0): self.pcb_pattern += 1
        
        print('Finished initializing the object with pcb_id =', pcb_id)
    #end-proc
    
    def update_parms(self,flow_no):
        if (flow_no == 1):
            pass   #No poperation
        
        elif (flow_no == 2):
            self.pp1_entry = NEG_NUM; self.pp1_exit = NEG_NUM;
            self.pp2_entry = NEG_NUM; self.pp2_exit = NEG_NUM;
            self.rfo_entry = NEG_NUM; self.rfo_exit = NEG_NUM;
            
        elif (flow_no == 3):
            self.rfo_entry = NEG_NUM; self.rfo_exit = NEG_NUM;
            
        elif (flow_no == 4):
            self.ldr_entry = NEG_NUM; self.ldr_exit = NEG_NUM;
            
        elif (flow_no == 5):
            self.ldr_entry = NEG_NUM; self.ldr_exit = NEG_NUM;
            self.pp1_entry = NEG_NUM; self.pp1_exit = NEG_NUM;
            self.pp2_entry = NEG_NUM; self.pp2_exit = NEG_NUM;
            self.rfo_entry = NEG_NUM; self.rfo_exit = NEG_NUM;
            
        elif (flow_no == 6):
            self.ldr_entry = NEG_NUM; self.ldr_exit = NEG_NUM;
            self.rfo_entry = NEG_NUM; self.rfo_exit = NEG_NUM;
            
        elif (flow_no == 7):
            self.ldr_entry = NEG_NUM; self.ldr_exit = NEG_NUM;
            self.spr_entry = NEG_NUM; self.spr_exit = NEG_NUM;
            
        elif (flow_no == 8):
            self.ldr_entry = NEG_NUM; self.ldr_exit = NEG_NUM;
            self.spr_entry = NEG_NUM; self.spr_exit = NEG_NUM;
            self.rfo_entry = NEG_NUM; self.rfo_exit = NEG_NUM;
            
        elif (flow_no == 9):
            self.ldr_entry = NEG_NUM; self.ldr_exit = NEG_NUM;
            self.spr_entry = NEG_NUM; self.spr_exit = NEG_NUM;
            self.pp1_entry = NEG_NUM; self.pp1_exit = NEG_NUM;
            self.pp2_entry = NEG_NUM; self.pp2_exit = NEG_NUM;
           
        else:
            print('Invalid flow number =', flow_no)
            return
        #end-if 
            
    #end-proc
    
    def update_pattern(self):
        self.pcb_pattern = 00000
        if (self.ldr_entry >= 0): self.pcb_pattern += 10000 
        if (self.spr_entry >= 0): self.pcb_pattern += 1000
        if (self.pp1_entry >= 0): self.pcb_pattern += 100
        if (self.pp2_entry >= 0): self.pcb_pattern += 10
        if (self.rfo_entry >= 0): self.pcb_pattern += 1
    #end-proc
    
    def print_parms(self):
        print( \
        '|| PCB |', self.pcb_id, \
        '|| LDR |', self.ldr_entry, ':', self.ldr_exit, \
        '|| SPR |', self.spr_entry, ':', self.spr_exit, \
        '|| PP1 |', self.pp1_entry, ':', self.pp1_exit, \
        '|| PP2 |', self.pp2_entry, ':', self.pp2_exit, \
        '|| RFO |', self.rfo_entry, ':', self.rfo_exit, \
        '|| Pattern |', self.pcb_pattern
        )
    #end-proc
#end-class