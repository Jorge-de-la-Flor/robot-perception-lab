English | [Español](README.es.md)

# Robot Perception Lab

Minimal experiments illustrating probabilistic perception and environment representation in robotics systems.

This repository explores simple probabilistic techniques used in robot perception, including sensor models, occupancy grid mapping, and probabilistic localization.

The examples demonstrate how robots can estimate properties of the environment using uncertain sensor data.

## Contents

The `src/` directory contains three minimal experiments:

* `occupancy_grid_mapping.py`

  Demonstrates a simple occupancy grid used to represent the probability of obstacles in a 2D environment.

* `bayes_sensor_model.py`

  Implements a basic Bayesian sensor update model for estimating the probability of obstacle presence.

* `particle_filter_localization.py`

  Simulates a particle filter used for probabilistic robot localization.

## Purpose

These experiments illustrate engineering concepts relevant to:

* robotic perception
* probabilistic robotics
* environment mapping
* localization under uncertainty

## Motivation

Robots operating in real environments must perceive and interpret incomplete and noisy sensor data.

Probabilistic perception techniques allow robots to estimate the structure of their environment and their position within it despite sensor uncertainty.

These methods are widely used in autonomous robots, mobile robotics, and autonomous vehicles.

## Method

The repository implements simplified probabilistic perception algorithms.

The experiments include:

* Bayesian sensor models for environment estimation
* occupancy grid mapping for representing obstacles
* particle filtering for probabilistic localization

These implementations are intentionally minimal and focus on illustrating the conceptual behaviour of perception algorithms rather than full SLAM systems.

## Running the examples

Clone the repository and run any of the scripts:

```bash
git clone https://github.com/Jorge-de-la-Flor/robot-perception-lab
cd robot-perception-lab
python src/occupancy_grid_mapping.py
```

Each script simulates perception behaviour and visualizes the resulting probability distributions.

## Example output

![occupancy grid example](assets/occupancy_grid.png)
![bayesian sensor model example](assets/bayes_sensor_model.png)
![particle filter localization example](assets/particle_filter_localization.png)

## Project tree

```bash
robot-perception-lab
├─ .python-version
├─ LICENSE
├─ README.es.md
├─ README.md
├─ assets
│  ├─ occupancy_grid.png
│  ├─ bayes_sensor_model.png
│  └─ particle_filter_localization.png
├─ pyproject.toml
├─ src
│  ├─ bayes_sensor_model.py
│  ├─ occupancy_grid_mapping.py
│  └─ particle_filter_localization.py
└─ uv.lock
```

## Requirements

The examples use:

* Python 3.12+
* NumPy
* Matplotlib

## Installation

Install the required dependencies:

* using `pip`

```bash
pip install numpy matplotlib
```

* using `uv`

```bash
uv add numpy matplotlib
```

## References

* Thrun, S., Burgard, W., & Fox, D. (2005).
  *Probabilistic Robotics.*

* Elfes, A. (1989).
  *Occupancy Grids: A Stochastic Spatial Representation for Active Robot Perception.*
