# Dataset : Link-state prediction result and the strongest path angle of arrival result.

Please use this dataset to run the NSLAM code.

## Run python download.py All

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
