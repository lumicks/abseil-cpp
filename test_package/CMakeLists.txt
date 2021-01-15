cmake_minimum_required(VERSION 3.2.0)
project(test_package CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

find_package(absl REQUIRED CONFIG)

add_executable(${PROJECT_NAME} main.cpp)
target_link_libraries(${PROJECT_NAME} PRIVATE
    absl::strings
    absl::flat_hash_set 
    absl::flat_hash_map 
    absl::numeric 
    absl::time
)
