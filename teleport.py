# -*- coding: utf-8 -*-

# Copyright 2018, IBM.
#
# This source code is licensed under the Apache License, Version 2.0

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import available_backends, execute

# Create a Quantum Register and classical registers with 3 qubits and 3 classical bits.
q = QuantumRegister(3)
c = ClassicalRegister(3)
qc = QuantumCircuit(q, c)

# Prepare an initial state using a single unitary
qc.u1(0.5, q[0])

 # Prepare an entangled pair using qubit ② and qubit ③
qc.h(q[1])
qc.cx(q[1], q[2])

# Barrier to prevent gate reordering for optimization
qc.barrier(q)

# Perform a CNOT between qubit ① and qubit ②
qc.cx(q[0], q[1])

# Measure qubit ② in the computational basis
qc.measure(q[1], c[1])

# Measure qubit ① in the + - basis
qc.h(q[0])
qc.measure(q[0], c[0])

# If needed Perform a phase correction to qubit ③
if c[0] == 1:
    qc.z(q[2])

# If needed Perform a bit flip correction to qubit ③
if c[1] == 1:
    qc.x(q[2])


qc.measure(q[2], c[2])


# Compile and run the Quantum circuit on a simulator backend
job_sim = execute(qc, "local_qasm_simulator")
sim_result = job_sim.result()
print(sim_result)
print(sim_result.get_counts(qc))

