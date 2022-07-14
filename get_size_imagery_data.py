import rasterio
import numpy as np
import os
import pandas as pd
import argparse

def write_image_stats(stats_list):
  df = pd.DataFrame(stats_dict_list)
  df.to_csv(os.path.join(output_folder, 'stats.csv'), index=None)
  
  return

def get_image_folder_stats(input_folder, output_folder):
  files = [os.path.join(input_folder, x) for x in os.listdir(input_folder)]
  for file in files:
    stats_dict = get_image_stats(file)
    stats_dict_list += [stats_dict]
  
  write_image_stats(stats_dict)
  
  return stats_dict_list

def get_image_stats(file):
  src = rasterio.open(file)
  image_array = src.read()
  stats_dict = {}
  stats_dict['file'] = file
  stats_dict['bands'] = image_array.shape[0]
  stats_dict['height'] = image_array.shape[1]
  stats_dict['width'] = image_array.shape[2]

  return stats_dict

if __name__ =='__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-i','--input-folder',type=str)
  parser.add_argument('-o','--output-folder',type=str)
  args = parser.parse_args()
  get_image_folder_stats(**vars(args))
