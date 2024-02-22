# Better Search Efficiency: Grover’s Algorithm in Quantum Computing
#### Written and edited by : Latin-American Computer Scientist Meggan Raad

## Introduction and Preliminaries
This in-depth article aims to explore the potential factors that make Grover’s algorithm improve search efficiency in Quantum Computing. Discussions will consist of the origins of search algorithms in Quantum, which was proposed by Lov Grover in 1996. Additionally, the theoretical foundations in the algorithm that make up its ability to achieve a quadratic speedup for unstructured search problems in comparison to other classical algorithms. Along with certain approaches and implementations to test the algorithm in Julia and Python3. There will be a closing conclusion and reflection on real-world applications. This includes various industries such as cryptography, database searches, and optimization problems.
> Key Words: speed-up, classical search, Qiskit, Unstructured Database, Julia, Python

------
## Table of Contents
### Chapter 1: Origins of search algorithms in Quantum
- 1.1 Seminal work of Lov Grover
- 1.2 Grover’s Algorithm foundations 
### Chapter 2: Grover’s Algorithm Explained
- 2.0 Bits
### Chapter 3: Applying Grover’s Algorithm in unstructured database
- 3.0 Program briefing
- 3.1 Grover’s Algorithm in Julia Program 3.2 Translating program to Python3
### Chapter 4: Real-world applications
- 4.0 Grover’s application in real-world scenarios
- 4.1 Post-quantum cryptography 
### Chapter 5: Conclusion
- 5.0 Reflection
### Reference

---
## Chapter 1
### Origins of Search algorithms in Quantum
Quantum Computers profess to have a speed-up over classical computers. Initially, it wasn’t clear if such a statement was true. This is until 1994, when American Mathematician Peter Shor developed Shor’s algorithm: a quantum algorithm that finds the prime factors of an integer. This opened the way for further possible algorithms to be developed and explored.
##### 1.1 Seminal work of Lov Grover 

Indian-American Computer Scientist Lov Grover, proposed in 1996 an innovational quantum algorithm that would advance classical search algorithms in an immense way. Lov’s prediction of the 21st Century becoming the age of Quantum, has led him to further progress in his studies of Quantum Search and beyond. His contributions to Quantum Computation and Information Processing have been of vital and significant value to the industry. With his PhD in Electrical Engineering from Stanford University, and work as member of Technical Staff in Bell Labs, his technical proficiencies have been the cause and effect of ground-breaking research in Quantum Computing.


* 1.2 Grover’s Algorithm foundations

Grover’s Algorithm is a Database Search algorithm consisting of a quadratic speed-up. This algorithm was originally intended for an unstructured database, which is useful when having to find items in a vast amount of unordered data. This algorithm will serve very useful when we see a world growth in Internet of Things (IoT) and there is a larger level of data coming in. The algorithm can best be taken advantage of in any brute-force search circumstance due to its quadratic speed up. This means it is important to understand fundamentally how Grover’s algorithm works at its core.

---

## Chapter 2 
### Grover’s Algorithm Explained
* 2.1 Classic vs Grover’s Logic

Given an unordered array of x elements, find a specific element. This classical computational problem of unordered arrays would, in the worst case, take x queries. In an
average computational setting the desired value would me found in $x/2$ queries. But is there a more efficient way?

With Grover’s search algorithm, the job can be done in $\sqrt{𝑥}$ queries. Ultimately creating a better speedup search time. We can look at this in the form of functions for better
understandment. Given a function $𝑓 : (0, 1)^𝑛 → (0, 1)$ and a binary string $(𝑥)_0$ such that:

$$f(x) = \begin{cases}
   1 &\text{if } x  = (x)_0 \\
   0 &\text{if } x \not = (x)_0
\end{cases}$$



Find $(𝑥)_0$. With classical computer science logic we would evaluate all $(2)^𝑛$ Binary strings to
find our $(𝑥)_0$. With Grover’s algorithm, we will only apply the following evaluation: 

$\sqrt(2)^𝑛 = (2)^{𝑛/2}$

Where 𝑓 will be given to us in the Unitary Matrix 𝑈𝑓 which takes $[𝑥, 𝑦 > to [𝑥, 𝑓(𝑥) ⊕ 𝑦 >$.
A classical approach will search an unordered array of size 𝑛 in 𝑛 steps, while Grover’s
algorithm will take time 𝑛. For the specific case of Grover's algorithm, the oracle flips the sign of the amplitude of the state corresponding to the target item, effectively marking it for identification through the subsequent application of the diffusion operator (also known as the Grover operator). This overall is called Quadratic Speedup. This doesn’t mean Grover’s application here is the holy grail of search time speedup, but it is still very good and efficient. Propositioning a faster and more efficient search time than your average computer science search algorithm.

the oracle's unitary matrix $U_f$ depends on the specific target state you're searching for. Let's consider a simple example with a 2-qubit system $(n = 2)$, where the database has $N = 2^n = 4$ items. Suppose we are searching for the item corresponding to the binary string $x_0 = 11$, which is the decimal number 3 in a 0-indexed system.

In this case $U_f$ is designed to flip the sign of the amplitude of the state $|11>$ while leaving the amplitude of all the other states unchanged. This would mean $U_f$ would be:

$$U_f = \begin{bmatrix}
   1 & 0 & 0 & 0  \\
   0 & 1 & 0 & 0  \\
   0 & 0 & 1 & 0 \\
   0 & 0 & 0 & -1
\end{bmatrix}$$

---
## Chapter 3
### Applying Grover's Algorithm in Unstructured Databases
* 3.0 Program Briefing

To further understand the application of Grover’s Algorithm, we will be designing a program to simulate a search in an unstructured database. Remember that Grover’s algorithm has the ability to significantly speed up search process time in comparison to a classical algorithm approach. Ideally, such a program would be better developed with a more quantum supportive feature such as Jupyter Notebook (IDE). But for simplicity and pursuit of fundamental understanding, any IDE of choice will suffice.

* 3.1 Grover's Algorithm in Julia Program

The following program written in Julia is designed to simulate what we have discussed previously about Grover’s algorithm. The program begins by setting up a Quantum Circuit through importing the Qiskit package. This package is a toolkit frequently used in Quantum computing:

```Julia
# Importing the required packages
using Qiskit
import Pkg; Pkg.add("Plots")
using Plots
```

We follow this up by setting our parameters for the algorithm. This being the number of Qubits and our targeted state.Our qubit here will be 𝑛 = 3, this will be the basic unit of quantum information. This number determines the size of the database that the algorithm can search. We then need to setup our calculation for the number of elements in the
database that the algorithm will search through. When 𝑛 qubits represents $(2)^𝑛$ states, then
3 qubits will have the program search for $(2)^3 = 8$ unique elements. This is due to each qubit being in a superposition of two states {0, 1}. So this means:
$3𝑞𝑏 = 2𝑥2𝑥2 → 3𝑞𝑏 = 8 𝑝𝑜𝑠𝑠𝑖𝑏𝑙𝑒𝑐𝑜𝑚𝑏𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑠$

So we initialize our Target to 3, specifying the index of the item the algorithm will be searching for in the database. Since we set our Target to index 3, the algorithm will search for the 4th element within the database. This is since indexing begins at 0

```Julia
# Defining the number of qubits and the target state n = 3 # of qubits
N = 2^n # of elements in the database
target = 3 # Index of the marked item within database
```

The core functionality of the program is when we apply the Grover iteration to the quantum circuit. This consist of two sections: the Oracle and the Diffusion operator. I will further explain the sectors. First let's create our quantum circuit.

We will create a new quantum circuit with 𝑛 number of qubits. To do this, we need to implement QuantumCircuit. This is a fundamental component in quantum. It represents a sequence of quantum gates and measurements that applies to the 𝑛 qubits.

We then apply Hadamard gates or H-gates to each qubit in the circuit. This creates a superposition state from the basis state. Once its applied to the qubit in a |0 > state, our H-gate will transform it into an equal superposition state of |0 > & |1 >. This will be integrated in a loop that for each qubit, will append an Hadamard gate to the circuit (this is done with the ‘append!’ function).

When we apply the H-gate to each 3 qubits, the circuit will prepare a superposition of all possible states. Resulting in a superposition of 8 states from (|000 > 𝑡𝑜 |111 >):

```Julia
# Create the quantum circuit
circuit = QuantumCircuit(n)
# Apply H-gates to all qubits to create a superposition
for i in 1:n
     append!(circuit, HGate(), [i])
end
```

Now we can setup our Grover Iteration. This portion plays as the heart of the program, it will construct the Oracle and Diffusion operations along with an optimal number of times to our quantum circuit. This will increase the probability of finding the target state.
We create our ‘oracle’ using the ‘OracleGate’ function which will flip the signs of amplitude of the target state. It will construct an oracle for 𝑛 qubits. With our Target specifying the state that the algorithm if looking for.

Our ‘DiffusionOperator’ will amplify the probability amplitude of our Target state. Increasing the measuring chances of our target state once the algorithm finishes running. An essential part of this is combining the oracle and diffusion, after we set both components up, into a single state.

It's important to remember that our algorithm requires approximately $\sqrt{n}$ iterations to fully enhance the probability of measuring our target state.

We initialize a calculation formula for this called ‘num_iterations’ and have it round to the nearest integer. Applying right after the Grover iterations to the circuit through a ‘for’ loop:

```Julia
# Grover iteration
oracle = OracleGate(n, target) # Creating the oracle diffusion = DiffusionOperator(n) # Creating the diffusion operator
grover_iteration = CompositeGate([oracle, diffusion])
# Number of iterations is approx: sqrt(N)
num_iterations = Int(ceil(sqrt(N)))
for _ in 1:num_iterations
     append!(circuit, grover_iteration)
end
```

Wrapping up, we will run the quantum circuit that we set up on a simulator to visualize the outcome. This will illustrate the efficacy of Grover’s algorithm as it is finding a specific item in the unstructured database.

Integrate the quantum simulator ‘qasm_simulator’ from Qiskit’s Aer module to mimic the behavior of a real quantum computer. It will execute the quantum circuit we created on this simulator. The simulator will run 1024 shots to get a fair statistical distribution of the outcome. Once done, the results are extracted, giving us the number of times each possible state ({000},{001}, etc) was measured on all runs. These are then visualized in a bar chart, having each bar represent the frequency of a particular state.

```Julia
# Simulate the circuit + measure results
backend = Aer.get_backend("qasm_simulator") job = execute(circuit, backend, shots=1024) result = job.result()
# Visualize the final results

counts = result.get_counts(circuit)
plot(bar(counts))
```

The program demonstrates how Grover’s algorithm can be implemented and visualized using Julia and the Qiskit framework. To give a full overview of the program, you can find the final resulting code [HERE](GroverAlgoJulia.jl)
>To access the program in Python, view [HERE](GroverAlgoPython.py)


---
## Chapter Four
### Real World Applications
* 4.0: Grover’s application in real world scenarios

Grover’s algorithm can be categorized as a fairly new concept in comparison to other classical algorithms. Although overtime Grover’s algorithm has made a significant academia impact and advancement, there is not a wide-spread level of its application. 

However, the algorithm is beginning to make some promising impact. Certain fields can be pointed out. In Cryptography, the algorithm plays a part in searching large sets of data to crack cryptographic codes. Specifically cracking symmetric key algorithms. Simplifying the way Security experts break down quantum-resistant encryption methods for potential threats. This is called post-quantum cryptography, which we will explore with an example using Python.

* 4.1: Post-quantum Cryptography

In this section , we will be coding a simple lattice based key exchange with Python, Implementing the Learning with Errors (LWE) problem. This is part of the Lattice-based cryptography method which is consistent with resisting attacks from both quantum and classical computers.

We will be generating public and private keys for ‘Ember’ and ‘Daniel’ based on lattice structure. It will initialize parameters to create a secure key exchange for both parties. Ember and Daniel will exchange public keys to independently compute a shared secret. This approach will demonstrate quantum-resistant cryptographic mechanism, showing how cryptography is consistently evolving to ensure better security in quantum computing

First, we must install the ‘latticecrypto’ package using pip:
```
Pip install latticecrypto
```

Now we can perform the following lattice-based key exchange. From the package ‘latticecrypto’ we will import the ‘LWEKeyExchange’ library and initialize the LWE key exchange parameters. ‘n’ will represent our dimension of lattice, while ‘q’ and ‘std_dev’ will be our modulus and standard deviation for the error distribution:

```Python
From latticecrypto import LWEKeyExchange #LWE key exchange param
lweParams = {
     'n': 512,
     'q': 4093,
     'std_dev': 3.2
}
```

We follow this up by initializing the key exchange objects for the two parties (Ember & Daniel). We generate Ember and Daniel’s public and private keys using the generate_keypair() method:

```Python
#initialize key exchange objects
Ember = LWEKeyExchange(lweParams)
Daniel = LWEKeyExchange(lweParams)

#Embers public and private keys
Ember_public_key, Ember_private_key = Ember.generate_keypair()

#Daniels public and private keys
Daniel_public_key, Daniel_private_key =
Daniel.generate_keypair()
```

Ember and Daniel need to exchange their keys, so we will exchange them to generate the shared secret:
```Python
Ember_shared_secret =
Ember.generate_shared_secret(Daniel_public_key,
Ember_private_key)

Daniel_shared_secret =
Daniel.generate_shared_secret(Ember_public_key,
Daniel_private_key)
```

Once Ember and Daniel have exchanged their keys, that exchange is saved under each individual’s secret variable. For this to run efficiently, we check if the shared secrets are the same:
```Python
#checking shared secrets are the same
Assert Ember_shared_secret == Daniel_shared_secret
print("Shared secret has been established successfully")
```

The shared secret can be used now for further operations. Many classical cryptographic algorithms, such as RSA and ECC, run the risk of being broken. However, with Lattice-based cryptography we don’t run that risk. It offers a promising alternative capable of withstanding quantum computer-based attacks.This is a vital area of research in the field of ethical hacking and cybersecurity.

To give a full overview of the program, you can find the final resulting code [HERE](LatticeKeyExchange.py)


---

## Chapter Five
### Conclusion
* 5.0:Reflection

The exploration of Grover’s algorithm in Quantum, as we went into detail in this article, marks the immense advancement in our research of Quantum Computing and Quantum search algorithms. With the roots of its seminal work and founder Lov Grover, Grover’s algorithm presents a speedup solution to the limitations of classical search algorithms. Offering a more efficient and fast approach to searching elements in unstructured databases. This is not just a theoretical approach, but a practical implementation. We developed real world applications through demonstrations of various programming languages such as Julia and Python3. Through them we reflected on the algorithms ability to optimize search efficiencies in a time dominated by big data and complex computational problems. Visualizing the simplification of managing difficult data.

The research presented in this article offers a comprehensive overview of Grover’s algorithm and its efficiency in searching data. We’ve discussed its logical foundation, computational implementations, and real-world applications. This was done with the intention to shed light on the algorithms capabilities but it also paves the way for further research and development in quantum search algorithms. This article serves as a testament to the transformative and dynamic nature of quantum computing and its potential to revolutionize various sectors. From data security to cryptography, quantum is building better security approaches for complex data.

As Quantum computers continue to evolve, the insights garnered from research articles like this will be a key instrument in harnessing the full potential of Quantum algorithms for solving some of the most complex and challenging problems in computer science.

