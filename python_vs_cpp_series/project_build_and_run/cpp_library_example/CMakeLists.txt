cmake_minimum_required (VERSION 3.10)
project(MyLib)

set(SOURCES ${PROJECT_SOURCE_DIR}/src/MyLib.cpp)

include_directories(${PROJECT_SOURCE_DIR}/include)

add_library(mylib STATIC ${SOURCES})
