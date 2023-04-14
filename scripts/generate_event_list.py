import pandas as pd
import numpy as np

from scripts.utils import convert_edge_list_to_rem_event_list
from sklearn.preprocessing import LabelEncoder
from collections import Counter


def yunnan():
    edge_list = '../Data/Preprocessed/yunnan_edgelist.csv'
    node_list = pd.read_csv('../Data/Preprocessed/yunnan_nodelist.csv')
    node_list.drop(columns='Unnamed: 0', inplace=True)
    attribute_list = list(node_list.columns[1:])
    # node_list = '../Data/Preprocessed/yunnan_nodelist.csv'
    return convert_edge_list_to_rem_event_list(edge_list=edge_list, node_list=node_list, attribute_list=attribute_list)


def hainan():
    edge_list = '../Data/Preprocessed/hainan_edgelist.csv'
    node_list = pd.read_csv('../Data/Preprocessed/hainan_nodelist.csv')
    node_list.drop(columns='Unnamed: 0', inplace=True)
    attribute_list = list(node_list.columns[1:])
    # node_list = '../Data/Preprocessed/hainan_nodelist.csv'
    return convert_edge_list_to_rem_event_list(edge_list=edge_list, node_list=node_list, attribute_list=attribute_list)


def shanxi():
    edge_list = '../Data/Preprocessed/shanxi_edgelist.csv'
    node_list = pd.read_csv('../Data/Preprocessed/shanxi_nodelist.csv')
    node_list.drop(columns='Unnamed: 0', inplace=True)
    node_list['hukou'] = LabelEncoder().fit_transform(node_list['hukou'])
    attribute_list = list(node_list.columns[1:])
    # node_list = '../Data/Preprocessed/shanxi_nodelist.csv'
    return convert_edge_list_to_rem_event_list(edge_list=edge_list, node_list=node_list, attribute_list=attribute_list)


def china():
    edge_list = '../Data/Preprocessed/china_edgelist.csv'
    node_list = pd.read_csv('../Data/Preprocessed/china_nodelist.csv')

    node_list['gender'] = node_list['gender'].apply(lambda x: str(x).lower())
    node_list['gender'] = node_list['gender'].apply(lambda x: x.strip())
    node_list['gender'] = node_list['gender'].apply(lambda x: 'male' if x in ('male', 'man') else x)
    node_list['gender'] = node_list['gender'].apply(lambda x: np.nan if x not in ('male', 'female') else x)
    node_list['gender'] = LabelEncoder().fit_transform(node_list['gender'])

    node_list['residency'] = node_list['residency'].apply(lambda x: str(x).lower())
    node_list['residency'] = node_list['residency'].apply(lambda x: x.strip())
    node_list['residency'] = LabelEncoder().fit_transform(node_list['residency'])

    node_list['place_event'] = node_list['place_event'].apply(lambda x: str(x).lower())
    node_list['place_event'] = node_list['place_event'].apply(lambda x: x.strip())
    node_list['place_event'] = LabelEncoder().fit_transform(node_list['place_event'])

    node_list['symptom'] = node_list['symptom'].apply(lambda x: str(x).lower())
    node_list['symptom'] = node_list['symptom'].apply(lambda x: x.strip())
    most_common_symptoms = Counter(node_list['symptom']).most_common()
    symptom_keys = set([x[0] for x in most_common_symptoms])
    node_list['symptom'] = node_list['symptom'].apply(lambda x: x if x in symptom_keys else np.nan)
    node_list['symptom'] = LabelEncoder().fit_transform(node_list['symptom'])

    node_list['place_admission'] = node_list['place_admission'].apply(lambda x: str(x).lower())
    node_list['place_admission'] = node_list['place_admission'].apply(lambda x: x.strip())
    node_list['place_admission'] = LabelEncoder().fit_transform(node_list['place_admission'])

    node_list['symptom_severity'] = node_list['symptom_severity'].apply(lambda x: str(x).lower())
    node_list['symptom_severity'] = node_list['symptom_severity'].apply(lambda x: x.strip())
    node_list['symptom_severity'] = node_list['symptom_severity'].apply(lambda x: x if x in ('stable', 'mild', 'light', 'severe') else np.nan)
    node_list['symptom_severity'] = LabelEncoder().fit_transform(node_list['symptom_severity'])

    attribute_list = ['age', 'gender', 'residency', 'place_event', 'symptom', 'symptom_severity', 'place_admission']  # exclude possible source
    return convert_edge_list_to_rem_event_list(edge_list=edge_list, node_list=node_list, attribute_list=attribute_list)


def bucharest():
    edge_list = '../Data/Preprocessed/bucharest_edgelist.csv'
    node_list = pd.read_csv('../Data/Preprocessed/bucharest_nodelist.csv')

    node_list['gender'] = node_list['gender'].apply(lambda x: str(int(1)) if x in ('1', 'male', '1.0') else x)
    node_list['gender'] = node_list['gender'].apply(lambda x: str(int(2)) if x in ('2', 'female', '2.0') else x)

    node_list['medical'] = LabelEncoder().fit_transform(node_list['medical'])
    node_list['isco08_label'] = LabelEncoder().fit_transform(node_list['isco08_label'])

    attribute_list = ['age', 'gender', 'medical', 'isco08_label']
    return convert_edge_list_to_rem_event_list(edge_list=edge_list, node_list=node_list, attribute_list=attribute_list)


if __name__ == '__main__':
    yunnan()
