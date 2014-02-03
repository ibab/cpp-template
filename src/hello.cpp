#include <iostream>

#include "hello.h"

void hello() {
    std::string message = get_message();
    std::cout << message << std::endl;
}

std::string get_message() {
    return "Hellx, World!";
}
