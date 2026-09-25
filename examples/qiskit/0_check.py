import sys
import qiskit
import qiskit_machine_learning
import qiskit_ibm_runtime
import sklearn
import numpy
import pandas
import matplotlib
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

print("Python                 ", sys.version.split()[0])
print("qiskit                 ", qiskit.__version__)
print("qiskit-machine-learning", qiskit_machine_learning.__version__)
print("qiskit-ibm-runtime     ", qiskit_ibm_runtime.__version__)
print("scikit-learn           ", sklearn.__version__)
print("numpy                  ", numpy.__version__)
print("pandas                 ", pandas.__version__)
print("matplotlib             ", matplotlib.__version__)


qc = QuantumCircuit(1)
qc.h(0)
qc.measure_all()

result = StatevectorSampler().run([qc], shots=1000).result()
print("\nCounts from 1000 runs:", result[0].data.meas.get_counts())