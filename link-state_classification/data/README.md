# Dataset : Channel Modeling Result, at most 5 paths for each link.

Please use this data to run the link-state classification.

## Run download.py

### The whole dataset is splited into 3 parts. For each part, take about 2 mins to download.

python download.py [X]

Replace [X] with one of: Part1, Part2, Part3, All

For example, 
    python download.py Part1

We divided the dataset into 5 parts because the entire dataset is large, and dividing it helps avoid downloading issues. Each part contains distinct data, so you can download any part of the data for use. Each part includes multiple maps, and each map contains data from 10 transmitters (TX).


## To get correct tx position:
```
% first -y
y = -y

% for 480 * 480 map
x = x / 0.05
y = y / 0.05

% around to int if needed
x = int(x)
y = int(y)
```
