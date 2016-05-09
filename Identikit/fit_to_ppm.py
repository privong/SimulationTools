#!/usr/bin/env python
#
# fit_to_ppm.py
#
# Take stellar kinematics information from an IFU fit and generate Identikit
# projections for dynamical modeling.

import argparse

parser = argparse.ArgumentParser(description='Generate Identikit projections \
from fits to IFU cubes.')
parser.add_argument('--output', '-o', default='idkit', type=str,
                    help='Root name for ppm files.')
parser.add_argument('--velocity', '-v', default=None, type=str,
                    help='Velocity range, given as a comma separated string. \
e.g., "-200,200"')
parser.add_argument('infile' type=str,
                    help='File of binIDs and velocity information.')
parser.add_argument('bininfo', type=str,
                    help='Voronoi bin information.')
args = parser.parse_args()

import numpy as np

