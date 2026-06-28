from qiskit.circuit import Parameter, QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.primitives import StatevectorSampler
from qiskit.quantum_info import Operator
from qiskit import transpile
from qiskit.circuit.library import HGate
from qiskit_aer import AerSimulator
import numpy as np

def check_params(func, *args, **kwargs):
    bound_args = inspect.signature(func).bind(*args, **kwargs)
    return bound_args.arguments

def quantum_rng(number_range, register=None, h_gate=None, reset=None):
    if reset and register is None and h_gate is None:
        quantum_reg = QuantumRegister(1, name="q")
        classical_reg = ClassicalRegister(1, name="c")
        qc = QuantumCircuit(quantum_reg, classical_reg)
        qc.append(HGate(), [0])
        qc.reset(0) 
        return qc
    
    quantum_reg = QuantumRegister(register, name="q")
    classical_reg = ClassicalRegister(register, name="c")
    qc = QuantumCircuit(quantum_reg, classical_reg)
    
    if h_gate is not None:
        for number in range(1, number_range):
            qc.append(HGate(), [number])
        me = qc.measure_all(add_bits=False)
        simulator = AerSimulator()
        job = simulator.run(qc, shots=1024)
        result = job.result()
        counts = result.get_counts()
        return counts
