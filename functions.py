def get_food_data(percent=100):
  """Download and unzip data.

  Args:
    percent: one of 1, 10, 100. Defines how much training data will be downloaded. 
  
  Returns:
    path to data, classes
  """
  if percent == 1:
    data_name = '10_food_classes_1_percent'
  elif percent == 10:
    data_name = '10_food_classes_10_percent'
  elif percent == 100:
    data_name = '10_food_classes_all_data'
  else:
    print('precent can be only one of 1, 10, 100')
    raise ValueError

  import zipfile
  import os

  if not os.path.isfile(data_name + '.zip'): # get data if not exist
    data_url = 'https://storage.googleapis.com/ztm_tf_course/food_vision/' + data_name + '.zip'
    !wget $data_url

  try: 
    zip_ref = zipfile.ZipFile(data_name + '.zip')
    zip_ref.extractall()
    zip_ref.close()
  except:
    print(f'File {data_name + ".zip"} not found')
    raise FileNotFoundError

  class_names = []
  for root, dirs, files in os.walk(data_name):
    if root == data_name:
      print(f'There are {len(dirs)} datasets: {dirs}')
    else:
      if files == []:
        print(f'  In {root} there are {len(dirs)} classes:\n  {dirs}')
        class_names = dirs
      else:
        print(f'    in {root} there are {len(files)} images')

  return data_name, class_names


def create_tb_callback(dir_name:str = 'tf_logs', exp_name:str = 'Default'):
  """Create a tensorboard callback to use in model.fit
  
  Args:
    dir_name (str): directory name for saving log files. 
    exp_name (str): experiment name.
   
  Returns:
    callback
  """
  import datetime
  import tensorflow as tf
  
  log_dir = dir_name + '/' + exp_name + '/' + datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
  tb_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, 
                                               )
  print(f'Saving TF logs to {log_dir}')
  return tb_callback
