# Indoor Millimeter Wave Ray Tracing

To capture the wireless coverage, we use the powerful ray
tracing package, [Wireless InSite](https://www.remcom.com/wireless-insite-em-propagation-software) by Remcom which has
also been used in several other recent mmWave studies such as. 
Ray tracing uses a high-frequency approximation to
simulate the electromagnetic paths between any two locations.

For each imported map, we then place the transmitters in
10 randomly selected locations representing 10 possible target 
positions. The ray tracing is then used to estimate the wireless
paths at RX locations on a 160 x 160 grid with 0.15 x 0.15
m grid representing a total area of 24 m^2. Example ray tracing
simulations areas are shown in Fig. 1.
The ray tracing is performed at 28 GHz, the most
commonly-used frequency for 5G mmWave devices. We
ignore the difference of material and treat all walls as the
ITU (International Telecommunication Union) layered drywall
whose permittivity is 2.94 (F/m) and conductivity is 0.1226
(S/m) in 28 GHz.
<p align="center">
  <img src="https://github.com/nyu-wireless/mmwRobotNav/blob/main/figs/remcom_maps.png" width="400">
  
  <em>Fig. 1: Four examples of ray tracing simulation area. In each map,
ten green dots represent transmitter locations and a red dots grid
represents the receiver grid with total 25,600 receivers. (The ceiling
of room is not shown.)</em>
</p>

Example ray tracing
outputs are shown in Fig. 2. Using the true signal parameters,
we can then simulate the path estimation algorithms to create estimates of the path parameters.
<p align="center">
  <img src="https://github.com/nyu-wireless/mmwRobotNav/blob/main/figs/ray_tracing_example.png" width="400">
  
  <em>Fig. 2: A LOS link (left) and a NLOS link (right) examples of the
ray tracing paths. (Some weaker paths are not shown).</em>
</p>
