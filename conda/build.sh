#!/usr/bin/env bash

TARGET_DIR=${PREFIX}/opt/omnisci-examples/
mkdir -p ${TARGET_DIR}

# remore .git if exists
rm -rf .git

cp -R . ${TARGET_DIR}
