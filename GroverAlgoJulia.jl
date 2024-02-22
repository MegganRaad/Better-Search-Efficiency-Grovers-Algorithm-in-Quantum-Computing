using Qiskit
import Pkg; Pkg.add("Plots")
using Plots

# Defining the number of qubits and the target state n = 3 # of qubits
N = 2^n # of elements in the database
target = 3 # Index of the marked item within database

# Create the quantum circuit
circuit = QuantumCircuit(n)
# Apply H-gates to all qubits to create a superposition
for i in 1:n
  append!(circuit, HGate(), [i])
end

# Grover iteration
oracle = OracleGate(n, target) # Creating the oracle
diffusion = DiffusionOperator(n) # Creating the diffusion operator grover_iteration = CompositeGate([oracle, diffusion])

# Number of iterations is approx: sqrt(N)
num_iterations = Int(ceil(sqrt(N)))
for _ in 1:num_iterations
       append!(circuit, grover_iteration)
end

# Simulate the circuit + measure results
backend = Aer.get_backend("qasm_simulator")
job = execute(circuit, backend, shots=1024)
result = job.result()

# Visualize the final results
counts = result.get_counts(circuit)
plot(bar(counts))