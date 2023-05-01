cmake_minimum_required(VERSION 3.0.0)
project(hello_world_client VERSION 0.1.0)

include(CTest)
enable_testing()

set(EXEC client)

add_executable(${EXEC} main.c)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
