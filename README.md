
# useirn

uSEIRn is a package to solve the Non-Markovian SEIR model with
arbitrary distributions for exposed/infected.

This is the python/cython version of the julia solvers developped by
A. Ramos:  https://gitlab.ift.uam-csic.es/alberto/uSEIR.jl

## usage
start by sourcing the setup script:
```
source setup.sh
```
You will get a printout
```
Usage:

source setup.sh export_path
source setup.sh compile_cython
source setup.sh clean
```
Running the first command will add the directory to your python path, while
the second command will compile the cython code.

The directory **nb** contains two notebooks:
uSEIR.ipynb : example of application including cython/python code
uSEIRApp.ipynb: same example, but code is imported from files.   


## License

"THE BEER-WARE LICENSE":
P. Hernandez, C. Pena, J.J. Gomez Cadenas wrote these files. As long
as you retain this notice you can do whatever you want with this
stuff. If we meet some day, and you think this stuff is worth it, you
can buy us a beer in return.
