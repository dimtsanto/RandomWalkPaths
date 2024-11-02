---

# Random Walk Simulation

This project simulates and visualizes random walks. It allows users to generate and plot a single random walk path, multiple paths, and a histogram of final positions for a set of simulations.

## Overview

A random walk is a mathematical process that describes a path consisting of successive random steps. This project uses Python to simulate random walks and visualize the paths and final positions of particles.

### Key Functions
- **`randomWalkPath(steps)`**: Simulates a random walk for a given number of steps.
- **`pathPlot(path)`**: Plots the path of a single random walk.
- **`allRandomWalksPaths(steps, simulations)`**: Generates multiple random walks with a specified number of steps and simulations.
- **`allPathsPlots(allPaths)`**: Plots all simulated random walk paths on a single graph.
- **`histPlot(allPaths)`**: Creates a histogram of the final positions of particles after all steps are completed.

## Project Structure

- **`randomWalkPath`**: Generates a single random walk path where each step is either -1 or +1, chosen at random.
- **`pathPlot`**: Plots a single random walk path.
- **`allRandomWalksPaths`**: Runs multiple simulations, returning paths for each particle.
- **`allPathsPlots`**: Plots all paths generated in `allRandomWalksPaths` to visualize variability.
- **`histPlot`**: Displays a histogram of the final positions from all simulations to illustrate the distribution of the endpoints.

## Requirements

- **Python 3.x**
- **NumPy** for numerical operations
- **Matplotlib** for plotting

To install the required libraries, run:
```bash
pip install numpy matplotlib
```

## Usage

1. Run the script:
    ```bash
    python random_walk_simulation.py
    ```

2. Enter the number of steps and simulations when prompted.

3. The program will:
   - Plot a single random walk path.
   - Plot multiple paths for all simulations.
   - Display a histogram showing the final positions of particles in all simulations.

## Example Output

1. **Single Random Walk Path**: Shows the position of a particle over time.
2. **Multiple Paths Plot**: Displays multiple random walk paths for comparison.
3. **Histogram of Final Positions**: Illustrates the distribution of particle positions after all steps are completed.

## License

Feel free to use and modify this code for educational purposes.

--- 
