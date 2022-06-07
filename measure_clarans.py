from timeit import default_timer as timer
import argparse

from pyclustering.cluster.silhouette import silhouette
import numpy as np

from clarans import Clarans
from data import load_data, visualize

def run_clarans(data, clusters_amount, numlocal, maxneighbor):
    clarans = Clarans(data, clusters_amount, numlocal, maxneighbor)
    start = timer()
    medoids, clusters = clarans.cluster()
    end = timer()
    return (end - start), clusters, medoids

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str, default=None, help='filename to load data')
    parser.add_argument('numlocal', type=int, default=None, help='numlocal parameter of clarans')
    parser.add_argument('maxneighbor', type=int, default=None, help='maxneighbor parameter of clarans')
    parser.add_argument('--plot', action='store_true', help='if visualize results')
    args = parser.parse_args()
    data, clusters_amount = load_data(args.file)
    time, clusters, medoids = run_clarans(data, clusters_amount, args.numlocal, args.maxneighbor)
    print(f'Time: {time}')
    print(f'Silhouette score: {np.mean(silhouette(data, clusters).process().get_score())}')
    if args.plot:
        visualize(data, clusters, medoids)
