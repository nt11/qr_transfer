import random

if __name__ == "__main__":
    x = []
    for i in range(0, 1300):
        x.append(int(255*random.random()))

    with open("input_file.txt", "wb") as fid:
        fid.write(bytes(x))
