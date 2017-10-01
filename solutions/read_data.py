# https://docs.python.org/3/library/gzip.html
# reads and writes gzip-format files, automatically compressing or decompressing the data 
# so that it looks like an ordinary file object
import gzip

def main():
    train_labels= read_labels_from_file('../data/train-labels-idx1-ubyte.gz')
    test_labels= read_labels_from_file('../data/t10k-labels-idx1-ubyte.gz')

def read_labels_from_file(filename):
    with gzip.open(filename,'rb') as f:

        # read first four bytes
        magic = f.read(4)
        magic = int.from_bytes(magic, 'big')
        print("Magic: ", magic)

        nolab = f.read(4)
        nolab = int.from_bytes(nolab, 'big')
        print("Labels: ", nolab)

        # read in labels
        labels = [f.read(1) for i in range(nolab)]
        # convert array of bytes to array of strings
        return [int.from_bytes(label,'big') for label in labels]

if __name__ == '__main__':
    main()