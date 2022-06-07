import csv

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
    np.random.seed(10)
    dim = 10
    size = 10000
    data1 = generate_gaussian_clusters(3, [dim * [0], dim * [1], dim * [-1]], 3 * [np.identity(dim).tolist()], 3 * [size])
    save_data('data/normal1', data1)

    dim = 50
    size = 10000
    data2 = generate_gaussian_clusters(3, [dim * [0], dim * [1], dim * [-1]], 3 * [np.identity(dim).tolist()], 3 * [size])
    save_data('data/normal2', data2)

    dim = 100
    size = 10000
    data3 = generate_gaussian_clusters(3, [dim * [0], dim * [3], dim * [-3]], 3 * [np.identity(dim).tolist()], 3 * [size])
    save_data('data/normal3', data3)

    dim = 10
    size = 20000
    data4 = generate_gaussian_clusters(3, [dim * [0], dim * [3], dim * [-3]], 3 * [np.identity(dim).tolist()], 3 * [size])
    save_data('data/normal4', data4)

    dim = 10
    size = 30000
    data5 = generate_gaussian_clusters(3, [dim * [0], dim * [3], dim * [-3]], 3 * [np.identity(dim).tolist()], 3 * [size])
    save_data('data/normal5', data5)

