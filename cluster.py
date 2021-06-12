class Cluster:
    def __init__(self, c_id, samples):
        """
        :param c_id: cluster id (int)
        :param samples: list of samples with Sample type
        """
        self.c_id = c_id
        self.samples = samples

    def merge(self, other):
        """
        adding cluster other to cluster self and sort self by id
        :param other: cluster
        """
        self.c_id = min(self.c_id, other.c_id)
        self.samples.extend(other.samples)
        self.samples.sort(key=lambda x: x.s_id, reverse=False)
        del other

    def print_details(self, silhouette):
        """
        print clusters id's, dominant label, silhouette
        :param silhouette: cluster silhouette value
        """
        pass



