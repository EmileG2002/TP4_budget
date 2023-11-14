import os
import argparse


badhash = '1ca217161f9f3c0485c6c7e983e0b7fb77170910'
goodhash = '33827ba712f81ebc7c1fc935e8115e9a49065a9a'

os.system(f'git bisect start {badhash} {goodhash}')
os.system('git bisect run manage.py test')
