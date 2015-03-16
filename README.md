
# C++ CMake template

This CMake template sets up a new C++ project with C++11, Doxygen and googletest integration.
When using it template for the first time, run

    $ python init.py

and answer the questions to initialize your project.

To build the project:

    $ mkdir build
    $ cd build
    $ cmake ..
    $ make

By default, the project will be compiled to both a library and an executable (via main.cpp).
You have to add additional source files in `src/CMakeLists.txt` by modifying the line

    set(SRC ...)

### Doxygen

This template is integrated with doxygen for producing documentation.
If you have doxygen installed, simply execute

    $ make doc

in the build directory to create the documentation.
A tutorial on the doxygen syntax can be found [here](http://www.stack.nl/~dimitri/doxygen/manual/docblocks.html).

### googletest

You can also make use of the googletest library to write and execute tests.
Simply create new tests in the `test` directory.
They will be automatically compiled into an executable and can be run with

    make check

For an introduction to writing tests with googletest, follow [this link](http://code.google.com/p/googletest/wiki/Primer).

