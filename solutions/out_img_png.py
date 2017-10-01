# Tara O'Kelly - G00322214
# Emerging Technologies, Year 4, Software Development, GMIT.

# Problem set: Read the MNIST data files
# 3. Use Python to output the image files as PNGs, saving them in a subfolder in your repository. Name the images in the format train-XXXXX-Y.png or test-XXXXX-Y.png where XXXXX is the image number (where it occurs in the data file) and Y is its label. For instance, the five-thousandth training image is labelled 2, so its file name should be train-04999-2.png. Note the images are indexed from 0, so the five-thousandth image is indexed as 4999. See below for an example of it. Commit these image files to GitHub.

# https://docs.python.org/3/library/gzip.html
# reads and writes gzip-format files, automatically compressing or decompressing the data so that it looks like an ordinary file object.
import gzip
from PIL import Image
import numpy as np

def main():
    esc = False
    train_labels= read_labels_from_file('../data/train-labels-idx1-ubyte.gz')
    test_labels= read_labels_from_file('../data/t10k-labels-idx1-ubyte.gz')
    train_images= read_images_from_file('../data/train-images-idx3-ubyte.gz')
    test_images= read_images_from_file('../data/t10k-images-idx3-ubyte.gz')

    while not esc:
        img_num = int(input("\n[Enter -1 to ESC]\nEnter img number you wish to save:\n"))
        if(img_num == -1):
            esc = True
        elif(img_num >= len(train_images) or img_num < 0):
            print("Invalid number.")
        else:
            img = Image.fromarray(np.array(train_images[img_num]))
            img = img.convert('RGB')
            img_filename = "../img/"+str(img_num).zfill(5)+"-"+str(train_labels[img_num])+".png"
            img.save(img_filename)
    print("Goodbye!")

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