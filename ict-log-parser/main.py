from anytree import Node, RenderTree
from tree_log import TreeLog
import os
from export import export as excel_export

log_folder_path = "log-samples"

def main():
    root = Node("root", data="")

    for log_path in os.listdir(log_folder_path):
        temp_tree_log = TreeLog(log_path)
        temp_tree_log.build_tree(root) # Now 'root' contains the tree structure of the log file

     #just to visualize the tree
    for pre, _, node in RenderTree(root):
        print(f"{pre}{node.name} {node.data if hasattr(node, 'data') else ''}")


    excel_export(root)


if __name__ == "__main__":
    main()
