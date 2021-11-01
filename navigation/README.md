Still working on...................................
# MmWave Wireless-assisted Indoor Navigation Integration with Active Neural SLAM

### Acknowledgements
This work is based on:
* [Habitat API](https://github.com/facebookresearch/habitat-api)
* [Habitat sim](https://github.com/facebookresearch/habitat-sim)
* [Active Neural SLAM](https://github.com/devendrachaplot/Neural-SLAM)

### Overview:
The method is demonstrated on a
[large dataset of indoor environments](http://gibsonenv.stanford.edu/database/) 
supplemented with ray
tracing to simulate the wireless propagation. The path estimation
and link state classification are also integrated into a [state-ofthe-
art neural simultaneous localization and mapping (SLAM)
module](https://arxiv.org/abs/2004.05155)
to augment camera and LIDAR-based navigation. It is
shown that the link state classifier can successfully generalize to
completely new environments outside the training set. In addition,
the neural-SLAM module with the wireless path estimation and
link state classifier provides rapid navigation to the target, close
to a baseline that knows the target location.

## Installing Dependencies (from [Active Neural SLAM](https://github.com/devendrachaplot/Neural-SLAM))
We develop the mmWave wireless-assisted indoor navigation from the "Active Neural SLAM".

### <em>Following [Active Neural SLAM](https://github.com/devendrachaplot/Neural-SLAM) guidance:</em>
  
We use earlier versions of [habitat-sim](https://github.com/facebookresearch/habitat-sim) and [habitat-api](https://github.com/facebookresearch/habitat-api). The specific commits are mentioned below.

Installing habitat-sim:
```
git clone https://github.com/facebookresearch/habitat-sim.git
cd habitat-sim; git checkout 9575dcd45fe6f55d2a44043833af08972a7895a9; 
pip install -r requirements.txt; 
python setup.py install --headless
python setup.py install # (for Mac OS)
```

Installing habitat-api:
```
git clone https://github.com/facebookresearch/habitat-api.git
cd habitat-api; git checkout b5f2b00a25627ecb52b43b13ea96b05998d9a121; 
pip install -e .
```

Install pytorch from https://pytorch.org/ according to your system configuration. The code is tested on pytorch v1.2.0. If you are using conda:
```
conda install pytorch==1.2.0 torchvision cudatoolkit=10.0 -c pytorch #(Linux with GPU)
conda install pytorch==1.2.0 torchvision==0.4.0 -c pytorch #(Mac OS)
```

### <em> Setup [Active Neural SLAM](https://github.com/devendrachaplot/Neural-SLAM):</em>
Clone the repository and install other requirements:
```
git clone --recurse-submodules https://github.com/devendrachaplot/Neural-SLAM
cd Neural-SLAM;
pip install -r requirements.txt
```

The code requires datasets in a `data` folder in the following format (same as habitat-api):
```
Neural-SLAM/
  data/
    scene_datasets/
      gibson/
        Adrian.glb
        Adrian.navmesh
        ...
    datasets/
      pointnav/
        gibson/
          v1/
            train/
            val/
            ...
```
Please download the data using the instructions here: https://github.com/facebookresearch/habitat-api#data

To verify that dependencies are correctly installed and data is setup correctly, run:
```
python main.py -n1 --auto_gpu_config 0 --split val
```

## Import Wireless Data
### Place data in "Neural-SLAM" root folder 
```
Neural-SLAM/
  data/
    wireless_data/
      txt/
        Adrian/
          Adrian_Tx_1_aoa.txt
          Adrian_Tx_1_linkstate.txt
          ...
        Bowlus/
          ...
        ...
```
### Get Tx location from "Ray tracing" data set
[Link](https://github.com/nyu-wireless/mmwRobotNav/tree/main/indoor_ray_tracing/data/tx_position)
```
% correct y
y = -y
```

## Usage
### Place 

