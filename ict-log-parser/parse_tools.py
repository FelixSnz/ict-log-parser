from anytree import Node

def _extract_node_name(log_str):
    """Extract the node name from the log string."""
    node_name = ""
    while len(log_str) > 0 and log_str[0] != '|':
        node_name += log_str[0]
        log_str = log_str[1:]
    return node_name, log_str[1:]


def _create_unique_node(node_name, parent_node:Node, sibling_count:dict) -> Node:
    """Create a unique node based on the node name and sibling count."""
    count = sibling_count.get(node_name, 0)
    unique_node_name = f"{node_name}_{count}" if count > 0 else node_name
    sibling_count[node_name] = count + 1
    return Node(unique_node_name, parent=parent_node, data="")


def parse_log(log_str, parent_node:Node):
    """
    Parse a log string into a tree structure.
    
    Parameters:
        log_str (str): The log string to be parsed.
        parent_node (Node): The parent node for this log string.
        
    Returns:
        str: Remaining log string after parsing.
    """
    sibling_count = {}  # Reset count for each new set of sibling nodes
    buffer = ""
    
    while len(log_str) > 0:
        char = log_str[0]
        log_str = log_str[1:]

        if char == '{':
            node_name, log_str = _extract_node_name(log_str)
            node = _create_unique_node(node_name, parent_node, sibling_count)
            log_str = parse_log(log_str, node)

        elif char == '}':
            if buffer:
                parent_node.data = buffer.strip()
                buffer = ""
            return log_str

        else:
            buffer += char

    if buffer:
        parent_node.data = buffer.strip()

    return log_str