## Huffman Encoding  and Decoding

This  Python code  implements Huffman encoding and decoding for text messages. The  Huffman algorithm  is a  lossless data compression algorithm  that assigns shorter codes to more frequently occurring symbols in a message. The algorithm builds a  binary tree  called the  Huffman encoding tree, in which each leaf node represents a symbol and the path from the root to a leaf node represents the code for that symbol.

### Getting Started

To use this code, follow these steps:

1.  Clone or download this repository to your local machine.
2.  Make sure you have Python 3.x installed on your machine.
3.  Open a terminal or  command prompt  and navigate to the directory containing the cloned or downloaded repository.
4.  Run the command  `python huffman_encoding.py`  to execute the program.
5.  The output will be written to the  `output.txt`  file in the same directory.

### Input File Format

The program requires the following input files to be present in the same directory as the Python code:

-   `ClearText.txt`: A  text file  containing the original messages to be encoded and decoded. Each line in the file represents a separate message.
-   `AdditionalClearText.txt`: A text file containing additional messages to be encoded and decoded. Each line in the file represents a separate message.
-   `FreqTable.txt`: A text file containing the  frequency table  of symbols in the messages. Each line in the file should be in the format  `<symbol> <frequency>`, where  `<symbol>`  is a single character and  `<frequency>`  is an integer representing the  frequency count  of that symbol in the messages. The lines should be sorted in descending order of frequency.

For example, the  `FreqTable.txt`  file might look like this:

```
e 100
t 70
a 60
o 50
i 45
n 40
s 35
r 30
h 25
d 20
l 15
u 10
c 5
m 3
f 2
p 1

```

### Output

The program outputs the following files:

-   `EncodedMessages.txt`: A text file containing the Huffman-encoded messages. Each line in the file represents a separate message.
-   `DecodedMessages.txt`: A text file containing the Huffman-decoded messages. Each line in the file represents a separate message.

The program also prints the following information to the console:

-   The size of the original message in bits.
-   The size of the Huffman-encoded message in bits.
-   The  compression ratio  achieved by Huffman encoding.

### Implementation Details

The code consists of the following parts:

#### Building the Huffman Encoding Tree

The  `build_huffman_tree`  function takes a frequency table of symbols in the message and their frequencies, and constructs the corresponding Huffman encoding tree using a priority queue. The  `HuffmanNode`  class represents a node in the tree, and has fields for the symbol, frequency, left child, and right child. The  priority queue  is implemented using a list, and the  `__lt__`  method is defined for sorting the nodes by their frequencies.

#### Generating the Code Table

The  `generate_codes`  function performs a  preorder traversal  of the Huffman encoding tree and generates the  code table, which is a  dictionary mapping  symbols to their codes. The code for a symbol is obtained by concatenating the "0" and "1" bits along the path from the root to the leaf node representing that symbol.

#### Encoding and Decoding Messages

The  `encode_message`  function takes a message and the code table, and returns the corresponding encoded message. The  `decode_message`  function takes an  encoded message  and the Huffman encoding tree, and returns the original message by traversing the tree according to the encoded bits.

#### Main Program

The main program reads the frequency table from a file called  `FreqTable.txt`, builds the Huffman encoding tree and generates the code table, and prints the Huffman encoding tree and the code table to an output file called  `output.txt`.

The program then reads the  input files  `ClearText.txt`  and  `AdditionalClearText.txt`  that contain the  text messages  to be encoded and decoded. It concatenates the lines from both files, and encodes and decodes each line separately using the same Huffman encoding tree and code table. The  encoded messages  are written to files called  `EncodedMessages.txt`  and  `AdditionalEncodedMessages.txt`.

Finally, the program reads the  encoded message files, decodes each line separately, and writes the decoded messages to the output file. Each  decoded message  is preceded by the corresponding  line number  and a label indicating whether the message was from the original file or the additional file.

### Usage

To use the program, make sure that the input files  `ClearText.txt`,  `AdditionalClearText.txt`, and  `FreqTable.txt`  are in the same directory as the Python code. Then, run the code using a Python interpreter. The output will be written to the  `output.txt`  file in the same directory.

Note: This program assumes that the  input messages  contain only  printable ASCII characters, and that the  frequency table file  contains one line per symbol in the format  `symbol - frequency`. If the input messages or frequency table have different formats, the code may need to be modified accordingly.