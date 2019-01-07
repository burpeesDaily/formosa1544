cmake_minimum_required (VERSION 3.5)
project(QuickStart)

set(QUICK_START_VERSION_MAJOR 1)
set(QUICK_START_VERSION_MINOR 0)

set(SOURCES ${PROJECT_SOURCE_DIR}/src/QuickStart.cpp)

include_directories("${PROJECT_SOURCE_DIR}/include")

add_library(QuickStart STATIC ${SOURCES})

enable_testing()

add_subdirectory(test)