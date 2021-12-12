import os
import mdtraj as md
import numpy as np
from pycompss.api.task import task
from pycompss.api.parameter import IN
import sys

FOLDER_NAME = 'zdock'
FOLDER = '/home/nct01/nct01055/pdb/zdock'
REFERENCE_TOPOLOGY = 'reference_topology.pdb'
rt = os.path.join(FOLDER, REFERENCE_TOPOLOGY)

@task(i=IN, j=IN)
def compute_rmsd(i, j):
    pose1 = f'{FOLDER}/{FOLDER_NAME}_{i}.pdb'
    pose2 = f'{FOLDER}/{FOLDER_NAME}_{j}.pdb'

    t1 = md.load(pose1, top=rt)
    t2 = md.load(pose2, top=rt)
    rmsd = md.rmsd(t1, t2, 0)
    print(i, j, rmsd, sep=',')


if __name__ == '__main__':
    n = len(os.listdir(FOLDER)) - 1

    for i in range(1, n - 1):
        for j in range(i + 1, n):
            compute_rmsd(i, j)
