import streamlit as st
import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import io

def main():
    st.set_page_config(page_title="MRT Network Analysis", layout="wide")
    st.title("Singapore MRT Transport Network")
    st.markdown("Visualisation and analysis of the transport network distance attributes.")

    unit_choice = st.radio("Choose distance attribute to visualise:", ('km', 'miles'))

    G = nx.Graph()

    stations = {
        # North South Line
        'Ang Mo Kio':    {'pos': ( 1.00, 11.50), 'type': 'normal'},
        'Bishan':        {'pos': ( 1.00,  8.05), 'type': 'interchange'},
        'Braddell':      {'pos': ( 1.00,  6.25), 'type': 'normal'},
        'Toa Payoh':     {'pos': ( 1.00,  4.90), 'type': 'normal'},
        'Novena':        {'pos': ( 1.00,  1.75), 'type': 'normal'},

        # North East Line
        'Hougang':       {'pos': ( 8.57, 11.07), 'type': 'normal'},
        'Kovan':         {'pos': ( 7.09,  9.59), 'type': 'normal'},
        'Serangoon':     {'pos': ( 5.50,  8.00), 'type': 'interchange'},
        'Woodleigh':     {'pos': ( 4.33,  6.83), 'type': 'normal'},
        'Potong Pasir':  {'pos': ( 3.38,  5.88), 'type': 'normal'},

        # Circle Line
        'Lorong Chuan':  {'pos': ( 3.55,  8.02), 'type': 'normal'},
        'Bartley':       {'pos': ( 7.30,  7.30), 'type': 'normal'},
        'Tai Seng':      {'pos': ( 8.80,  5.90), 'type': 'normal'},

        # Downtown Line
        'Kaki Bukit':    {'pos': (12.35,  5.28), 'type': 'normal'},
        'Ubi':           {'pos': (10.90,  4.90), 'type': 'normal'},
        'MacPherson':    {'pos': ( 9.30,  4.50), 'type': 'interchange'},
        'Mattar':        {'pos': ( 7.05,  4.50), 'type': 'normal'},
        'Geylang Bahru': {'pos': ( 5.55,  3.25), 'type': 'normal'},

        # East West Line
        'Kembangan':     {'pos': (12.80,  4.18), 'type': 'normal'},
        'Eunos':         {'pos': (11.30,  3.49), 'type': 'normal'},
        'Paya Lebar':    {'pos': ( 9.80,  2.80), 'type': 'interchange'},
        'Aljunied':      {'pos': ( 7.90,  1.92), 'type': 'normal'},
        'Kallang':       {'pos': ( 6.00,  1.04), 'type': 'normal'},
        'Dakota':        {'pos': ( 9.80,  0.85), 'type': 'normal'},
    }

    for node, attrs in stations.items():
        G.add_node(node, pos=attrs['pos'], type=attrs['type'])

    edges_data = [
        ('Ang Mo Kio',   'Bishan',        'North South Line', '#d42e12', 2.3),
        ('Bishan',       'Braddell',      'North South Line', '#d42e12', 1.2),
        ('Braddell',     'Toa Payoh',     'North South Line', '#d42e12', 0.9),
        ('Toa Payoh',    'Novena',        'North South Line', '#d42e12', 2.1),

        ('Hougang',      'Kovan',         'North East Line',  '#9016b2', 1.4),
        ('Kovan',        'Serangoon',     'North East Line',  '#9016b2', 1.5),
        ('Serangoon',    'Woodleigh',     'North East Line',  '#9016b2', 1.1),
        ('Woodleigh',    'Potong Pasir',  'North East Line',  '#9016b2', 0.9),

        ('Bishan',       'Lorong Chuan',  'Circle Line',      '#fd9a00', 1.7),
        ('Lorong Chuan', 'Serangoon',     'Circle Line',      '#fd9a00', 1.3),
        ('Serangoon',    'Bartley',       'Circle Line',      '#fd9a00', 1.3),
        ('Bartley',      'Tai Seng',      'Circle Line',      '#fd9a00', 1.4),
        ('Tai Seng',     'MacPherson',    'Circle Line',      '#fd9a00', 1.0),
        ('MacPherson',   'Paya Lebar',    'Circle Line',      '#fd9a00', 1.2),
        ('Paya Lebar',   'Dakota',        'Circle Line',      '#fd9a00', 1.3),

        ('Kaki Bukit',   'Ubi',           'Downtown Line',    '#005b9f', 1.0),
        ('Ubi',          'MacPherson',    'Downtown Line',    '#005b9f', 1.1),
        ('MacPherson',   'Mattar',        'Downtown Line',    '#005b9f', 1.5),
        ('Mattar',       'Geylang Bahru', 'Downtown Line',    '#005b9f', 1.3),

        ('Kembangan',    'Eunos',         'East West Line',   '#009645', 1.1),
        ('Eunos',        'Paya Lebar',    'East West Line',   '#009645', 1.1),
        ('Paya Lebar',   'Aljunied',      'East West Line',   '#009645', 1.4),
        ('Aljunied',     'Kallang',       'East West Line',   '#009645', 1.4),
    ]

    for u, v, line_name, color, km in edges_data:
        miles = round(km / 1.60934, 2)
        G.add_edge(u, v, line=line_name, color=color, km=km, miles=miles)

    pos = nx.get_node_attributes(G, 'pos')

    fig, ax = plt.subplots(figsize=(16, 12))
    plt.axis('off')

    edge_colors = [G[u][v]['color'] for u, v in G.edges()]
    nx.draw_networkx_edges(G, pos, width=5, edge_color=edge_colors, ax=ax)

    node_colors = []
    for node in G.nodes():
        if G.nodes[node]['type'] == 'interchange':
            node_colors.append('#e0e0e0')
        else:
            connected_edges = list(G.edges(node, data=True))
            node_colors.append(connected_edges[0][2]['color'] if connected_edges else '#000000')

    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=350,
                           edgecolors='white', linewidths=2.5, ax=ax)

    label_pos = {}
    for k, v in pos.items():
        x_off, y_off = 0.2, 0.2

        if k in ['Ang Mo Kio', 'Bishan', 'Braddell', 'Toa Payoh', 'Novena']:
            x_off, y_off = -0.6, 0.0

        elif k in ['Serangoon']:
            x_off, y_off = 0.7, 0.1

        elif k in ['Hougang', 'Kovan']:
            x_off, y_off = 0.5, 0.0

        elif k in ['Woodleigh', 'Potong Pasir']:
            x_off, y_off = -0.8, 0.0

        elif k == 'Lorong Chuan':
            x_off, y_off = -0.15, 0.38
        elif k == 'Bartley':
            x_off, y_off = 0.0, 0.35
        elif k == 'Tai Seng':
            x_off, y_off = 0.0, 0.35

        elif k == 'Kaki Bukit':
            x_off, y_off = -0.4, 0.3
        elif k == 'Ubi':
            x_off, y_off = -0.3, 0.2
        elif k == 'MacPherson':
            x_off, y_off = -0.6, 0.3
        elif k == 'Mattar':
            x_off, y_off = -0.3, 0.2
        elif k == 'Geylang Bahru':
            x_off, y_off = -0.55, 0.3
        elif k == 'Paya Lebar':
            x_off, y_off = 0.6, -0.2
        elif k == 'Dakota':
            x_off, y_off = 0.25, -0.35

        elif k in ['Kembangan', 'Eunos', 'Aljunied', 'Kallang']:
            x_off, y_off = 0.15, -0.42

        label_pos[k] = (v[0] + x_off, v[1] + y_off)

    nx.draw_networkx_labels(G, label_pos, font_size=10, font_weight='bold',
                            font_family='sans-serif', ax=ax)

    edge_labels = {}
    for u, v in G.edges():
        distance_value = G[u][v][unit_choice]
        edge_labels[(u, v)] = f"{distance_value} {unit_choice}"

    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=11,
                                 bbox=dict(facecolor='white', edgecolor='none',
                                           alpha=0.9, boxstyle='round,pad=0.2'), ax=ax)

    legend_elements = [
        plt.Line2D([0], [0], color='#d42e12', lw=2, label='North South Line'),
        plt.Line2D([0], [0], color='#9016b2', lw=2, label='North East Line'),
        plt.Line2D([0], [0], color='#fd9a00', lw=2, label='Circle Line'),
        plt.Line2D([0], [0], color='#005b9f', lw=2, label='Downtown Line'),
        plt.Line2D([0], [0], color='#009645', lw=2, label='East West Line'),
        plt.Line2D([0], [0], color='none',    label=''),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#e0e0e0',
                   markersize=12, markeredgecolor='white', markeredgewidth=2,
                   label='Interchange Station'),
    ]

    ax.legend(handles=legend_elements, loc='lower right', title='Key',
              title_fontsize='12', frameon=True, prop={'size': 10},
              handlelength=2)

    plt.tight_layout()
    st.pyplot(fig)

    # Download button
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=150, bbox_inches='tight')
    buf.seek(0)
    st.download_button(
        label="Download map as PNG",
        data=buf,
        file_name=f"mrt_network_{unit_choice}.png",
        mime="image/png",
    )

    # Task 2: Extracted Data
    total_km    = sum(nx.get_edge_attributes(G, 'km').values())
    total_miles = sum(nx.get_edge_attributes(G, 'miles').values())
    avg_km      = total_km    / G.number_of_edges()
    avg_miles   = total_miles / G.number_of_edges()

    st.markdown("---")
    st.subheader("Task 2: Extracted Data")

    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Total Length (km)",    value=f"{total_km:.2f}")
        st.metric(label="Total Length (miles)", value=f"{total_miles:.2f}")
    with col2:
        st.metric(label="Average Distance (km)",    value=f"{avg_km:.2f}")
        st.metric(label="Average Distance (miles)", value=f"{avg_miles:.2f}")


if __name__ == '__main__':
    main()