#!/bin/bash

INPUT="example.proto"

mkdir -p out

# TODO: This step should be integrated into a proper pipeline. The current code
# is only for demonstration purposes and very brittle.
cp $INPUT $INPUT.tmp
python3 transform.py <$INPUT.tmp >$INPUT ; protoc --cpp_out out/ $INPUT
mv $INPUT.tmp $INPUT
