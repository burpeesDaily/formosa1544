cmake_minimum_required (VERSION 3.10)
project(MyExecutable)

set(SOURCES
    ${PROJECT_SOURCE_DIR}/src/MyLib.cpp
    ${PROJECT_SOURCE_DIR}/src/Main.cpp
)

include_directories(${PROJECT_SOURCE_DIR}/include)

add_executable(myexe ${SOURCES})
