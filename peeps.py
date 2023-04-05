#!/usr/bin/env python

# name    :	peeps.py
# version :	0.0.1
# date    :	20230329
# author  :	Leam Hall
# desc    :	Create a small number of NPCs for a 3d6 game


import argparse
import random

from peeps import peeps

if __name__ == "__main__":

    args = {}
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "-i", "--init", 
        action  = "store_true", 
        help    = "Initialize data")
    argparser.add_argument(
        "-f", "--family",
        action  = "store_true",
        default = False,
        help    = "Create a family")
    argparser.add_argument(
        "--f-age",
        default = 16,
        type    = int,
        help    = "Age of the father, in years") 
    args = argparser.parse_args()

    if args.init:
        peeps.peep_init()
        sys.exit(0)
    elif args.family:
        data = {}
        if args.f_age > 14:
            data['f_age'] = args.f_age 
        family = peeps.start_family(data)
        peeps.print_family(family)
    else:
        print(peeps.peep_builder({}))
 
