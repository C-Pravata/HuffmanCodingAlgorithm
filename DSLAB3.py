# Open the output file in write mode
with open("output.txt", "w") as output_file:

    # Define a class for nodes in the Huffman Encoding Tree
    class HuffmanNode:
        def __init__(self, freq, symbol=None):
            self.freq = freq
            self.symbol = symbol
            self.left = None
            self.right = None

        # Define __lt__ method for sorting nodes in priority queue
        def __lt__(self, other):
            return self.freq < other.freq

    # Build Huffman Encoding Tree
    def build_huffman_tree(freq_table):
        pq = []
        for symbol, freq in freq_table.items():
            node = HuffmanNode(freq, symbol)
            pq.append(node)

        while len(pq) > 1:
            pq.sort()
            left_child = pq.pop(0)
            right_child = pq.pop(0)
            parent_freq = left_child.freq + right_child.freq
            parent = HuffmanNode(parent_freq)
            parent.left = left_child
            parent.right = right_child
            pq.append(parent)

        return pq[0]

    # Perform preorder traversal of Huffman Encoding Tree and generate codes
    def generate_codes(node, code="", code_table={}):
        if node.symbol:
            code_table[node.symbol] = code
        if node.left:
            generate_codes(node.left, code + "0", code_table)
        if node.right:
            generate_codes(node.right, code + "1", code_table)
        return code_table

    # Print the Huffman Encoding Tree in preorder traversal
    def print_tree(node, prefix="", is_left=True):
        if node:
            print(prefix + ("|-- " if is_left else "`-- ") + f"{node.symbol}:{node.freq}", file=output_file)
            prefix += "| " if is_left else " "
            print_tree(node.left, prefix, True)
            print_tree(node.right, prefix, False)

    # Encode a message using a given code table
    def encode_message(message, code_table):
        encoded_message = ""
        for char in message:
            encoded_message += code_table.get(char, "")
        return encoded_message

    # Decode a message using a given Huffman Encoding Tree
    def decode_message(encoded_message, huffman_tree):
        decoded_message = ""
        curr_node = huffman_tree
        for bit in encoded_message:
            if bit == "0":
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
            if curr_node.symbol:
                decoded_message += curr_node.symbol
                curr_node = huffman_tree
        return decoded_message

    # Read the frequency table from the file
    freq_table = {}
    with open("FreqTable.txt", "r") as f:
        for line in f:
            symbol, freq = line.strip().split(" - ")
            freq_table[symbol] = int(freq)

    # Build the Huffman Encoding Tree and generate codes
    huffman_tree = build_huffman_tree(freq_table)
    code_table = generate_codes(huffman_tree)

    # Print the Huffman Encoding Tree
    print("Huffman Encoding Tree:", file=output_file)
    print_tree(huffman_tree)

    # Print the resulting encoding generated by the tree
    print("The code is:", file=output_file)
    for symbol, code in sorted(code_table.items(), key=lambda x: (len(x[0]), x[0])):
        print(f"{symbol} = {code}", file=output_file)

    def encode_message(line, code_table):
        encoded_message = ""
        for symbol in line:
            encoded_message += code_table[symbol]
        return encoded_message

    def decode_message(encoded_message, huffman_tree):
        decoded_message = ""
        node = huffman_tree
        for bit in encoded_message:
            if bit == "0":
                node = node.left
            else:
                node = node.right
            if node.symbol:
                decoded_message += node.symbol
                node = huffman_tree
        return decoded_message

    def huffman_encoding(lines):
        freq_table = {}
        for line in lines:
            for symbol in line:
                freq_table[symbol] = freq_table.get(symbol, 0) + 1

        huffman_tree = build_huffman_tree(freq_table)
        code_table = generate_codes(huffman_tree)

        for i, line in enumerate(lines):
            # Mark the line number
            print(f"Line {i+1}: {line.strip()}", file=output_file)

            # Encode and print the encoded message
            encoded_message = encode_message(line, code_table)
            print(f"Encoded message: {encoded_message}", file=output_file)

            # Decode and print the original message
            decoded_message = decode_message(encoded_message, huffman_tree)
            print(f"Decoded message: {decoded_message}\n", file=output_file)

    # Open and read the input files
    with open("ClearText.txt", "r") as file:
        clear_lines = file.readlines()

    with open("AdditionalClearText.txt", "r") as additional_file:
        additional_lines = additional_file.readlines()

    # Concatenate the lines from both files
    lines = clear_lines + additional_lines

    # Encode and decode the lines using the Huffman Encoding Tree
    huffman_encoding(lines)

    # Open and read the encoded text files
    with open("Encoded.txt", "r") as file:
        encoded_lines = file.readlines()

    with open("AdditionalEncoded.txt", "r") as additional_file:
        additional_encoded_lines = additional_file.readlines()
    
        # Decode each line separately using the same Huffman Encoding Tree and code table
    for i, line in enumerate(encoded_lines + additional_encoded_lines):
        # Mark the line number
        print(f"Line {i+1}: {line.strip()}", file=output_file)

        # Decode and print the original message
        decoded_message = decode_message(line.strip(), huffman_tree)
        print(f"Decoded message: {decoded_message}\n", file=output_file)