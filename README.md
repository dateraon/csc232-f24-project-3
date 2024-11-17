# Project 3: Ludobots

## Table of Contents

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)

## Project Overview

This project explores the evolution of virtual robots (ludobots) using evolutionary algorithms. The goal is to simulate the development of robot morphologies and behaviors over successive generations to achieve optimized movement patterns. For this project, we focus on evolving a two-legged virtual robot using ***Random Search*** to move left (away and into the screen) as efficiently and quickly as possible, simulating walking behavior.

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/dateraon/csc323-f24-project-3.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd csc323-f24-project-3/project3_ludobots
   ```

3. **OPTIONAL: Create a virtual environment**:
   It is recommended to create a virtual environment to manage dependencies.

   ```bash
   python3 -m venv venv
   ```

   Activate the virtual environment:

   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```

4. **Install dependencies**:
   Use the `requirements.txt` file to install all necessary Python packages.

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the project**:
   Follow the usage instructions in the README to start the simulation or analyze results.

## Usage

To run the simulation and observe the evolution of the robots:

1. **Configure Simulation Parameters**:
   - Modify the `constants.py` file to set parameters such as number of iterations.

2. **Start the Evolutionary Process**:
   ```bash
   python3 search.py
   ```
   This script initializes the population and begins the evolutionary algorithm.


## Project Structure

- `data/`: Contains directories for sensor logs
- `pyrosim/`: Includes modules for interfacing with the Pyrosim simulator.
- `analyze.py`: Script for analyzing and visualizing the results of the evolutionary process.
- `constants.py`: Defines global constants and parameters for the simulation.
- `generate.py`: Handles the generation of initial robot populations.
- `motor.py`: Defines motor functionalities for robot movement.
- `robot.py`: Contains the Robot class definition and related methods.
- `search.py`: Main script to initiate the evolutionary search process.
- `sensor.py`: Defines sensor functionalities for robots.
- `simulate.py`: Manages the simulation environment and execution.
- `solution.py`: Represents potential solutions in the evolutionary algorithm.
- `world.py`: Defines the simulation world and its properties.



