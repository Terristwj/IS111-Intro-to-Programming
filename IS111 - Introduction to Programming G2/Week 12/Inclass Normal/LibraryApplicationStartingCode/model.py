import util
import json
import plotly
import config as cfg

def get_sorted_items(item_list, sort_param_index):
    return sorted(item_list, key=lambda row:row[sort_param_index])
    
def generate_graphs(item_file_name, loan_file_name):
    
    (graph_1_x, graph_1_y) = zip(*util.get_item_counts_by_library(item_file_name))
    (graph_2_x, graph_2_y) = zip(*util.get_item_counts_by_format(item_file_name))
    (graph_3_x, graph_3_y) = zip(*util.get_item_counts_by_language(item_file_name))
    
    graphs = [
        dict(
            data=[dict(
                    x=graph_1_x,
                    y=graph_1_y,
                    type='bar')],
            layout=dict(title="Distribution of Items across Libraries", plot_bgcolor="lightblue")
        ),
        dict(
            data=[dict(
                    labels=graph_2_x,
                    values=graph_2_y,
                    type='pie')],
            layout=dict(title="Distribution of Items of Different Formats", plot_bgcolor="lightblue")
        ),
        dict(
            data=[dict(
                    labels=graph_3_x,
                    values=graph_3_y,
                    type='pie')],
            layout=dict(title="Distribution of Items of Different Languages", plot_bgcolor="lightblue")
        )
    ]
    
    ids = ['Chart-{}'.format(i+1) for i in range(len(graphs))]
    
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    
    return (ids, graphJSON)