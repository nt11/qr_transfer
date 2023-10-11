# qr_transfer

This library creates a sequence of CRC and serial checked QR code sequence in order to transfer a small file (a few KB) and is able to decode the sequence of files

# Files include:
requirements.txt - Requirement file for virtual environment
make_random.py - Creates a random file of length 1300 bytes for testing
input_file.txt - A file created by make_random.py
make_qr.py - A program that makes a sequence of QR code png files from a binary file
read_qr.py - A program that reads, checks a sequence of QR png or jpg/jpeg files with QR codes to create an output file

# Environment
Tested on python 3.11

# Help
Running each file without parameters will show a usage help line

# Installation
- On Ubuntu or MacOS:

`pip -m venv venv`
`pip install -r requirements.txt`

- On PC/ Windows
Don't know

# Testing

**Run the following line to encode:**

`python3 make_qr.py input_file.txt output_qr 512`

**Output should be:**

Creating output_qr_0.png
Creating output_qr_1.png
Creating output_qr_2.png

**Run the following line to decode:**

`python3 read_qr.py output_qr png output_file.txt`

**Output should be:**

reading output_qr_0.png
reading output_qr_1.png
reading output_qr_2.png
reading output_qr_3.png
[ WARN:0@0.278] global loadsave.cpp:248 findDecoder imread_('output_qr_3.png'): can't open/read file: check file path/integrity
not found

(Ignore the last error, it is always there since the program is trying to read a non-existent file)

**Compare the input to output files:**

`diff input_file.txt output_file.txt`

Output should be empty

# Comments

- Up to 255 QR files are supported
- File order makes a difference! When downloading files make sure to label them xyz_0.jpeg, xyz_1.jpeg, etc. based on the order of creation
- Both file order and checksums are checked and if there is any error, the read_qr.py program will report this error. There is no overall checksum, so if the number of files transferred was incorrect, the program will not know this.
- Checked up to 512 bytes/QR code with iPhone13 max pro camera. Exceeding this number may cause QR codes to be transferred incorrectly
- This entire code was coded swiftly (~2 hours) and testing was scarce. Proceed with caution
- All testing was done with Python 3.11 on Mac OS
