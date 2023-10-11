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

pip -m venv venv
pip install -r requirements.txt

- On PC/ Windows
Don't know
