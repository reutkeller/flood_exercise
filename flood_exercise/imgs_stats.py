# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/statistics.ipynb.

# %% auto 0
__all__ = ['ImgsStatistics']

# %% ../nbs/statistics.ipynb 3
import rasterio
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from . import utils_func
from . import const_vals as CONST

# %% ../nbs/statistics.ipynb 4
class ImgsStatistics():

  def __init__(self,
      path_to_imgs : str , # path to the folder that contains the images
      ):
      
      # get the tiles paths
      self.list_of_files = utils_func.load_tif_paths(path_to_imgs)

      self.collect_results = {CONST.PATH_STR : [] , CONST.REGION_STR : []}

      for path in self.list_of_files:
         region = self._get_region_name_(path)
         self.collect_results[CONST.PATH_STR] = path
         self.collect_results[CONST.REGION_STR]=region

      self._img_statistics_(path)


  def _get_region_name_(self,
                        tile_name : str , # path of image , assuming that the first word in the file name is the region name
                        ):
     """
     Takes a string of images from the type "region_id_label.tif and extract the region name.
     for example, for "Bolivia_23014_S2Hand.tif" it will return Bolivia
     Parameters:
     folder_path (str): The path to the folder containing TIFF files.

     Returns:
     string: Name of the region , extracted from the tile name 
     """
     
     region = tile_name.split(CONST.SPLIT_TILES_NAMES_STR)[0]
     return region
  

  
  def _img_statistics_(self,
                       path : str , # path to image (tif file)
                       ):
     
     src = rasterio.open(path)
     src_arr = src.read()
     band_names = list(src.descriptions)

     self.bands_stats = {CONST.STR_BAND_NAME : [] , CONST.STR_MEAN : [] , CONST.STR_STD : [] }

     for band_name , index in zip(band_names,range(0,src.read().shape[0])):
        
        arr = src_arr[index,:,:]

        #convert 0 to nan , assuming 0 is no value and we don't want it to interrupt the staitistics
        arr = np.where(src_arr==0, np.nan, arr)

        #calculate mean
        mean = np.nanmean(arr)

        #calculate std
        std = np.nanstd(arr)

        self.bands_stats[CONST.STR_BAND_NAME] = band_name
        self.bands_stats[CONST.STR_MEAN] = mean
        self.bands_stats[CONST.STR_STD] = std






        
        

        

     

    

