#!/bin/sh

# Deletes and rebuilds the temporary CMake files

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
CMAKE_BASE_DIR="$(dirname "$DIR")"

if [ -f CMakeLists.txt ]
then
echo "Directory contains CMakeLists.txt. You should use a clean out of source build. Exiting."
exit 1
fi

if [ -f CMakeCache.txt ]
then
echo "Directory contains CMake files, will clean up."
rm -rf bin/ CMake* cmake_install.cmake Makefile lib/ main/ src/
fi

echo "Building CMake build system for installation to $DOOFITSYS."
if [ "$1" = "debug" ]
then
cmake -DCMAKE_INSTALL_PREFIX=$DOOFITSYS -DCMAKE_BUILD_TYPE=Debug $CMAKE_BASE_DIR
elif [ "$1" = "profiling" ]
then
cmake -DCMAKE_INSTALL_PREFIX=$DOOFITSYS -DCMAKE_BUILD_TYPE=Profiling $CMAKE_BASE_DIR
else
cmake -DCMAKE_INSTALL_PREFIX=$DOOFITSYS -DCMAKE_BUILD_TYPE=Release $CMAKE_BASE_DIR
fi
