find_package(GTest REQUIRED)

add_executable(multiply_test
    src/multiply_test.cpp)



target_include_directories(multiply_test PRIVATE
    GTest::GTest
    multiply)

target_link_libraries(multiply_test PRIVATE
    GTest::GTest
    multiply)

add_test(multiply_gtests multiply_test)