def create_distances_matrix(samples_list):
    """
    creating distances matrix, distances_matrix[i][j] is the distance between sample i and sample j
    :param samples_list: list of Samples
    :return: 2D matrix of distances
    """
    num_of_samples = len(samples_list)
    distances_matrix = [[0 for x in range(num_of_samples)] for x in range(num_of_samples)]

    for i in range(num_of_samples):
        for j in range(num_of_samples):
            if i==j:
                continue
            distances_matrix[i][j] = samples_list[i].compute_euclidean_distance(samples_list[j])
            distances_matrix[j][i] = distances_matrix[i][j]

    return distances_matrix

