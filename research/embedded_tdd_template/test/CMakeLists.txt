cmake_minimum_required(VERSION 3.0.0)
project(firmware_test)
enable_testing()

### firmware directory
get_filename_component(ROOT_DIR ${CMAKE_CURRENT_SOURCE_DIR} DIRECTORY)
set(FW_SRC_DIR ${ROOT_DIR}/firmware/Project)

## GTest include
find_package(GTest REQUIRED)

## build firmware again with gcc
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIE -no-pie")

############################## test1 ############################## 
set(TEST multiply) # only change this
# test lib build
add_library(${TEST} ${FW_SRC_DIR}/${TEST}/Src/${TEST}.cpp)
target_include_directories(${TEST} PUBLIC ${FW_SRC_DIR}/${TEST}/Inc)
# test executable build
set(TEST_SRC Src/${TEST}_test.cpp)
set(TEST_TEST ${TEST}_TEST)
add_executable(${TEST_TEST}
    ${TEST_SRC})
target_include_directories(${TEST_TEST} PUBLIC
    GTest::GTest
    ${TEST})
target_link_libraries(${TEST_TEST} PUBLIC
    GTest::GTest
    ${TEST})
# add test
add_test(${TEST}_gtest ${TEST_TEST})

############################## test2 ############################## 
set(TEST add) # only change this
# test lib build
add_library(${TEST} ${FW_SRC_DIR}/${TEST}/Src/${TEST}.cpp)
target_include_directories(${TEST} PUBLIC ${FW_SRC_DIR}/${TEST}/Inc)
# test executable build
set(TEST_SRC Src/${TEST}_test.cpp)
set(TEST_TEST ${TEST}_TEST)
add_executable(${TEST_TEST}
    ${TEST_SRC})
target_include_directories(${TEST_TEST} PUBLIC
    GTest::GTest
    ${TEST})
target_link_libraries(${TEST_TEST} PUBLIC
    GTest::GTest
    ${TEST})
# add test
add_test(${TEST}_gtest ${TEST_TEST})