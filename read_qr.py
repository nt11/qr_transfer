import cv2
import sys
import base64
import binascii


def read_qr_code(filename):
    """Read an image and read the QR code.
    from
    Args:
        filename (string): Path to file
    
    Returns:
        qr (string): Value from QR code
    """

    try:
        img = cv2.imread(filename)
        detect = cv2.QRCodeDetector()
        value, points, straight_qrcode = detect.detectAndDecode(img)
        return value
    except:
        return


def usage(arg):
    print("Usage:")
    print("%s <input_file_qr_without_extension> <extension> <output_file>" % arg[0])
    sys.exit()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        usage(sys.argv)
    i = 0
    accumulate = b""
    while True:
        try:
            fname = "%s_%d.%s" % (sys.argv[1], i, sys.argv[2])
            print("reading %s" % fname)
            out = read_qr_code(fname)  # Decode QR file
            if not out:
                print ("Unable to read file %s" % fname)
                sys.exit()
            data = base64.b64decode(out)  # extract data
            serial = data[0]
            if serial != i:
                print("Wrong serial file %s got %d, should be %d" % (fname, serial, i))
                break
            checksum = data[-4:]  # extract checksum
            data_checksum = binascii.crc32(data[:-4]).to_bytes(4)  # Compute checksum on data and serial
            if checksum != data_checksum:  # compare checksums
                print("Wrong checksum file %s received %s, data_checksum %s" % (fname, checksum, data_checksum))
                break

            accumulate += data[1:-4]  # Remove serial and checksum before concatenating
            i += 1
        except:
            print("not found")
            break

    with open(sys.argv[3], "wb") as fid:
        fid.write(accumulate)
