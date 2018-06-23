# -*- coding: utf-8 -*-

# Copyright 2018, IBM.
#
# This source code is licensed under the Apache License, Version 2.0

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import available_backends, execute

# Create a Quantum Register and classical registers with 2 qubits and 2 classical bits.
q = QuantumRegister(2)
c = ClassicalRegister(2)
qc = QuantumCircuit(q, c)

 # Add a H gate on qubit 0 to create a superposition
qc.h(q[0])
# Add a controlled not (CX) with qubit 0 as control and qubit 1 target
qc.cx(q[0], q[1])

# Perform a unitary transformation to obtain one of the other three bell states
# if we want to send 0 then we don't do anything as we are already in the bell computational basis
# if we want to send 1 then perform a X transformation
# if we want to send 2 then perform a Z transformation
# if we want to send 3 then perform a XZ transformation

qc.x(q[0]) 
# qc.z(q[0])    
# qc.x(q[0])
# qc.z(q[0])

# To obtain the encoded value reapply the CX and H transformations followed by a measurement
# This enables us to uncover the value by detecting which bell state we are in
qc.cx(q[0], q[1])
qc.h(q[0])

# Add a Measure gate to see the state.
qc.measure(q, c)

# Compile and run the Quantum circuit on a simulator backend
job_sim = execute(qc, "local_qasm_simulator")
sim_result = job_sim.result()
print(sim_result.get_counts(qc))