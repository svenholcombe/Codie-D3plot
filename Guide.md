 
# Python guide

The codie python library can be used to read a D3plot and access it's data in python. 

# Installation

In order to install the package use the .whl (python wheel) if possible, since they contain already compiled code. Otherwise you may use the setup.py with "python2 setup.py install". Compilation was tested with Visual Studio for Python on Windows, as well as gcc on OpenSuse.

# D3plot

To use the module just import the D3plot class from the module. The **D3plot** instance has the following functions:

**D3plot(filepath,use_femzip=False,read_states=None)**

*return: instance of the d3plot class.*

Read a d3plot with basic geometry into the memory. The second option is meant to be used for femzipped result files. use_femzip is optional and False by default. The pre-compiled .whl is compiled with femzip. The option read_states works the same as the function d3plot.read_states and is meant to save time to already load state variables on first time loading.

**d3plot.get_filepath()**

*return: (string) filepath*

Get the path of the file the d3plot is operating on.

**d3plot.get_timesteps()**

*return: (list of floats) output time*

Get a list of time-steps at which the data was written to the d3plot.

**d3plot.get_nodeByID(arg)**

*return: node or list of nodes*

The a node or a list of nodes, depending on the argument. One can either use just a node id (thus an integer) or a list of ids (thus a list of int). In the second case the function returns a list of nodes. 

**d3plot.get_elementByID(element_Type,arg)**

*return: element or list of elements*

This function takes two arguments. The first one is the element type. It may be a string "beam", "shell" or "solid". This is necessary due to the reason that ls-dyna is the sole solver which can use the same id for two different element types. The second argument may be either an id or a list od ids.

**d3plot.get_partByID(id)**

*return: part*

Get a part instance by it's id.

**d3plot.get_parts()**

*return: list of parts*

Get all the parts in the d3plot.

**d3plot.read_states(arg)**

*return: None*

Argument arg may be a string or a list of strings.

Read a variable from the state files. If this is not done, the nodes and elements return empty lists when requesting a result. The variables available are:
- disp = displacement 
- vel = velocity
- accel = acceleration
- strain [(optional) mode]
- stress [(optional) mode]
- plastic_strain [(optional) mode]
- history [id1] [id2] ... [shell or solid] [(optional) mode]

Additionally one has to keep in mind that shells contain multiple output layers with results. Therefore additional modes where introduced in order to specify the handling of multiple outputs.
- in/mid/out
- max/min/mean

In order to read the plastic-strain considering only the maximum over all integration layers use: "plastic_strain max". Default is mean, if no mode is given. When reading history variables, one MUST specify type (shell/solid) and at least one index starting at 1. 

# Node

The **Node** class has the following functions:

**node.get_id()**

*return: the node id.*

**node.get_coords(int iTimestep = 0)**

*return: (list of floats) 3D-coordinates*

The geometrical coordinates of the node. Coordinates can also be loaded from different timesteps, in which case displacements must be loaded though (see d3plot.read_states). iTimestep may also be negative to access coordinates backwards (e.g. -1 for last timestep), similar to python array syntax.

**node.get_disp()**

*return (list of list of floats) time series of displacement*

The the time series of the displacement of the node. The first index is the time state and the second index the space coordinate index.

**node.get_vel()**

*return (list of list of floats) time series of the velocity vector*

**node.get_accel()**

*return (list of list of floats) time series of the acceleration vector*

**node.get_elements()**

*return (list of elements) elements of the node.*

# Element

The **Element** class has the following functions:


**element.get_id()**

*return: the element id*

**element.get_plastic_strain()**

*return: (list of floats) time series of plastic strain values*

**element.get_energy()**

*return: (list of floats) time series of element energy*

**element.get_strain()**

*return: (list of list of floats) time series of the strain vector*

This function returns a time series of the strain vector. The vector contains the 6 values of the strain vector [exx,eyy,ezz,exy,eyz,exz].

**element.get_stress()**

*return: (list of list of floats) time series of the stress vector*

This function returns a time series of the stress vector. The vector contains the 6 values of the stress vector [sxx,syy,szz,sxy,syz,sxz].

**element.get_nodes()**

*return: (list of nodes) nodes of the elements*

**element.get_coords(iTimestep=0)**

*return: (list of flaot) Get the coordinates of the element.*

You can get the coordinates of the element, which is the mean of it's nodes coordinates. If the optional flag iTimtestep != 0 then the displacements must be read in the d3plot. One also may use negative numbers like -1 for the last timestep.

**element.get_history()**

*return: (list of list of floats) time series of the history variable vector

This function returns the time series of the history variables. The first index is the timestep and the second index the loaded variable. The history variables loaded in shells and solids may be different!

**element.get_estimated_size()**

*return: estimated element size*

Calculates an average element size for the element. The size is not highly accurate for performance reasons, but is a good indicator for the dimensional size though.

# Part

The **Part** class has the following functions:


**part.get_id()**

*return: (int) get the id of the part*

**part.get_name()**

*return: (string) part get_name*

**part.get_nodes()**

*return: (list) nodes of the part*

**part.get_elements()**

*return: (list) elements of the part*

# Memory management
The whole memory magic is taking place in the native c++ code. A python instance of class node only has a pointer the instance in c++, as well as it's python-d3plot (in order to prevent python garbage collection). In order to allow python to garbage collect a d3plot, all of it's references must be gone. Since every instance from that d3plot (node, part and element) keep a reference to it, also all of these must be deleted to allow the release of the d3plot in memory. This is utterly important when post-processing a DOE for example.

The native c++ code saves the results as small as possible (floats and ints). If python requests those values, they are converted into double and long. Remember that retrieving results is a copy-process in memory, as well as an additional increase due to the use of the bigger data types.