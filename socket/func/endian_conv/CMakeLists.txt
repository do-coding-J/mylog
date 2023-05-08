cmake_minimum_required(VERSION 3.0.0)
project(endian_conv VERSION 0.1.0)

include(CTest)
enable_testing()

set(EXEC endian_conv)

add_executable(${EXEC} main.c)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
