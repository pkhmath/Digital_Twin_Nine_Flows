#******************************************************************************************************************************************
# TITLE     : ROUTINE_PATTERN_DECODER
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

def pattern_decoder(inp_pattern):
    switcher = {
        11111 : 'Flow01 : LDR entry : Perfect flow through the line'
       ,11000 : 'Flow02 : LDR entry : PCB disappeared after SPR exit'
       ,11110 : 'Flow03 : LDR entry : PCB disappeared after PP2 exit'
       ,1111  : 'Flow04 : SPR entry : PCB full flow through partial line'
       ,1000  : 'Flow05 : SPR entry : PCB disappeared after SPR exit'
       ,1110  : 'Flow06 : SPR entry : PCB disappeared after PP2 exit'
       ,111   : 'Flow07 : PP1 entry : PCB full flow through partial line'
       ,110   : 'Flow08 : PP1 entry : PCB disappeared after PP2 exit'
       ,1     : 'Flow09 : RFO entry : PCB passed through only one machine'
    }
    return switcher.get(inp_pattern,'invalid pattern')
#end-proc