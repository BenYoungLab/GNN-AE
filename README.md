# GNN-AE

The GNN-AE approach consists of both offline and online phases (i.e., /offline and /online).  GNN-AE is a graph neural network (GNN)-based anchor embedding approach, which can return all exact matching locations for subgraph retrieval.

Since the data after offline training is large, we have prepared two examples (i.e., the yeast and syn-ws datasets) containing the necessary offline training results. This allows you to run the online process directly, without executing the offline process first.

## Running Offline Process

```
cd offline
python main.py
```

## Running Online Process
1. Download the /online, execute the following commands.

```
cd online
```

2. Under the root directory of the project, compile the source code.

```
mkdir build
cd build
cmake ..
make
```

3. Execute the following command to run the experiment over the Yeast dataset (the necessary pre-computed data produced by the offline process is already stored in the '/data' directory).

```
./gnnae yeast
```

## Configuration Items
The configuration items of the offline process are in main.py

| name | description | 
| ----- | --------- |
| gnn_model_name | Available GNN models (options: 'GIN' and 'GAT') |
| emb_dimension | Dimension of the anchored subgraph embedding output by the GNN model |
| emb_precision | Precision (per dimension) of anchored subgraph embeddings |
| dd_path_modes | Anchored path mode (options: '2' = hybrid mode; '3' = dual mode) |

The configuration items of the online process are in the main.cpp

| name | description | 
| ----- | --------- |
| emb_precision | Precision (per dimension) of anchored subgraph embeddings |
| parallel_threads | Number of parallel threads (default: 8) for the matching growth algorithm |
| path_index_type | Anchored path index mode (options: '2' = hybrid index mode; '3' = dual index mode) |

## Experiment Datasets
You can run 'utils/generator.py' to generate random queries, and download the [real](https://github.com/RapidsAtHKUST/SubgraphMatching) datasets (from an existing benchmark) and the [synthetic](https://1drv.ms/f/c/0098e169ff45042e/IgCUX8TRKsETSLOVkcSah1qqARmB29GWDwWg4esUY2eaKkQ) datasets.  

