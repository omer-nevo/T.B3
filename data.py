import pandas


class Data:

    def __init__(self, path):
        self.path = path
        df = pandas.read_csv(path)  # import the path to df
        self.data = df.to_dict(orient="list")  # converting the cvs to dictionary
        print("good luck!!fsdfs!")