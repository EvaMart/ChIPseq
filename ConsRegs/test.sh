#!/bin/bash
cd ~/eomes/PARTE2/cons/soft/
ConsRegs='/home/eva/eomes/PARTE2/cons/soft/ConsRegs/ConsRegs.py'
input='/home/eva/eomes/PARTE2/cons/soft/test.out.txt'
output='/home/eva/eomes/PARTE2/cons/soft/ConsRegs/test.consregs.bed'
threshold=0.9

python $ConsRegs $input $output $threshold
