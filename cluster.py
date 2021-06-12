class Cluster:
    def __init__(self, c_id, samples):
        """

        :param c_id: cluster id
        :param samples: list of samples with Sample type
        """
        self.d_id = c_id
        self.samples = samples

    def merge(self, other):
        """
        merging two clusters into one, adding other to self
        :param other:
        :return:
        """
        pass

    def print_details(self, silhouette):
        pass



