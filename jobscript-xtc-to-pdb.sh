#!/bin/bash
#SBATCH -J lightdock
#SBATCH --output=align_%j.out
#SBATCH --error=align_%j.err
#SBATCH --ntasks=16
#SBATCH --time=0-01:59:59 # we fast boiiiii
#SBATCH --qos=debug

module load ANACONDA/2019.10
module load intel mkl impi gcc # 2> /dev/null
module load impi
module load boost/1.64.0

GPFS=/gpfs/projects/nct01/nct01055
ZDOCK_PATH=$GPFS/set1/set1/zdock

eval "$(conda shell.bash hook)"
conda activate /gpfs/projects/nct01/nct01051/utils/mdtraj/
python /gpfs/projects/nct01/nct01051/utils/transform_pdb.py $ZDOCK_PATH $ZDOCK_PATH/reference_topology.pdb -c 16
