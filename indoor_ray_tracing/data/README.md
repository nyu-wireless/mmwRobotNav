#### Ray Tracing Data Set

There are at most 25 paths per each TX-RX links.

#### To get correct tx position:
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
