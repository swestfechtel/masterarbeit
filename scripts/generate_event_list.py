import pandas as pd

from utils import convert_edge_list_to_rem_event_list


def yunnan():
    edge_list = '../Data/Preprocessed/yunnan_edgelist.csv'
    node_list = pd.read_csv('../Data/Preprocessed/yunnan_nodelist.csv')
    attribute_list = list(node_list.columns[:1])


if __name__ == '__main__':
    yunnan()


