from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


qc = QuantumCircuit(1)
print("Qubit sitting at 0:", Statevector(qc).data.round(3))


qc.h(0)
qc.h(0)
qc.h(0)


print("After H gate:    ", Statevector(qc).data.round(3))

probs = Statevector(qc).probabilities_dict()
print()
for answer, p in probs.items():
    print(f"  chance of {answer}: {p:.1%}")

print()
print(qc.draw())

