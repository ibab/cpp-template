
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

By default, your project will be compiled to both a library and an executable (via main.cpp).

You can add additional source files in `src/CMakeLists.txt` by modifying the line

    set(SRC ...)

### Doxygen

This template is integrated with doxygen for producing documentation.
If you have doxygen installed, simply execute

    $ make doc

in the build directory to create the documentation for your project.
A tutorial on the doxygen syntax can be found [here](http://www.stack.nl/~dimitri/doxygen/manual/docblocks.html).

### googletest

You can also make use of the googletest library to write and execute tests.
Simply create new tests in the `test` directory.
They will be automatically compiled into an executable.
For an introduction to writing tests with googletest, follow [this link](http://code.google.com/p/googletest/wiki/Primer).

### C++ 11

C++ 11 is the newest released standard of the C++ programming language.
It contains many useful syntax improvements (e.g. for each loop, lambda expressions) and an expanded standard library (e.g. improved random number generators).
By default, this template will only work with C++11 capable compilers.
You can relax this requirement by editing the file `cmake/Include.cmake`.



