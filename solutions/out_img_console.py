# Tara O'Kelly - G00322214
# Emerging Technologies, Year 4, Software Development, GMIT.

# Problem set: Read the MNIST data files
# 2. Output the third image in the training set to the console. Do this by representing any pixel value less than 128 as a full stop and any other pixel value as a hash symbol.

# https://docs.python.org/3/library/gzip.html
# reads and writes gzip-format files, automatically compressing or decompressing the data so that it looks like an ordinary file object.
import gzip

def main():
    invalid = True
    files = [['../data/t10k-labels-idx1-ubyte.gz', '../data/t10k-images-idx3-ubyte.gz', 'test'], ['../data/train-labels-idx1-ubyte.gz', '../data/train-images-idx3-ubyte.gz', 'train']]

    while invalid:
        name_num = int(input("\n[Enter -1 to ESC]\nEnter:\n1 - for "+ files[0][2] +"\n2 - for "+ files[1][2] +"\n"))
        if(name_num == 1 or name_num == 2):
            print("Opening " + files[name_num-1][2] + "_images...")
            menu(read_labels_from_file(files[name_num-1][0]),read_images_from_file(files[name_num-1][1]),files[name_num-1][2])
        elif(name_num == -1):
            invalid = False
    print("Goodbye!")

def menu(array_labels, array_images, name):
    esc = False
    while not esc:
        img_num = int(input("\n[Enter -1 to ESC]\nEnter img number you wish to print to console:\n"))
        if(img_num == -1):
            esc = True
        elif(img_num >= len(array_images) or img_num < 0):
            print("Invalid number.")
        else:
            print("Label: ",array_labels[img_num])
            for row in array_images[img_num]:
                for col in row:
                    # print . or # then a space
                    print('.' if col <= 127 else '#', end='')
                # newline and the end of row
                print()
    print("Exiting " + name + "_images...")

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