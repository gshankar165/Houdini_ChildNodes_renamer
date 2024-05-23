To DO:
“
This tool retrieves all geo nodes and rename their child nodes by adding a prefix of the parent's name and a suffix with the child node type in short format.
This also show Childs in the UI using list widget.
For example:
If geo node name is 'head_GEO'
child Nodes: grid1, sculpt1, null1, smooth1
Rename child nodes as: head_grid1, head_sculpt1, head_null1
Lib : Python 2.7 and PySide2 “




Tool Help
Rename All Childs button: Rename all sub-children inside the geo nodes available in /obj context. Refresh_list button: Take the selection from Parent Combo box and shows all the Childs of the parent geo node inside the listWidget.
Code help

Main.py file has all the ui related functions mapped to button and all the cooking happening in Comm_func.py file.
To start, please change the base script directory to script folder. Run the code from “run_here()” function.
