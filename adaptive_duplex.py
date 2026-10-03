import tkinter as tk
from tkinter import ttk
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# ---------------------------------------------------------
# ADAPTIVE DUPLEX MODE SELECTION SIMULATION
# ---------------------------------------------------------

class DuplexSimulation:

    def __init__(self, root):
        self.root = root
        self.root.title("Adaptive Duplex Mode Selection")
        self.root.geometry("1000x700")

        self.running = False
        self.time = 0

        self.time_data = []
        self.traffic_a_to_b = []
        self.traffic_b_to_a = []
        self.throughput_data = []
        self.delay_data = []
        self.mode_data = []

        # -------------------------
        # Title
        # -------------------------
        title = tk.Label(
            root,
            text="Adaptive Duplex Mode Selection Based on Bidirectional Traffic Demand",
            font=("Arial", 16, "bold")
        )
        title.pack(pady=10)

        # -------------------------
        # Network display
        # -------------------------
        network_frame = tk.Frame(root)
        network_frame.pack(pady=10)

        self.node_a = tk.Label(
            network_frame,
            text="NODE A",
            font=("Arial", 14, "bold"),
            relief="raised",
            width=12,
            height=2
        )
        self.node_a.grid(row=0, column=0, padx=40)

        self.link_label = tk.Label(
            network_frame,
            text="↔\nCHANNEL",
            font=("Arial", 12, "bold")
        )
        self.link_label.grid(row=0, column=1)

        self.node_b = tk.Label(
            network_frame,
            text="NODE B",
            font=("Arial", 14, "bold"),
            relief="raised",
            width=12,
            height=2
        )
        self.node_b.grid(row=0, column=2, padx=40)

        # -------------------------
        # Current status
        # -------------------------
        status_frame = tk.Frame(root)
        status_frame.pack(pady=10)

        tk.Label(
            status_frame,
            text="Current Mode:",
            font=("Arial", 12, "bold")
        ).grid(row=0, column=0, padx=5)

        self.mode_label = tk.Label(
            status_frame,
            text="WAITING",
            font=("Arial", 14, "bold"),
            width=15
        )
        self.mode_label.grid(row=0, column=1, padx=10)

        # -------------------------
        # Traffic information
        # -------------------------
        traffic_frame = tk.Frame(root)
        traffic_frame.pack(pady=5)

        self.a_to_b_label = tk.Label(
            traffic_frame,
            text="A → B Traffic: 0",
            font=("Arial", 11)
        )
        self.a_to_b_label.grid(row=0, column=0, padx=30)

        self.b_to_a_label = tk.Label(
            traffic_frame,
            text="B → A Traffic: 0",
            font=("Arial", 11)
        )
        self.b_to_a_label.grid(row=0, column=1, padx=30)

        self.throughput_label = tk.Label(
            traffic_frame,
            text="Throughput: 0",
            font=("Arial", 11)
        )
        self.throughput_label.grid(row=1, column=0, padx=30)

        self.delay_label = tk.Label(
            traffic_frame,
            text="Average Delay: 0 ms",
            font=("Arial", 11)
        )
        self.delay_label.grid(row=1, column=1, padx=30)

        # -------------------------
        # Buttons
        # -------------------------
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        self.start_button = ttk.Button(
            button_frame,
            text="Start Simulation",
            command=self.start_simulation
        )
        self.start_button.grid(row=0, column=0, padx=10)

        self.stop_button = ttk.Button(
            button_frame,
            text="Stop",
            command=self.stop_simulation
        )
        self.stop_button.grid(row=0, column=1, padx=10)

        self.reset_button = ttk.Button(
            button_frame,
            text="Reset",
            command=self.reset_simulation
        )
        self.reset_button.grid(row=0, column=2, padx=10)

        # -------------------------
        # Graph
        # -------------------------
        self.figure, self.ax = plt.subplots(figsize=(8, 4))

        self.canvas = FigureCanvasTkAgg(
            self.figure,
            master=root
        )

        self.canvas.get_tk_widget().pack(
            fill=tk.BOTH,
            expand=True,
            padx=20,
            pady=10
        )

        self.update_graph()

    # -----------------------------------------------------
    # Adaptive decision algorithm
    # -----------------------------------------------------

    def select_mode(self, a_to_b, b_to_a):

        total = a_to_b + b_to_a

        if total < 20:
            return "SIMPLEX"

        difference = abs(a_to_b - b_to_a)

        if a_to_b > 70 and b_to_a > 70:
            return "FULL DUPLEX"

        if difference > 50:
            return "HALF DUPLEX"

        return "HALF DUPLEX"

    # -----------------------------------------------------
    # Calculate performance
    # -----------------------------------------------------

    def calculate_performance(self, mode, a_to_b, b_to_a):

        total = a_to_b + b_to_a

        if mode == "SIMPLEX":
            throughput = max(a_to_b, b_to_a) * 0.80
            delay = 45

        elif mode == "HALF DUPLEX":
            throughput = total * 0.72
            delay = 30

        else:
            throughput = total * 0.92
            delay = 15

        return throughput, delay

    # -----------------------------------------------------
    # Start simulation
    # -----------------------------------------------------

    def start_simulation(self):

        if not self.running:
            self.running = True
            self.simulate()

    # -----------------------------------------------------
    # Simulation loop
    # -----------------------------------------------------

    def simulate(self):

        if not self.running:
            return

        self.time += 1

        # Generate changing traffic demand
        phase = self.time % 30

        if phase < 8:
            # Mostly A -> B
            a_to_b = random.randint(60, 100)
            b_to_a = random.randint(0, 15)

        elif phase < 16:
            # Mostly B -> A
            a_to_b = random.randint(0, 15)
            b_to_a = random.randint(60, 100)

        elif phase < 24:
            # Strong bidirectional traffic
            a_to_b = random.randint(70, 100)
            b_to_a = random.randint(70, 100)

        else:
            # Low traffic
            a_to_b = random.randint(0, 15)
            b_to_a = random.randint(0, 15)

        mode = self.select_mode(a_to_b, b_to_a)

        throughput, delay = self.calculate_performance(
            mode,
            a_to_b,
            b_to_a
        )

        # Store data
        self.time_data.append(self.time)
        self.traffic_a_to_b.append(a_to_b)
        self.traffic_b_to_a.append(b_to_a)
        self.throughput_data.append(throughput)
        self.delay_data.append(delay)
        self.mode_data.append(mode)

        # Keep graph readable
        if len(self.time_data) > 50:
            self.time_data.pop(0)
            self.traffic_a_to_b.pop(0)
            self.traffic_b_to_a.pop(0)
            self.throughput_data.pop(0)
            self.delay_data.pop(0)
            self.mode_data.pop(0)

        # Update screen
        self.a_to_b_label.config(
            text=f"A → B Traffic: {a_to_b}"
        )

        self.b_to_a_label.config(
            text=f"B → A Traffic: {b_to_a}"
        )

        self.throughput_label.config(
            text=f"Throughput: {throughput:.2f}"
        )

        self.delay_label.config(
            text=f"Average Delay: {delay} ms"
        )

        self.mode_label.config(
            text=mode
        )

        self.update_graph()

        self.root.after(800, self.simulate)

    # -----------------------------------------------------
    # Update graph
    # -----------------------------------------------------

    def update_graph(self):

        self.ax.clear()

        if self.time_data:

            self.ax.plot(
                self.time_data,
                self.traffic_a_to_b,
                label="A → B Traffic"
            )

            self.ax.plot(
                self.time_data,
                self.traffic_b_to_a,
                label="B → A Traffic"
            )

        self.ax.set_title(
            "Bidirectional Traffic Demand"
        )

        self.ax.set_xlabel("Simulation Time")
        self.ax.set_ylabel("Traffic Demand")

        self.ax.legend()
        self.ax.grid(True)

        self.figure.tight_layout()
        self.canvas.draw()

    # -----------------------------------------------------
    # Stop
    # -----------------------------------------------------

    def stop_simulation(self):

        self.running = False

    # -----------------------------------------------------
    # Reset
    # -----------------------------------------------------

    def reset_simulation(self):

        self.running = False
        self.time = 0

        self.time_data.clear()
        self.traffic_a_to_b.clear()
        self.traffic_b_to_a.clear()
        self.throughput_data.clear()
        self.delay_data.clear()
        self.mode_data.clear()

        self.mode_label.config(
            text="WAITING"
        )

        self.a_to_b_label.config(
            text="A → B Traffic: 0"
        )

        self.b_to_a_label.config(
            text="B → A Traffic: 0"
        )

        self.throughput_label.config(
            text="Throughput: 0"
        )

        self.delay_label.config(
            text="Average Delay: 0 ms"
        )

        self.update_graph()


# ---------------------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------------------

root = tk.Tk()

app = DuplexSimulation(root)

root.mainloop()