import os
import re
import pandas as pd
import numpy as np
from PIL import Image
from numpy import asarray
from numba import jit, cuda, vectorize


x = []
data = [[[[]]]]
path = 'python script/'

#Get numbers from image names
def get_numbers_from_filename(filename):
    return re.search(r'\d+', filename).group(0)

for filename in os.listdir('python script'):
    x.append(int(get_numbers_from_filename(filename)))

#Sorting and splitting the array for loop
x.sort()
#print(x)
print((len(x)))

x = list(dict.fromkeys((x)))
#print(x)
print((len(x)))

x.pop(0)
#print(x)
print((len(x)))

print(type(x))
print(type(x[0]))


#initializing data array with first 2 images
img = Image.open( path + '10_left.jpeg')
img_r = img.resize((100,80))
data1 = asarray(img_r)
data = np.array([data1]);
print(data.shape)

img = Image.open( path + '10_right.jpeg')
img_r = img.resize((100,80))
data1 = asarray(img_r)
data = np.append(data,[data1],axis=0);
print(data.shape)


#converting each image into numpy array and preprocessing
for i in x:
    try:
        print(i)
        img = Image.open(path + str(i) + "_left.jpeg")
        img_r = img.resize((100, 80))
        data1 = asarray(img_r)
        data = np.append(data,[data1],axis=0)
        #print(data.shape)

    except:
        print(str(i) + '_left has FAILED us !!!')
        pass
    try:
        img = Image.open(path + str(i) + "_right.jpeg")
        img_r = img.resize((100, 80))
        data1 = asarray(img_r)
        data = np.append(data, [data1], axis=0)
        #print(data.shape)
    except:
        print(str(i) + '_right has FAILED us !!!')
        pass

print(data.shape)
np.save('t_data',data)




