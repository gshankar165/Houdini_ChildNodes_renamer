'''
This is the main file to run code.
The ui file is called and button fuctions are linked here.

Please Run the "run_here()" function to run the code.
'''


from PySide2 import QtCore, QtUiTools, QtWidgets
import sys
import hou
import os

# change this directory to script folder
base_dir = "/Users/gs/PycharmProjects/Houdini_ChildNodes_renamer"
hcr_ui_file = os.path.join(base_dir, "ui_files", "Houdini_Child_renamer.ui")

# import Comm_func.py file
sys.path.append(base_dir)
import Comm_func as com_func


def load_ui():
    # load the ui file here
    ui_loader = QtUiTools.QUiLoader()
    file = QtCore.QFile(hcr_ui_file)
    file.open(QtCore.QFile.ReadOnly)
    ui = ui_loader.load(file)
    file.close()
    return ui


class SLWidget(QtWidgets.QWidget):
    def __init__(self):
        super(SLWidget, self).__init__()
        self.ui = load_ui()

        # add parent nodes to combo box
        self.set_parent_combo_box()

        # button functions
        self.ui.rename_btn.clicked.connect(lambda: com_func.rename_all_child_nodes())
        self.ui.refresh_btn.clicked.connect(lambda: self.get_combo_box_sel())
        self.setParent(hou.ui.mainQtWindow(), QtCore.Qt.Window)


    def rename_btn(self):
        com_func.rename_all_child_nodes()

    def set_parent_combo_box(self):
        # set parents in combo box list
        # get parents list using create_parent_child_dict()
        # set each parent to combo box

        parent_node_list = com_func.create_parent_child_dict()
        for each_parent in parent_node_list.keys():
            self.ui.parent_comboBox.addItem(each_parent)
        return None

    def get_combo_box_sel(self):
        # get parent selection from combo box
        # create parent houdini node
        # get all childs inside parent node
        # set to listWidget box

        parent_sel = self.ui.parent_comboBox.currentText()
        parent_node_list = com_func.create_parent_child_dict()
        if parent_sel in parent_node_list.keys():
            parent_node = com_func.create_context(node_name=parent_sel, node_path=None)
            get_child_nodes = com_func.get_child_nodes(parent=parent_node)

            self.ui.child_listWidget.clear()
            for each_child in range(len(get_child_nodes)):
                child = get_child_nodes[each_child]
                self.ui.child_listWidget.addItem(child.name())


def run_here():
    win = SLWidget()
    win.ui.show()



run_here()















