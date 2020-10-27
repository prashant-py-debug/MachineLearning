import numpy as np
import matplotlib.pyplot as plt

def eucledean_dist(x ,y):
    return np.sqrt(np.sum((x-y)**2))

class K_mean:

    def __init__(self, k = 5 , max_iter = 100 , plot_step = False):
        self.k = k
        self.max_iter = max_iter
        self.plot_step = plot_step
        
        #list of sample idxs for each cluster
        self.clusters = [[] for _ in range(self.k)]
        self.centroids = []

    def predict(self , X):

        self.X = X
        self.n_samples , self.n_features = X.shape


        #initialize
        random_sample_idx = np.random.choice(self.n_samples , self.k , replace=False)
        self.centroids = [self.X[idx] for idx in random_sample_idx]

        #optimize clusters
        for _ in range(self.max_iter):
            #assign samples to closed centroid
            self.clusters = self._create_clusters(self.centroids)

            if self.plot_step:
                self.plot()


            #calculate new centroid from the cluster
            centroids_old = self.centroids
            self.centroids = self._get_centroids(self.clusters)

            #check is cluster have changed
            if self._is_converged(centroids_old , self.centroids):
                break
            if self.plot_step:
                self.plot()
            

        #classify samples as the index of their cluster
        return self._get_cluster_labels(self.clusters)
    
    def _get_cluster_labels(self, clusters):
        labels = np.empty(self.n_samples)
        for cluster_idx , cluster in enumerate(clusters):
            for samples in cluster:
                labels[samples] = cluster_idx
        return labels



    def _create_clusters(self , centroids):
        # Assign the samples to the closest centroids to create clusters
        clusters = [[] for _ in range(self.k)]
        for idx , sample in enumerate(self.X):
            centroids_idx = self._closet_centroid(sample,centroids)
            clusters[centroids_idx].append(idx)
        return clusters
    
    def _closet_centroid(self, sample , centroids):
        distances = [eucledean_dist(sample , point) for point in centroids]
        closest_index = np.argmin(distances)
        return closest_index
    
    def _get_centroids(self , clusters):
        centroids = np.zeros((self.k , self.n_features))
        for cluster_idx , cluster in enumerate(clusters):
            cluster_mean = np.mean(self.X[cluster], axis = 0)
            centroids[cluster_idx] = cluster_mean
        return centroids
        
    def _is_converged(self , centroids_old , centroids):
        distances = [eucledean_dist(centroids_old[i] , centroids[i]) for i in range(self.k)]
        return sum(distances) == 0
    
    def plot(self):
        fig, ax = plt.subplots(figsize=(12, 8))

        for i, index in enumerate(self.clusters):
            point = self.X[index].T
            ax.scatter(*point)

        for point in self.centroids:
            ax.scatter(*point, marker="x", color='black', linewidth=2)

        plt.show()


        
        






