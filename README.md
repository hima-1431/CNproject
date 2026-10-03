# Adaptive Duplex Mode Selection Based on Bidirectional Traffic Demand

## Project Description

This project is a Python-based simulation that adaptively selects the duplex communication mode based on traffic demand between Node A and Node B.

The system monitors:
- A → B traffic
- B → A traffic

Based on the traffic conditions, it selects:
- SIMPLEX
- HALF DUPLEX
- FULL DUPLEX

The GUI displays the current traffic, selected mode, throughput, average delay, and traffic graph.

## Requirements

- Python 3.x
- Tkinter
- Matplotlib

## How to Run

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Open the VS Code Terminal.
4. Install Matplotlib using:

`pip install matplotlib`

5. Run the program using:

`python adaptive_duplex.py`

6. The GUI window will open.
7. Click **Start Simulation** to begin the simulation.

## Output

The GUI displays:

- Node A and Node B
- Current Duplex Mode
- A → B Traffic
- B → A Traffic
- Throughput
- Average Delay
- Bidirectional Traffic Demand graph

### Graph

**X-axis:** Simulation Time  
**Y-axis:** Traffic Demand

The graph shows the changes in A → B and B → A traffic during the simulation.

## Duplex Mode Selection

- Low traffic → SIMPLEX
- Mainly one-directional traffic → HALF DUPLEX
- High traffic in both directions → FULL DUPLEX

## Controls

- **Start Simulation** – Starts the simulation
- **Stop** – Stops the simulation
- **Reset** – Clears the simulation data and resets the values