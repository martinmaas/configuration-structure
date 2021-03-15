#!/bin/bash

# Build and run example.
g++ -Iout/ test.cc out/example.pb.cc -lprotobuf
./a.out
