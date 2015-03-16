
# C++ CMake template

Setting up a new CMake project can consume a lot of time, especially if you want to set up dependencies,
generate documentation and set up automated testing.

This CMake template speeds up the process by providing a complete project with C++11, Doxygen and googletest integration.
When using it for the first time, run

    $ python init.py

and answer a few questions (name, version, ...) to initialize your project.
This will customize the name of the executable, the documentation, and so on.

To build the project, run

    $ mkdir build
    $ cd build
    $ cmake ..
    $ make

By default, the project will be compiled to both a library and an executable (via main.cpp).
You can add additional source files in `src/CMakeLists.txt` by modifying the line

    set(SRC ...)

### Doxygen

Documentation can be generated with

    $ make doc

A tutorial on the doxygen syntax can be found [here](http://www.stack.nl/~dimitri/doxygen/manual/docblocks.html).

### googletest

You can also make use of the googletest library to write and execute automated tests.
Simply create new tests in the `test` directory.
They will be automatically compiled into an executable and can be run with

    make check

For an introduction to writing tests with googletest, follow [this link](http://code.google.com/p/googletest/wiki/Primer).

