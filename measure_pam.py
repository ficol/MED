from timeit import default_timer as timer
import random
import argparse

from pyclustering.cluster.kmedoids import kmedoids

from data import load_data, visualize

def run_pam(data, initial_medoids):
    kmedoids_instance = kmedoids(data, initial_medoids)
    start = timer()
    kmedoids_instance.process()
    end = timer()
    return (end - start), kmedoids_instance.get_clusters(), kmedoids_instance.get_medoids()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str, default=None, help='filename to load data')
    parser.add_argument('--plot', action='store_true', help='if visualize results')
    args = parser.parse_args()
    random.seed = 1
    data, clusters_amount = load_data(args.file)
    time, clusters, medoids = run_pam(data, random.sample(range(len(data)), clusters_amount))
    print(time)
    if args.plot:
        visualize(data, clusters, medoids)