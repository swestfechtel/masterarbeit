import networkx as nx
import pandas as pd
import numpy as np


class BasicAnalysisFramework:
    def __init__(self):
        self._network = nx.Graph()
        self._degree_centrality = None
        self._betweenness_centrality = None
        self._pagerank_centrality = None
        self._connected_components = None
        self._triadic_census = None

    def load_edgelist(self, filename: str):
        df = pd.read_csv(filename)
        df['Referee'] = df['Referee'].astype('Int64', errors='ignore')
        df['Referral'] = df['Referral'].astype('Int64', errors='ignore')
        rows_with_contact = df[~df['Referral'].isnull()]
        rows_without_contact = df[df['Referral'].isnull()]
        try:
            assert df.shape[0] == (rows_with_contact.shape[0] + rows_without_contact.shape[0]) # sanity check
        except AssertionError:
            print(rows_with_contact.shape, rows_without_contact.shape)

        edge_list = list(np.empty(rows_with_contact.shape[0]))
        i = 0
        for index, row in rows_with_contact.iterrows():
            edge_list[i] = (row['Referee'], row['Referral'])
            i += 1

        self._network.add_edges_from(edge_list)
        self._network.add_nodes_from(rows_without_contact['Referee'])

    @property
    def degree_centrality(self):
        return self._degree_centrality

    @property
    def betweenness_centrality(self):
        return self._betweenness_centrality

    @property
    def pagerank_centrality(self):
        return self._pagerank_centrality

    @property
    def connected_components(self):
        return self._connected_components

    @property
    def triadic_census(self):
        return self._triadic_census

    def compute_measurements(self):
        self._degree_centrality = nx.degree_centrality(self._network)
        self._betweenness_centrality = nx.betweenness_centrality(self._network)
        self._pagerank_centrality = nx.pagerank(self._network)
        self._connected_components = nx.connected_components(self._network)

        di_network = nx.to_directed(self._network)
        self._triadic_census = nx.triadic_census(di_network)

    def create_report(self):
        df = pd.DataFrame(columns=['Referee', 'Degree_Centrality', 'Betweenness_Centrality', 'Pagerank_Centrality', 'Component_Size'])
        for node in self._network.nodes:
            df = df.append({'Referee': node, 'Degree_Centrality': self._degree_centrality[node], 'Betweenness_Centrality': self._betweenness_centrality[node], 'Pagerank_Centrality': self._pagerank_centrality[node], 
                            'Component_Size': len(nx.node_connected_component(self._network, node))}, ignore_index=True)
        
        df['Referee'] = df['Referee'].astype('Int64', errors='ignore')
        df = df.sort_values(by='Referee', ascending=True)
        df = df.reset_index()
        df.drop(columns=['index'], inplace=True)
        return df