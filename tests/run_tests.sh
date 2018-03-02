#!/bin/bash
cd ..
coverage run --source moire -m unittest discover -s tests
echo ""
echo "COVERAGE"
echo "========"
coverage report -m
