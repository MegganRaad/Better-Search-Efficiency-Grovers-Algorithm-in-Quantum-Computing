from qiskit import QuantumCircuit, Aer, execute
from qiskit.quantum_info import Operator
from qiskit.visualization import plot_histogram
import numpy as np
import matplotlib.pyplot as plt

# Defining the number of qubits and the target state
n = 3  # Number of qubits
N = 2**n  # Number of elements in the database
target = 3  # Index of the marked item within the database

# Create the quantum circuit
circuit = QuantumCircuit(n, n)  # Including classical bits for measurement

# Apply H-gates to all qubits to create a superposition
circuit.h(range(n))

# Oracle: marking the state |target>
oracle_matrix = np.identity(2**n)
oracle_matrix[target, target] = -1
oracle_gate = Operator(oracle_matrix)
circuit.unitary(oracle_gate, range(n), label="Oracle")

# Diffusion operator
diffusion_matrix = 2*np.full((2**n, 2**n), 1/(2**n)) - np.eye(2**n)
diffusion_gate = Operator(diffusion_matrix)
circuit.unitary(diffusion_gate, range(n), label="Diffusion")

# Number of iterations is approx: sqrt(N)
num_iterations = int(np.ceil(np.sqrt(N)))
for _ in range(num_iterations):
    # Apply Oracle
    circuit.unitary(oracle_gate, range(n), label="Oracle")
    # Apply Diffusion Operator
    circuit.unitary(diffusion_gate, range(n), label="Diffusion")

# Adding measurement operation to all qubits
circuit.measure(range(n), range(n))

# Simulate the circuit and measure results
backend = Aer.get_backend('qasm_simulator')
job = execute(circuit, backend, shots=1024)
result = job.result()

# Visualize the final results
counts = result.get_counts(circuit)
plot_histogram(counts)
plt.show()

