# Millimeter Wave Wireless-Assisted Robotic Navigation with Link State Classification

* Mingsheng Yin, Akshaj Veldanda, Kai Pfeiffer, Yaqi Hu, Siddharth Garg, Elza Erkip, Ludovic Righetti, Sundeep Rangan (NYU)
* Amee Trivedi (University of British Columbia)
* Jeff Zhang (Harvard University)

The work is based on

* Millimeter Wave Wireless-Assisted Robotic Navigation with Link State Classification. arXiv preprint [arXiv:2110.14789](https://arxiv.org/abs/2110.14789).
* The figures and explanations in this repository can be found in the paper.

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

## Path Estimation
Detailed antenna and multiple array modeling: Practical
mmWave devices at the terminal (UE) and base station
(gNB) often use multiple arrays oriented in different
directions to obtain 360 degree coverage.
This work models these multiple array structures and
also includes detailed models of the antenna element
directivity in each array. In addition, we do not consider
any local oscillator (LO) synchronization across different
arrays.

<p align="center">
  <img src="https://github.com/nyu-wireless/mmwRobotNav/blob/main/figs/ant_array_pattern.png" width="400">
  
  <em>Fig. 2: The pattern of one gNB antenna array and one UE antenna
array. (The array is aligned so that its bore-sight is on the x-axis.)</em>
</p>

<p align="center">
  <img src="https://github.com/nyu-wireless/mmwRobotNav/blob/main/figs/array_coverage-gain.jpg" width="300">
  
  <em>Fig. 3: Array gain including the element gain from each gNB array
as well as the best for all three arrays. We see that by using multiple
arrays we can obtain full azimuth coverage.</em>
</p>

Beam sweeping double directional estimation: Many
prior mmWave localization studies have either abstracted
the directional estimation, considered single-sided
directional estimates, or considered double
directional estimates using MIMO signaling. In
this work, we modify the low-rank tensor decomposition
algorithms in [paper](https://ieeexplore.ieee.org/document/8647176) and 
[paper](https://ieeexplore.ieee.org/document/7914672)
to account for both sweeping of
the TX beams and use of multiple arrays at the TX and
RX. Beam sweeping at the transmitter is critical to model
for most cellular mmWave systems.
<p align="center">
  <img src="https://github.com/nyu-wireless/mmwRobotNav/blob/main/figs/beam_sweep.jpg" width="400">
  
  <em>Fig. 4: Example TX beam sweeping with Ntx_arr = 3 arrays and
4 directions per array for a total of Ntx_dir = 12 beam directions.
The synchronization signals are sent once in each direction with the
pattern repeating every Tsweep seconds.</em>
</p>

<p align="center">
  <img src="https://github.com/nyu-wireless/mmwRobotNav/blob/main/figs/h_peak.png" width="400">
  
  <em>Fig. 5: Example received power spectrum along TX-RX direction
pair along with the location of the actual ray tracing paths of a LOS
link and a NLOS link. The black squares indicate the result of path
estimation by the low-rank tensor decomposition.</em>
</p>

## Link State Classification
As shown in
Fig. 6, we will classify the link as being in one of four states
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
  
  <em>Fig. 6: A demonstration of the LOS, Higher-order NLOS, and Higherorder NLOS.</em>
</p>

Multi-class link classification: Instead of simply classifying
the link as LOS or NLOS, we differentiate between
four states: LOS, NLOS from a single interaction, higherorder
NLOS and outage. We show that for target localization
application, both LOS and first-order NLOS paths
have angles of arrival that strongly correlate with good
navigation directions.
<p align="center">
  <img src="https://github.com/nyu-wireless/mmwRobotNav/blob/main/figs/link-states_predict_map.png", width="500">
  
  <em>Fig. 7: Two Link-States maps. (a) is truth from ray traying tool and
(b) is result of the link-states classification neural network prediction.</em>
</p>

The reason we are interested in this
problem is that the angle of arrival of LOS and first-order
NLOS path have strong correlation with the optimal direction
for navigation. Hence, if can reliably detect the link state and
estimate the angle of arrival of the strongest path, we can
build a navigation system that simply follows the estimated
strongest path angle of arrival.
<p align="center">
  <img src="https://github.com/nyu-wireless/mmwRobotNav/blob/main/figs/aoa_est_err.png">
  
  <em>Fig. 8: Distribution of the absolute error between the estimated
strongest path’s AoA from channel sounding and the AoA of the
strongest path in real ray tracing data set.</em>
</p>

## Wireless-Assisted Robotic Navigation Integration with Neural SLAM
Of course, the link state and the path estimate are not
known a priori by the mobile agent. We thus propose to
use the link state classification along with the estimated SNR
of the strongest path to make a decision on whether to use
the wireless-based navigation goal or not. If the wirelessbased
navigation goal is selected, it can simply overwrite
the navigation goal in the Neural-SLAM module. If, on the
other hand, the wireless-based navigation goal is considered
unreliable, the mobile agent can use the exploration-based
goal from the original global policy. This selection concept
is illustrated in Fig. 9.
<p align="center">
  <img src="https://github.com/nyu-wireless/mmwRobotNav/blob/main/figs/nslam_new.png", width="600">
  
  <em>Fig. 9: MmWave-Based wireless path detection and link state classification are used to augment the Active Neural SLAM module [9] by
overwriting the navigation goal from the wireless path estimation.</em>
</p>

We consider three possible selection algorithms for determining
whether or not to use the estimated AoA from the
wireless detection:
* AoA based on SNR only: The robot follows the AoA of
the highest SNR path if the path SNR is above some
threshold in any link state. Otherwise, the robot follows
the goal from Active Neural SLAM map exploration.
* AoA when LOS: The robot follows the estimated AoA
when the strongest path is in a LOS state and the SNR
is above the threshold.
* AoA when LOS or First-order NLOS: The robot follows
the estimated AoA when the strongest path is in a LOS
state or first-order NLOS and the SNR is above the
threshold.

An example result can be found [here](https://github.com/nyu-wireless/mmwRobotNav/tree/main/navigation/example)
<p align="center">
  <img src="https://github.com/nyu-wireless/mmwRobotNav/blob/main/figs/arrival_rate.png", width="400">
  
  <em>Fig. 10: Arrival success rate of three algorithms in easy, moderate,
and hard environments.</em>
</p>
<p align="center">
  <img src="https://github.com/nyu-wireless/mmwRobotNav/blob/main/figs/arrival_speed.png", width="400">
  
  <em>Fig. 11: Three cumulative distribution function (CDF) plots show
the arrival speed in easy, moderate, and hard difficult level. At all
three difficulty levels, AoA when LOS or First-order NLOS algorithm
performs most effectively. The results demonstrate the effectiveness
of the link-state classification neural network in improving the robot
navigation problem.</em>
</p>
</p>
<p align="center">
  <img src="https://github.com/nyu-wireless/mmwRobotNav/blob/main/figs/example_lsaoa_better.png", width="400">
  
  <em>Fig. 12: An example of two different robot walling paths are
generated in a test case. In (a), the robot uses the AoA when LOS or
First-order NLOS and spends 150 steps to arrive the TX. In (b), the
robot uses the AoA based on SNR and spends 358 steps to reach the
TX. The area framed by the black dashed line shows the difference
between the two algorithms.</em>
</p>


## Indoor MmWave Robotic Data Sets
We provide the first complete 5G wireless localization
dataset combined with camera data and robotic
simulation environment.
This millimeter wave indoor wireless data can be combined with the [Habitat-Sim](https://github.com/facebookresearch/habitat-sim) robot simulator.
Regarding wireless, there are two data sets:
* [Indoor 28GHz ray tracing](https://github.com/nyu-wireless/mmwRobotNav/tree/main/indoor_ray_tracing)
* [MmWave MIMO channel modeling](https://github.com/nyu-wireless/mmwRobotNav/tree/main/mmwave_channel_modeling)

Habitat-Sim and Active Neural SLAM adaptive data set:
* [Robot simulation](https://github.com/nyu-wireless/mmwRobotNav/tree/main/navigation)

Supporting data sets:
* [Gibson indoor 3D models](http://gibsonenv.stanford.edu/database/) 
* [Top-Down indoor maps](https://github.com/nyu-wireless/mmwRobotNav/tree/main/indoor_env)


## Acknowledgments
The authors were supported by NSF grants 1952180, 1925079, 1564142,
1547332, the SRC, OPPO, and the industrial affiliates of NYU WIRELESS.
The work was also supported by RemCom that provided the [Wireless Insite](https://www.remcom.com/wireless-insite-em-propagation-software)
software.
