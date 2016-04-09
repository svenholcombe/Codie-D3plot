
# Codie-D3plot

This project contains a reader of binary result files coming from the commercial FEM-Code LS-DYNA. This project is not affiliated in any way with the creators or distributors of LS-Dyna and thus is totally unofficial.

The core-code is written entirely in C++ with a python-2.7 wrapper. Even though the code is being validated with big effort, there always may be mistakes and bugs. The reader is very touchy in terms of checks, so if anything will go wrong during reading, an exception will be thrown.
Use the python wheels in "dist" if possible for installation on windows: pip install [wheel filename].whl. The python weel is compiled with femzip support.

The focus of this project was mainly **speed and usability**. As a result the **memory consumption** for bigger models is **quite high** (5M elements -> 3GB RAM), but still acceptable. The amount is small enough to load two big models at once with one or two results. In future memory consumption might be optimized ... or not.

# Features

The file reader is not finished yet but is currently aiming for the following features:
- Single Precision (DONE), Double Precision (TODO)
- Elements: Beams,Shells,Solids (no thick shells) (DONE)
- Results (DONE)
- no SPH or fluid dynamics planned!

Nodal Results:
- displacement (disp)
- velocity (vel)
- acceleration (acc)

Element Results:
- plastic strain (plastic\_strain) (SHELLS: in/mid/out,min/max,mean)
- stress tensor (stress) (SHELLS: in/mid/out,min/max,mean)
- strain tensor (strain) (SHELLS: in/mid=mean/out,min/max,mean)
- internal energy (energy)
- history variables (history)

The FEM-results are returned within **internal classes** such as **Node or Element** which can be attained by either ID or from parts. For shell elements, which have multiple results (stress and plastic strain per integration layer & 2x strain tensor) the following modes may be used:

Shell result flags:
- in,mid,out
- max,min
- mean (standard)

So if you want to load strains and "mean" the tensor for shells, just provide: "strain mean"

# Python2-Example

```python
from codie import D3plot

d3plot = D3plot("filepath/to/d3plot",read_states="disp")
timesteps = d3plot.get_timesteps()
d3plot.read_states(["plastic_strain max","history 2 shell max"])

node = d3plot.get_nodeByID(7)
node_displacement = node.get_disp()

element = d3plot.get_elementByID("shell",11)
elem_plastic_strain = element.get_plastic_strain()
for node in element.get_nodes():
  print("Node:"+str(node.get_id()))

part = d3plot.get_partByID(13)
part_elems = part.get_elements()

```

# CPP-Example

```cpp
bool use_femzip=false;
vector<string> variables;
variables.push_back("disp");

D3plot* d3plot = new D3plot("filepath/to/d3plot",use_femzip,variables);
vector<float> timesteps = d3plot->get_timesteps();

variables.push_back("plastic_strain max"); 
d3plot.read_states(variables); // double reading of disp is caught

Node* node = d3plot->get_db_nodes()->get_nodeByID(1);
vector<vector<float>> node_displacement = node->get_disp();

Element* element = d3plot->get_elementByID(SHELL,11);
vector<float> elem_plastic_strain = element->get_plastic_strain();
for (auto node : element->get_nodes() )
  cout << "Node:" << node->get_nodeID() << endl;

Part* part = d3plot->get_db_parts()->get_part_fromID(13);
set<Element*> part_elems = part->get_elements();

```

# Tutorial

Will be available with first release.

# License

See the LICENSE file.
