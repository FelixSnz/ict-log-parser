from anytree import Node

class TreeLog:
    def __init__(self, path: str) -> None:
        with open(path, 'r') as f:
            self.log_str = f.read()

    def _extract_node_name(self, log_str: str):
        """Extract the node name from the log string."""
        node_name = ""
        while len(log_str) > 0 and log_str[0] != '|':
            node_name += log_str[0]
            log_str = log_str[1:]
        return node_name, log_str[1:]

    def _create_unique_node(self, node_name: str, parent_node: Node, sibling_count: dict) -> Node:
        """Create a unique node based on the node name and sibling count."""
        count = sibling_count.get(node_name, 0)
        unique_node_name = f"{node_name}_{count}" if count > 0 else node_name
        sibling_count[node_name] = count + 1
        return Node(unique_node_name, parent=parent_node, data="")

    def parse(self, parent_node: Node = None) -> str:
        """
        Parse a log string into a tree structure.
        """
        sibling_count = {}  # Reset count for each new set of sibling nodes
        buffer = ""

        while len(self.log_str) > 0:
            char = self.log_str[0]
            self.log_str = self.log_str[1:]

            if char == '{':
                node_name, self.log_str = self._extract_node_name(self.log_str)
                node = self._create_unique_node(node_name, parent_node, sibling_count)
                self.log_str = self.parse(node)

            elif char == '}':
                if buffer:
                    parent_node.data = buffer.strip()
                    buffer = ""
                return self.log_str

            else:
                buffer += char

        if buffer:
            parent_node.data = buffer.strip()

        return self.log_str