# SBND Channel Mapping Tool

```channel_mapping.xlsx``` contains a complete map of wires to front-end hardware

To plot wires corresponding to a WIB: ```python channel_mapping.py plotWIBprojection(WIB_crate, WIB_no)```

    Input: WIB crate # (1-4) & WIB # (1-6)

To return wires corresponding to a WIB: ```python channel_mapping.py printwires(WIB_crate, WIB_no)```
    
    Input: WIB crate # (1-4) & WIB # (1-6)

To return a WIB corresponding to given wires: ```python channel_mapping.py printWIBs(wires)```
    
    Input: A 3D array of wires with U,V,Y dimension

To plot wires corresponding to a WIB fiber: ```python channel_mapping.py plotfiberprojection(WIB_crate, WIB_no, WIB_QFSP, WIB_fiber)```

    Input: WIB crate # (1-4), WIB # (1-6), 'DAQ1'/'DAQ2' & Fiber # (1/2)

To plot wires corresponding to an FEMB: ```python channel_mapping.py plotFEMBprojection(WIB_crate, WIB_no, FEMB_no)```
    
    Input: WIB crate # (1-4), WIB # (1-6) & FEMB # (1-3)
