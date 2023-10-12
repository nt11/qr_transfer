import qrcode
import sys
import base64
import binascii


def usage(arg):
    """
    Displays Usage
    Args:
        arg: Input arguments from sys.argv

    Returns:

    """
    print("Usage:")
    print("%s <input_filename> <output_filename_without_extension> <len>" % arg[0])
    print("len should be less than or equal to 967")
    sys.exit()


if __name__ == "__main__":
    print("Hello World")
    if len(sys.argv) != 4:
        usage(sys.argv)
    chunk_len = int(sys.argv[3])
    if chunk_len > 967:  # This threshold has been tested on synthetic files
        print("Error: Chunk len has to be less than or equal to 967")
        sys.exit()
    if chunk_len > 512:
        print("Wraning: Chunk len greater than 512 might not transfer well on (phone) camera!")
    print(
        "Running on file %s, output to file %s.png with chunk size = %d" % (sys.argv[1], sys.argv[2], int(sys.argv[3])))
    with open(sys.argv[1], "rb") as fid:
        i = 0
        while True:
            raw_data = fid.read(chunk_len)
            if not raw_data:
                break
            data = i.to_bytes(1) + raw_data  # add file serial
            checksum = binascii.crc32(data)  # debug
            data = data + checksum.to_bytes(4)

            img = qrcode.make(base64.b64encode(data))
            type(img)  # qrcode.image.pil.PilImage
            fname = "%s_%d.png" % (sys.argv[2], i)
            print("Creating %s" % fname)
            img.save(fname)
            i += 1
            if i > 255:
                print("Too many file")
                break
