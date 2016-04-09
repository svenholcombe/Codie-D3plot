## Project
cmake_minimum_required(VERSION 3.0)

project ("QD-D3plot")
#enable_testing()


## Files
file(GLOB_RECURSE srcs_db    src/db/*.cpp)
file(GLOB_RECURSE srcs_dyna  src/dyna/*.cpp)
file(GLOB_RECURSE srcs_util  src/utility/*.cpp)
#file(GLOB_RECURSE libs_fz_win  lib/Windows_VS2010_MT/x64/*.lib)

## Linking
#LINK_DIRECTORIES(lib/Linux/64Bit)

## Test
add_library(codie-d3plot SHARED ${srcs_db} ${srcs_dyna} ${srcs_util})
#add_executable(codie-test src/test/test.cpp ${srcs_db} ${srcs_dyna} ${srcs_util})
#add_library(codie-d3plot STATIC ${srcs_db} ${srcs_dyna} ${srcs_util})


## Compiler Stuff
#TARGET_LINK_LIBRARIES(codie-test femunzip_dyna_standard ipp_z ippcore ippdc ipps ifcore ifcoremt imf ipgo irc svml ippcore_l stdc++ dl)
#TARGET_LINK_LIBRARIES(codie-d3plot femunzip_dyna_standard ipp_z ippcore ippdc ipps ifcore_pic ifcoremt imf ipgo irc svml ippcore_l stdc++ dl cr)
#TARGET_LINK_LIBRARIES(codie-d3plot ${libs_fz_win})


#target_compile_options(codie-test PUBLIC -std=c++11 -Wall -fPIC -O2 -DQD_DEBUG)
#target_compile_options(codie-d3plot PUBLIC -std=c++11 -Wall -fPIC -O2 -DQD_DEBUG)

