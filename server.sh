#!/bin/bash
ls
makeblastdb -in out.fas -dbtype nucl -parse_seqids
python3 blast.py
