# Task 02: NumPy Arrays and Numerical Computation

**Mathematical concept:** An array stores many numbers together; NumPy applies one operation to every element without a loop.

---

## B. Inputs and mathematical operation

**Input values:** 24 hourly temperature readings in degrees Celsius (one weather station, one day).

**Operation performed:** Mean, minimum and maximum of the array, then the vectorized conversion F = 1.8C + 32 applied to every reading at once.

**Program:** `code/Task_02_numpy_arrays.py`

### Output of the original program

```text
Daily mean temperature: 23.12 C
Minimum temperature: 17.50 C
Maximum temperature: 29.40 C
First six Fahrenheit readings: [65.3  64.4  64.04 63.5  64.22 66.2 ]
```

---

## C. Changed parameter

**What was changed:** The reading at hour 12 was changed from 29.4 C to 39.4 C (a simulated sensor spike).

**Program:** `changed_parameter/Task_02_numpy_arrays_changed.py`

```text
Daily mean temperature: 23.54 C
Minimum temperature: 17.50 C
Maximum temperature: 39.40 C
First six Fahrenheit readings: [65.3  64.4  64.04 63.5  64.22 66.2 ]
```

**How the result changed:** The mean rose from 23.12 C to 23.54 C (an increase of 10/24 = 0.42 C), the maximum jumped from 29.40 C to 39.40 C, and the minimum stayed at 17.50 C. One extreme value moves the mean and maximum but not the minimum, which shows why outliers must be checked in sensor data.

---

## D. Meaning of the output

The day was mild: the coolest time was early morning (17.50 C, 63.5 F) and the hottest was around midday (29.40 C). The mean of 23.12 C summarises the whole day in one number. The Fahrenheit array shows the same readings on another scale, for example 18.5 C becomes 65.3 F.

**Graphs saved for this task:**

- No graph for this task (text output only).

---

## E. Modified real-world case: IoT water-tank level monitoring

**New assumptions:** A 5000 L tank has a level sensor reporting every hour for 24 hours. A pump refills the tank in the evening and the morning, so the level rises and falls during the day. Levels are in litres.

**New input data:** 24 hourly levels from 4200 L down to 2300 L and back up to 3500 L, stored in a NumPy array.

**Program:** `modified_case/Task_02_water_tank_modified.py`

### Output

```text
Mean level: 3389.6 L (3.390 m3)
Minimum level: 2300 L at hour 10
Maximum level: 4200 L at hour 0
First six readings as percent full: [84. 82. 80. 78. 77. 76.]
First six readings in m3: [4.2  4.1  4.   3.9  3.85 3.8 ]
Largest hourly drop: -500 L
Largest hourly rise: 400 L
Hours below 50 percent full: 2 of 24
```

### Interpretation

The average level was 3389.6 L (3.390 m3). The tank was emptiest at hour 10 (2300 L) and fullest at hour 0 (4200 L). The biggest hourly drop was 500 L and the biggest rise was 400 L (np.diff gives the change between neighbouring readings). Only 2 of 24 hours were below 50 percent full, so the operator would see that the tank rarely runs low.
