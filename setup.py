
from setuptools import setup, Extension
import sys
from sys import platform

# ======= S E T T I N G S ======= #
useFemzip = True
debugging_mode = False
# =============================== #

# Version
_version = "1.3.3"

# Check for MinGW usage
use_mingw=False
for ii in range(len(sys.argv)):
	if (sys.argv[ii] == "-c") and (sys.argv[ii+1] == "mingw32"):
		use_mingw=True
	if (sys.argv[ii] == "--compiler=mingw32"):
		use_mingw=True

# Basic srcs
srcs = ["src/python/wrapper.cpp"
    ,"src/db/DB_Elements.cpp"
    ,"src/db/DB_Nodes.cpp"
    ,"src/db/DB_Parts.cpp"
    ,"src/db/Element.cpp"
    ,"src/db/Node.cpp"
    ,"src/db/Part.cpp"
    ,"src/dyna/D3plotBuffer.cpp"
    ,"src/dyna/d3plot.cpp"
    ,"src/utility/FileUtility.cpp"
    ,"src/utility/IOUtility.cpp"
    ,"src/utility/TextUtility.cpp"
    ,"src/utility/MathUtility.cpp"]

include_dirs = []
	
# FEMZIP yes/no?
compiler_args = []
if useFemzip:

   srcs.append("src/dyna/FemzipBuffer.cpp")
   
   if (platform == "win32"):
		lib_dirs = ['lib/Windows_VS2010_MT/x64']
		libs = ['femunziplib_standard_dyna','ipp_zlib','ippcoremt',
            'ippdcmt','ippsmt','ifwin','ifconsol','ippvmmt','libmmt',
            'libirc','svml_dispmt','msvcrt']
		compiler_args.append("/DCD_USE_FEMZIP")
   else:
      lib_dirs = ['lib/Linux/64Bit']
      libs = ['femunzip_dyna_standard','ipp_z','ippcore',
            'ippdc','ipps','ifcore_pic','ifcoremt','imf',
            'ipgo','irc','svml','ippcore_l','stdc++','dl']
      compiler_args.append("-DCD_USE_FEMZIP")
		
		
# No FEMZIP
else:
		
	lib_dirs = []
	libs = []
		
# Compiler args
# Linux
if (platform == "linux") or (platform == "linux2") or use_mingw:
	compiler_args.append("-std=c++11")
	compiler_args.append("-O3")
	if not use_mingw:
		compiler_args.append("-fPIC")
	if debugging_mode:
		compiler_args.append("-DCD_DEBUG")
# Windows
else:
	if debugging_mode:
		compiler_args.append("/DCD_DEBUG")

# Setup
setup(name="codie",
      version=_version,
      description="This is the codie python utility toolbox for CAE.",
      author="C. Diez",
      author_email="gmjason@gmx.de",
      url="www.qd-coding.com",
      license="GNU GPL 3",
      ext_modules=[Extension("codie", srcs, extra_compile_args = compiler_args,
									  library_dirs=lib_dirs,
									  libraries=libs,
									  include_dirs=include_dirs,)],
      classifiers=[
      'Development Status :: 4 - Beta',
      'Topic :: Utilities',
      'Topic :: Engineering',
      'Topic :: CAE',
      'Topic :: FEM',
      'Programming Language :: Python :: 3.4',
      'Programming Language :: Python :: 3.5'
      ],)
