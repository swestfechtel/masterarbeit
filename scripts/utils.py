import warnings

import pandas as pd

from tqdm import tqdm

warnings.filterwarnings('ignore')


def convert_edge_list_to_rem_event_list(edge_list: str, node_list: pd.DataFrame, attribute_list: list) -> pd.DataFrame:
    """
    Convert a conventional edge list to a REM-compatible event list.

    Accepts an edge list of the general format (time, source, target, source attributes, target attributes) and converts it into a
    list of events of the general format (event_id, time, source, target, event_type, event_weight). Source and target attributes
    are translated into dummy events, where event_type specifies the corresponding attribute.

    For example, a record

    ``2000-01-01, A, B, male, female``

    produces the following three events:

    ``0, 1970-01-01, A, A, is_male, 1``

    ``0, 1970-01-01, B, B, is_male, 0``

    ``1, 2000-01-01, A, B, interaction, 1``

    :param edge_list: A string specifying the location of the edge list file
    :param node_list: A DataFrame representation of the node list
    :param attribute_list: A list containing the names of the node attributes to add to the event list

    :return: event_list
    """
    edge_list = pd.read_csv(edge_list)
    # node_list = pd.read_csv(node_list)

    edge_list = edge_list[~edge_list['Referral'].isna()]  # exclude non-edges, not relevant for R(H)EM

    event_list = pd.DataFrame(columns=['event_id', 'referee', 'referral', 'date', 'type', 'weight'])
    print(attribute_list)

    for index, row in tqdm(node_list.iterrows()):
        event_list_temp = pd.DataFrame({'event_id': [0], 'referee': [row['node_id']], 'referral': [row['node_id']], 'date': [pd.to_datetime('2000-01-01').strftime('%y%m%d')], 'type': ['add_actor'], 'weight': [1]})
        # event_list = event_list.append(pd.Series({'event_id': 0, 'referee': row['node_id'], 'referral': row['node_id'], 'date': pd.to_datetime('2000-01-01').strftime('%y%m%d'), 'type': 'add_actor', 'weight': 1}), ignore_index=True)  # add nodes for risk set
        for attribute in attribute_list:
            # categorical attributes have to be converted to numerical representations
            # event_list = event_list.append(pd.Series({'event_id': 0, 'referee': row['node_id'], 'referral': row['node_id'], 'date': pd.to_datetime('2000-01-01').strftime('%y%m%d'), 'type': attribute, 'weight': row[attribute]}), ignore_index=True)
            event_list_temp = event_list_temp.append(pd.Series({'event_id': 0, 'referee': row['node_id'], 'referral': row['node_id'], 'date': pd.to_datetime('2000-01-01').strftime('%y%m%d'), 'type': attribute, 'weight': row[attribute]}), ignore_index=True)

        event_list = pd.concat([event_list, event_list_temp])

    i = 0
    events = dict()

    for index, row in tqdm(edge_list.iterrows()):
        # Need to infer event id:
        # Idea: all edges from source x on date d have the same event id
        if (event := f'{str(row["Referee"])}_{str(int(row["Date"]))}') in events.keys():
            event = events[event]
        else:
            events[event] = i
            event = i
            i += 1

        event_list = event_list.append(pd.Series({'event_id': event, 'referee': row['Referee'], 'referral': row['Referral'], 'date': int(row['Date']), 'type': 'contact_nomination', 'weight': 1}), ignore_index=True)

    event_list['date'] = event_list['date'].astype('str')
    return event_list
