
#include <gtest/gtest.h>

#include "hello.h"

TEST(Feature, get_message)
{
    std::string m = get_message();
    ASSERT_EQ("Hello, World!", m);
}
