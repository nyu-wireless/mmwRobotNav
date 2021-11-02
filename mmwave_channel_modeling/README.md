# Indoor Millimeter Wave MIMO Channel Modeling
We assumed a 28 GHz array similar to several recent
published 5G designs and layouts. The parameters
for the arrays and signaling are shown in Table. I.
The target
TX is assumed to be a UE device and the RX is a gNB. The
arrays use microstrip patch antennas and the beam patterns of
each array when directed at boresight are shown in Fig. 1.
<p align="center">
  <img src="https://github.com/nyu-wireless/mmwRobotNav/blob/main/figs/table_1.jpg" width="400">
</p>
<p align="center">
  <img src="https://github.com/nyu-wireless/mmwRobotNav/blob/main/figs/ant_array_pattern.png" width="400">
  
  <em>Fig. 1: The pattern of one gNB antenna array and one UE antenna
array. (The array is aligned so that its bore-sight is on the x-axis.)</em>
</p>

We create the multiple antenna arrays at both
the gNB and UE. Specifically, we assume three arrays with
azimuth angles 0°, 120°, and -120° and 0° elevation. The
multi-sector layout provides 360° coverage. For example,
Fig. 2 plots the maximum gain for each individual array and
the maximum gain over all three arrays over [180°, 180°]
the azimuth directions. We see that the minimum gain is only
approximately 3 dB below the maximum.

<p align="center">
  <img src="https://github.com/nyu-wireless/mmwRobotNav/blob/main/figs/array_coverage-gain.jpg" width="300">
  
  <em>Fig. 2: Array gain including the element gain from each gNB array
as well as the best for all three arrays. We see that by using multiple
arrays we can obtain full azimuth coverage.</em>
</p>

## Useful Link
* [NYU Wireless Comm by Prof.Rangan](https://github.com/sdrangan/wirelesscomm) 
