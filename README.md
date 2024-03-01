# SBND Channel Mapping Tool

```channel_mapping.xlsx``` contains a complete map of wires to front-end hardware

## **Plotting Wire Plane Views** 

```plotprojections.py``` contains functions to plot different wire plane views of warm electronics hardware groupings

**To plot wires corresponding to a set of FEMBs in a WIB: ```python plotprojections.py FEMB --wibcrate <WIB_CRATE_NUMBER> --wib <WIB_NUMBER> --fembs <FEMB_NUMBER_1> <FEMB_NUMBER_2>```**

Inputs:

```--wibcrate```: Specify the WIB crate number (between 1-4). (e.g., --wibcrate 3)

```--wib```: Specify the WIB number (between 1-6). (e.g., --wib 2)

```--fembs```: Specify the WIB numbers separated by spaces (between 0-4). (e.g., --fembs 0 1)

**To plot wires corresponding to a set of WIBs in a WIB crate: ```python plotprojections.py WIB --wibcrate <WIB_CRATE_NUMBER> --wibs <WIB_NUMBER_1> <WIB_NUMBER_2>```**

Inputs:

```--wibcrate```: Specify the WIB crate number (between 1-4). (e.g., --wibcrate 3)

```--wibs```: Specify the WIB numbers separated by spaces (between 1-6). (e.g., --wibs 2 4 5)

**To plot wires corresponding to a set of FEMs in a TPC crate: ```python plotprojections.py FEM --tpccrate <TPC_CRATE_NUMBER> --fems <FEM_NUMBER_1> <FEM_NUMBER_2>...```**

Inputs:

```--tpccrate```: Specify the TPC crate number (between 1-11). (e.g., --tpccrate 10)

```--fems```: Specify the FEM numbers separated by spaces (between 1-16). (e.g., --fems 10 11 12)

**To plot wires corresponding to a list of LArSOFT Channels: ```python plotprojections.py LArSOFT --offlinech <LArSOFTch.txt> $```**

Inputs:

```--offlinech```: Provide a ```.txt``` file with a set of offline channels (between 1-11264). (e.g., samplech.txt)

## **Printing Upstream Info**

```printinfo.py``` contains functions to return the upstream info corresponding to TPC hardware and offline channels

**To print TPC wires, FEMB & WIB info corresponding to a set of FEMs in a TPC crate: ```python printinfo.py FEM --tpccrate <TPC_CRATE_NUMBER> --fems <FEM_NUMBER_1> <FEM_NUMBER_2>...```**

Inputs:

```--tpccrate```: Specify the TPC crate number (between 1-11). (e.g., --tpccrate 10)

```--fems```: Specify the FEM numbers separated by spaces (between 1-16). (e.g., --fems 10 11 12)

**To print TPC wires, FEMB, WIB & FEM info corresponding to a list of LArSOFT Channels: ```python printinfo.py LArSOFT --offlinech <LArSOFTch.txt> $```**

Inputs:

```--offlinech```: Provide a ```.txt``` file with a set of offline channels (between 1-11264). (e.g., samplech.txt)

