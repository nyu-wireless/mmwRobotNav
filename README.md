# Millimeter Wave Wireless-Assisted Robotic Navigation with Link State Classification

* Mingsheng Yin, Akshaj Veldanda, Kai Pfeiffer, Yaqi Hu, Siddharth Garg, Elza Erkip, Ludovic Righetti, Sundeep Rangan (NYU)
* Amee Trivedi (University of British Columbia)
* Jeff Zhang (Harvard University)

<p align="center">
  <img src="https://github.com/nyu-wireless/mmwRobotNav/blob/main/figs/room_target_agent_new.png" width="300" height="300">
  
  <em>Fig. 1: Target localization and navigation: A target has a wireless
transponder and a robotic agent must locate and navigate to the target
using received wireless signals. The path and map shown in the
figure are example outputs of the [Active Neural-SLAM module](https://arxiv.org/abs/2004.05155)
augmented with the proposed mmWave wireless path estimation and
link state classification algorithm.</em>
</p>

The millimeter wave (mmWave) bands have attracted
considerable attention for high precision localization applications
due to the ability to capture high angular and temporal
resolution measurements. This work explores mmWave-based
positioning for a target localization problem where a fixed target
broadcasts mmWave signals and a mobile robotic agent attempts
to listen to the signals to locate and navigate to the target.
A three strage procedure is proposed: 
* First, the mobile agent
uses tensor decomposition methods to detect the wireless paths
and their angles. 
* Second, a machine-learning trained classifier
is then used to predict the link state, meaning if the strongest
path is line-of-sight (LOS) or non-LOS (NLOS). For the NLOS
case, the link state predictor also determines if the strongest
path arrived via one or more reflections, as shown in Fig. 2. 
* Third, based on the
link state, the agent either follows the estimated angles or
explores the environment.

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

The work is partly based on

* Millimeter Wave Wireless-Assisted Robotic Navigation with Link State Classification. arXiv preprint arXiv:2110.14789.

## Link State Classification
As shown in
Fig. 2, we will classify the link as being in one of four states
on the basis of the strongest received path:
* <em>LOS</em>: The strongest received path is above the minimum threshold and is LOS;
* <em>First-order NLOS</em>: The strongest received path is above
the minimum threshold and is NLOS with one interaction;
* <em>Higher-order NLOS</em>: All sufficiently strong paths from
the TX to RX are NLOS with two or more interactions.
* <em>Outage</em>: There are no sufficiently strong paths above the
minimum threshold.
<p align="center">
  <img src="https://github.com/nyu-wireless/mmwRobotNav/blob/main/figs/Link-states.png" width="300" height="270">
  
  <em>Fig. 2: A demonstration of the LOS, Higher-order NLOS, and Higherorder NLOS.</em>
</p>


## Indoor MmWave Robotic Data Sets
We provide the first complete 5G wireless localization
dataset combined with camera data and robotic
simulation environment.
This millimeter wave indoor wireless data can be combined with the [Habitat-Sim](https://github.com/facebookresearch/habitat-sim) robot simulator.
Regarding wireless, there are two data sets:
* Indoor 28GHz ray tracing
* MmWave MIMO channel modeling

Supporting data sets:
* [Gibson indoor 3D models](http://gibsonenv.stanford.edu/database/) 
* Top-Down indoor maps

<!-- ## Wireless-Assisted Robotic Simulation
The 'Active Neural SLAM' are using  -->

## Acknowledgments
The authors were supported by NSF grants 1952180, 1925079, 1564142,
1547332, the SRC, OPPO, and the industrial affiliates of NYU WIRELESS.
The work was also supported by RemCom that provided the [Wireless Insite](https://www.remcom.com/wireless-insite-em-propagation-software)
software.
