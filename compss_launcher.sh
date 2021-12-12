#!/bin/bash

export COMPSS_PYTHON_VERSION=3

module load COMPSs/2.10

enqueue_compss --exec_time=60 --num_nodes=1 --cpus_per_node=48 --lang=python --pythonpath=/home/nct01/nct01055/pdb --debug --tracing run_rmsd_compss.py
