# Tara O'Kelly - G00322214
# Emerging Technologies, Year 4, Software Development, GMIT.

# Problem set: Read the MNIST data files
# 1. Download the image and label files. Have Python decompress and read them byte by byte into appropriate data structures in memory.

# https://docs.python.org/3/library/gzip.html
# reads and writes gzip-format files, automatically compressing or decompressing the data so that it looks like an ordinary file object.
import gzip

def main():
    train_labels= read_labels_from_file('../data/train-labels-idx1-ubyte.gz')
    test_labels= read_labels_from_file('../data/t10k-labels-idx1-ubyte.gz')
    train_images= read_images_from_file('../data/train-images-idx3-ubyte.gz')
    test_images= read_images_from_file('../data/t10k-images-idx3-ubyte.gz')

    for row in train_images[4999]:
        for col in row:
            print('.' if col <= 127 else '#', end='')
        print()

def read_labels_from_file(filename):
    with gzip.open(filename,'rb') as f:

        # read first four bytes
        magic = f.read(4)
        magic = int.from_bytes(magic, 'big')
        print("Magic: ", magic)

        # read in number of labels
        nolab = f.read(4)
        nolab = int.from_bytes(nolab, 'big')
        print("Labels: ", nolab)

        # read in labels
        labels = [f.read(1) for i in range(nolab)]
        # convert array of bytes to array of strings
        return [int.from_bytes(label,'big') for label in labels]

def read_images_from_file(filename):
    with gzip.open(filename,'rb') as f:

        # read first four bytes
        magic = f.read(4)
        magic = int.from_bytes(magic, 'big')
        print("Magic: ", magic)

        # read in number of images
        noimg = f.read(4)
        noimg = int.from_bytes(noimg, 'big')
        print("Images: ", noimg)

        # read in number of rows
        norow = f.read(4)
        norow = int.from_bytes(norow, 'big')
        print("Rows: ", norow)

        # read in number of columns
        nocol = f.read(4)
        nocol = int.from_bytes(nocol, 'big')
        print("Columns: ", nocol)

        images = []

        # use the number of images, row and columns to create an array of images, 
        # reading in one byte at a time and converting it to an int
        for i in range(noimg):
            rows = []
            for r in range(norow):
                cols = []
                for c in range(nocol):
                    cols.append(int.from_bytes(f.read(1),'big'))
                rows.append(cols)
            images.append(rows)
        return images

if __name__ == '__main__':
    main()