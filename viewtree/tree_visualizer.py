from graphviz import Digraph
from IPython.display import Image, display

def visualize_tree(root):
    """
    Visualizes a binary tree using Graphviz with proper spacing, alignment, and uniform node sizes.
    Distinguishes left and right child nodes but does not display labels on the edges.
    :param root: The root node of the binary tree.
    """
    dot = Digraph()
    dot.attr(
        rankdir='TB',
        splines='line',
        nodesep='0.6',       # Increase node separation
        ranksep='0.4',       # Increase rank separation
        pad='0.20',             # Add padding around the whole graph
        fontsize='10'        # Font size for labels
    )
    dot.attr('node', shape='circle', fixedsize='true', width='0.5', height='0.5', fontsize='10')  # Uniform node size
    dot.attr('edge', fontsize='10', labeljust='c', labelloc='t')  # Center and top-align edge labels

    def add_nodes_edges(node):
        if not node:
            return
        # Add the current node
        dot.node(str(id(node)), str(node.elem))

        # Add the left child
        if node.left:
            dot.edge(str(id(node)), str(id(node.left)))  # No label here
            add_nodes_edges(node.left)
        # else:
        #     # Add gray "None" text with no background and no padding
        #     dot.node(str(id(node)) + "_L", label="None", fontcolor="gray", style="solid", shape="plaintext", width="0.5", height="0.25", fontsize='10')
        #     # Color the edge to the "None" node gray, reduce its width, and set the label color to gray
        #     dot.edge(str(id(node)), str(id(node)) + "_L", color="gray", penwidth="0.5", fontcolor="gray")

        # Add the right child
        if node.right:
            dot.edge(str(id(node)), str(id(node.right)))  # No label here
        #     add_nodes_edges(node.right)
        # else:
        #     # Add gray "None" text with no background and no padding
        #     dot.node(str(id(node)) + "_R", label="None", fontcolor="gray", style="solid", shape="plaintext", width="0.5", height="0.25", fontsize='10')
        #     # Color the edge to the "None" node gray, reduce its width, and set the label color to gray
        #     dot.edge(str(id(node)), str(id(node)) + "_R", color="gray", penwidth="0.5", fontcolor="gray")

    add_nodes_edges(root)
    return dot

def viewTree(root):
    # Visualize the tree
    tree_visualization = visualize_tree(root)
    # Render the tree as a PNG and display it inline
    tree_visualization.render("binary_tree", format="png", cleanup=False)  # Save the PNG
    display(Image(filename="binary_tree.png"))  # Display the PNG in the notebook
