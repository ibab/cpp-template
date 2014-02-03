
#include <gtest/gtest.h>

#include "hello.h"

TEST(Hello, get_message)
{
    std::string m = get_message();
    ASSERT_EQ("Hello, World!", m);
}
