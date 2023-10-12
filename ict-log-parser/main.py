from anytree import Node, RenderTree
from anytree.exporter import JsonExporter
from parse_tools import parse_log
import os
from export import export

log_folder_path = "log-samples"

root = Node("root", data="")

for log_file in os.listdir(log_folder_path):
    with open(os.path.join(log_folder_path, log_file), 'r') as f:
        log_str = f.read()

    parse_log(log_str, root)
    # Now 'root' contains the tree structure of the log file


for pre, _, node in RenderTree(root):
    print(f"{pre}{node.name} {node.data if hasattr(node, 'data') else ''}")


exporter = JsonExporter(indent=2, sort_keys=True)
json_data = exporter.export(root)

# Specify the full path where you want to save the .json file
# with open("out/tree.json", "w") as f:
#     f.write(json_data)

export(root)
