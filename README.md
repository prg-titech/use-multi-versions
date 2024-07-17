## Use Multiple Version of NumPy 
This repository contains a Python program that dynamically loads different versions of the NumPy library.

### SetUp
Before execution, dynamically loaded packages need to be installed in local environment.
```bash
pip download numpy==1.26.4
mkdir numpy-1.26.4
pip install {.whl file created when downloading numpy 1.26.4} --target=numpy-1.26.4

pip download numpy==2.0.0
mkdir numpy-2.0.0
pip install {.whl file created when downloading numpy 2.0.0} --target=numpy-2.0.0
```

### Run
```bash
python3 main.py
```

- To use other NumPy versions, change the implementation of version_dispatch.load_numpy