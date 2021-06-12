import sys
import data
import sample
import cluster
import distances

def main(argv):
    path = argv[1]
    dict = data.Data(path)

    samples_list = dict.create_samples()
    # distances_matrix = distances.create_distances_matrix(samples_list)


    # a = []
    # b = []
    # a.extend(samples_list[0:10])
    # b.extend(samples_list[10:20])
    # c1 = cluster.Cluster(7, b)
    # c2 = cluster.Cluster(18, a)
    # c1.merge(c2)
    #
    # print(c1.c_id)
    # print(c2.c_id)





if __name__ == '__main__':
    main(sys.argv)
