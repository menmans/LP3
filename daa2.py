class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ""

    def print_nodes(self, val=""):
        new_val = val + str(self.huff)
        if self.left:
            self.left.print_nodes(new_val)
        if self.right:
            self.right.print_nodes(new_val)
        if not self.left and not self.right:
            print(f"{self.symbol} -> {new_val}")

# List of characters and their corresponding frequencies
chars = ["a", "b", "c", "d", "e", "f"]
freq = [50, 10, 30, 5, 3, 2]

# Creating initial nodes for each character
nodes = [Node(freq[i], chars[i]) for i in range(len(chars))]

# Building the Huffman Tree
while len(nodes) > 1:
    # Sort nodes based on frequency
    nodes = sorted(nodes, key=lambda x: x.freq)

    # Select the two nodes with the smallest frequency
    left = nodes[0]
    right = nodes[1]

    # Assign binary values to the left and right nodes
    left.huff = "0"
    right.huff = "1"

    # Create a new node with combined frequency and symbol
    new_node = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)

    # Remove the two nodes and add the new node
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(new_node)

# Print characters and their frequencies
print("Characters :", chars)
print("Frequencies:", freq)
print("\nHuffman Encoding:")

# Print the Huffman codes from the root node
if nodes:
    nodes[0].print_nodes()
