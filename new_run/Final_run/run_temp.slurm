#!/bin/bash
#
##SBATCH --id=short_run
##SBATCH --nodelist=n005
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=64
#SBATCH --time=5-00:00:00 
#SBATCH -p long

str = ""
for ((i = 1; i <= 64; i++)); do
    str="$str ${i}"
done
printf str
parallel --delay .5 --joblog run_parallel.log 'python trans_time.py {1}' ::: $str
