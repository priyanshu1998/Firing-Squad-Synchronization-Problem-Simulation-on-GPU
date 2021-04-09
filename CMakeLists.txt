cmake_minimum_required(VERSION 3.17)
project(fast_FSSP CUDA)

set(CMAKE_CUDA_STANDARD 14)

add_executable(fast_FSSP main.cu)

set_target_properties(
        fast_FSSP
        PROPERTIES
        CUDA_SEPARABLE_COMPILATION ON)