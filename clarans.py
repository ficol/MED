import random

class Clarans:
    def __init__(self, data, clusters_amount, numlocal, maxneighbor):
        self.data = data
        self.clusters_amount = clusters_amount
        self.numlocal = numlocal
        self.maxneighbor = maxneighbor
        self.best_medoids = []
        self.best_clusters = []
        self.best_cost = float("inf")
    
    def cluster(self):
        i = 1
        while i <= self.numlocal:
            current_medoids = random.sample(range(len(self.data)), self.clusters_amount)
            current_clusters, current_cost = self.update_clusters(current_medoids)
            j = 1
            while j <= self.maxneighbor:
                # print(i, j, self.maxneighbor)
                neighbor_medoids = self.get_neighbor_medoids(list(current_medoids))
                neighbor_clusters, neighbor_cost = self.update_clusters(neighbor_medoids) 
                if neighbor_cost < current_cost:
                    current_medoids = neighbor_medoids
                    current_clusters = neighbor_clusters
                    current_cost = neighbor_cost
                    j = 1
                else:
                    j += 1
            if current_cost < self.best_cost:
                self.best_medoids = current_medoids
                self.best_clusters = current_clusters
                self.best_cost = current_cost    
            i += 1
        return self.best_medoids, self.best_clusters
    
    def get_neighbor_medoids(self, medoids):
        to_swap = random.randrange(len(medoids))
        medoids[to_swap] = random.choice(list(set(range(len(self.data))) - set(medoids)))
        return medoids
        

    def update_clusters(self, medoids):
        clusters = [[] for _ in range(len(medoids))]
        cost = 0
        for index, element in enumerate(self.data):
            distances = [self.get_distance(self.data[medoid], element) for medoid in medoids]
            argmin_distance = min(range(len(distances)), key=lambda i: distances[i])
            clusters[argmin_distance].append(index)
            cost += distances[argmin_distance]
        return clusters, cost       
    
    def get_distance(self, x, y):
        return sum((x[dim] - y[dim])**2 for dim in range(len(x)))



if __name__ == "__main__":
    clarans = Clarans([[1], [2], [3], [400], [5], [100], [101], [102], [103]], 8, 10, 10)
    medoids, clusters = clarans.cluster()
    print(medoids, clusters)
