from anytree import Node, RenderTree
from parse_tools import parse_log
import os

log_folder_path = "log-samples"

root = Node("root", data="")

for log_file in os.listdir(log_folder_path):
    with open(os.path.join(log_folder_path, log_file), 'r') as f:
        log_str = f.read()

    parse_log(log_str, root)
    # Now 'root' contains the tree structure of the log file


for pre, _, node in RenderTree(root):
    print(f"{pre}{node.name} {node.data if hasattr(node, 'data') else ''}")
