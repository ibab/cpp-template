
# C++ CMake template

## Rationale

Compiling large C++ applications is a complicated process with potentially many steps, as every source file needs to be compiled to an object file before the collection of all object files can be linked into a library or executable.

The command line utility `make` has been created to streamline this process.
Given instructions on how to build a project in the form of a `Makefile`, it only performs the compilation steps that are necessary to bring the application to its most up-to-date state.

But `Makefile`s are tedious to write by hand and difficult to write in a way that is portable between different operating systems and computers.
This is where high-level build tools like CMake come into play.
CMake allows you to specify build instructions in a more abstract and powerful way.
It can then generate a `Makefile` on demand, or export your build instructions into other formats, like those used by your IDE (CodeBlocks, Eclipse, XCode, ...).

This CMake template should be well-suited for starting a new C++ project.
It is preconfigured to allow you to compile an executable or library from a collection of source files in the `src` directory.

It also allows you to define and run automated tests of your code (with [googletest](http://code.google.com/p/googletest/)), as well as generate documentation from the source files (with [Doxygen](http://www.stack.nl/~dimitri/doxygen/)).

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

### GTest

You can also make use of the googletest library to write and execute tests.
Simply create new tests in the `test` directory.
They will be automatically compiled into an executable.
For an introduction to writing tests with googletest, follow [this link](http://code.google.com/p/googletest/wiki/Primer).


