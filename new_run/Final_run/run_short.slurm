#!/bin/bash
#
##SBATCH --id=fin
##SBATCH --nodelist=n002
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=64
#SBATCH --time=5-00:00:00 
#SBATCH -p long

str = ""
for ((i = 1; i <= 64; i++)); do
    str="$str ${i}"
    python edit_lamps.py $i
done
printf str
parallel --delay .5 --joblog run_parallel.log '/home/rajat/anaconda3/envs/my-lammps-env/bin/lmp_serial -in protein_run/protein_run{1}.in' ::: $str

parallel --delay .5 --joblog run_parallel.log 'python trans_time.py {1}' ::: $st
