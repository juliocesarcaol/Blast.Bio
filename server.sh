#!/bin/bash
ls
makeblastdb -in db.fas -dbtype nucl -parse_seqids
python3 p5.py
