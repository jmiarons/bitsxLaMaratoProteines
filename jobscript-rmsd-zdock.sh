#!/bin/bash
#SBATCH -J lightdock
#SBATCH --output=jobscript_output/align_%j.out
#SBATCH --error=jobscript_output/align_%j.err
#SBATCH --ntasks=48
#SBATCH --time=0-01:59:59 # we fast boiiiii
#SBATCH --qos=debug

module load ANACONDA/2019.10
module load intel mkl impi gcc # 2> /dev/null
module load impi
module load boost/1.64.0

eval "$(conda shell.bash hook)"
conda activate /gpfs/projects/nct01/nct01051/utils/mdtraj/

export OMP_NUM_THREADS=48
python run_rmsd.py
# python run_rmsd_compss.py
