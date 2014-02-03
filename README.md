
# C++ CMake template

## Instructions

When using this template for the first time, run

    $ python init.py

and answer the questions to initialize your project.

To build your project, create a build directory

    $ mkdir build

and execute cmake from inside this directory:

    $ cd build
    $ cmake ..
    $ make

You can add additional source files in
`src/CMakeLists.txt` by modifying

    set(SRC ...)


