# flood_exercise

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

This repo is for the Flood excercise and contains the following modules:
01 - cosntants variables <br />  
02 - utilities functios <br /> 
03 - basic statistics   <br />
04 - use NDWI for water detection  <br />
05 - Create TFRecord file <br /> 
06 - Train ML model   <br />

## Install

``` sh
pip install flood_exercise
```

## The use of NBDEV

This repository utilizes nbdev for development purposes. nbdev facilitates working with Jupyter notebooks and exporting them to .py files, enabling seamless module import and export within the Jupyter environment. The .py files are under "flood_exercise" folder, and the jupyter notebooks can be found in the "nbs" folder.  Explore additional advantages of using nbdev. [Click here for more information](https://nbdev.fast.ai/tutorials/tutorial.html)

## 03 basic statistics

The purpose of this module is to compute the basic statistics of the the dataset. 
The following variables are computed withing the class:
- number of images  
- per channel mean and standard devation  
- probability of water ( % of water pixels in each image, based on NDWI values)  
-Per train/dev/test sets and for the held-out region (Bolivia)


``` python
ImgsStatistics(path_to_imgs = r'D:\git\flood_exercise\S2',
                path_to_split_file= r'D:\git\flood_exercise\split\flood_handlabeled' )
```


## 04 NDWI
This module computes per-pixels probability of eater using the NDWI index.

- calculate NDWI per image based on the formula :
``` python  
B3-B8 / B3 + B8
```
- calculate optimal NDWI threshold - finds the maximum and minimum value of NDWI values based on the hand labels data. 

- calculate water probability per image - calclate the percentage of water pixels in each image based on NDWI threshold.

``` python
instance = ndwi(path_to_s2_tiles = r"D:\git\flood_exercise\S2",
                path_to_labeled_tiles= r"D:\git\flood_exercise\S2_HANDLABELED")
```

**CAUTION: The images provided are in L1-C (top of atmosphere). This representation does not accurately reflect surface reflectance, potentially impacting the precision of water pixel detection and compromising the results of any models.**

## 06 TFRecord 

This class is designed to convert GeoTIFF files into TFRecord format.
``` python
instance =  ConvertTRF(path_to_tif= r"D:\git\flood_exercise\S2" ,
                       path_save_trf= r"D:\git\flood_exercise\RESULTS\trfRecords")
```

## 06 Train ML
This class is designed to collect pixels from images and train ML model with XGB algorithm. This is just a brginning of training of ML model, more algrithms should be tested and also more data should be used in order to create ML model. 


``` python
instance = classification_pixels(path_imgs_str=r"D:\git\flood_exercise\S2",
                                 path_labels_str=r"D:\git\flood_exercise\S2_HANDLABELED",
                                 target_col = 'None',
                                 cols_to_drop= ['qc'],
                                 test_size= 0.25,
                                 random_state = 42,

                                 )
```

