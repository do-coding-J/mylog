#include "add.h"
#include <gtest/gtest.h>

TEST(AddTests, TestIntegerOne_One)
{
    const auto expected = 2;
    const auto actual = add(1,1);
    ASSERT_EQ(expected, actual);
}

TEST(AddTests, TestFloatOnePointFive_OnePointFive)
{
    const auto expected = 3.0f;
    const auto actual = add(1.5,1.5);
    ASSERT_EQ(expected, actual);
}

TEST(AddTests, TestIntegerHundred_Hundred)
{
    const auto expected = 200;
    const auto actual = add(100,100);
    ASSERT_EQ(expected, actual);
}

int main(int argc, char** argv)
{
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
