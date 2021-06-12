import sys
import os
import data


# def load_data(argv):
#     """
#     Loads data from path in first argument
#     :return: returns data as dictionary
#     """
#     if len(argv) < 1:
#         print('Not enough arguments provided. Please provide the path to the input file')
#         exit(1)
#     input_path = argv[1]
#
#     if not os.path.exists(input_path):
#         print('Input file does not exist')
#         exit(1)
#
#     dict = data.Data(input_path)
#     return dict


def main(argv):
    path = argv[1]
    dict = data.Data(path)
    print(dict.data.keys())



if __name__ == '__main__':
    main(sys.argv)
