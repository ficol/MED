import csv
import argparse

import numpy as np
from pyclustering.cluster import cluster_visualizer

def generate_gaussian_clusters(clusters_amount, mean, variation, amount):
    data = dict()
    for i in range(clusters_amount):
        data[i] = np.random.multivariate_normal(mean=mean[i], cov=variation[i], size=amount[i]).tolist()
    return data

def save_data(path, data):
    with open(path, 'w') as f:
        for cluster_num in data:
            for point in data[cluster_num]:
                f.write(''.join([','.join(str(i) for i in point)]) + f',{cluster_num}\n')

def load_data(path):
    with open(path) as f:
        csv_reader = csv.reader(f)
        data = list(csv_reader)
        clusters_amount = int(data[-1][-1]) + 1
        data = [[float(i) for i in point[:-1]] for point in data]
    return data, clusters_amount

def visualize(data, clusters, medoids):
    visualizer = cluster_visualizer()
    visualizer.append_clusters(clusters, data)
    visualizer.append_cluster(medoids, data, markersize=14, marker='*', color='black')
    visualizer.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str, default=None, help='filename to save data')
    args = parser.parse_args()
    np.random.seed(10)
    data = generate_gaussian_clusters(3, [[0,0], [10,10], [100,100]], [[[1,0],[0,1]],[[1,0],[0,1]],[[1,0],[0,1]]], [10000,10000,10000])
    save_data(args.file, data)
