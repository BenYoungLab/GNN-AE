# GNN-AE

The GNN-AE approach consists of both offline and online phases (i.e., offline.tar.gz and online.tar.gz).  GNN-AE is a graph neural network (GNN)-based anchor embedding approach that allows exact subgraph matching.

Note that for generality, we set the code to find all subgraph matches instead of terminating when $10^5$ matches are discovered. As the data after offline training are large, we have prepared two examples (i.e., the Yeast dataset and the Syn-WS dataset) of necessary data after offline training. You can run online processing directly without running offline operations first.

## Running Offline Process
Download the offline.tar.gz, and execute the following commands.

```
tar -xzvf offline.tar.gz
cd offline
python main.py
```

## Running Online Process
1. Download the online.tar.gz, and execute the following commands.

```
tar -xzvf online.tar.gz
cd online
```

2. Under the root directory of the project, compile the source code.

```
mkdir build
cd build
cmake ..
make
```

3. Execute the following command to run the experiment over the Yeast dataset (or the Syn-WS dataset) (the necessary pre-computed data produced by the offline process is already stored in the data directory).

```
./gnnae yeast (or ./gnnae ws )
```

## Key Parameters
The key parameters of the offline process are in main.py

| name | description | 
| ----- | --------- |
| gnn_model_name | optional GNN models, including 'GIN', and 'GAT' |
| emb_dimension | the dimension of the anchor graph embedding |
| emb_precision | precision for each dimension in anchor graph embedding, default 100 |
| dd_path_modes | anchor path mode, '2' indicates hybrid positive \& negative 1-hop anchor paths, and '3' indicates dual 1-hop anchor path |

The key parameters of the online process are in main.cpp

| name | description | 
| ----- | --------- |
| emb_precision | precision for each dimension in anchor embedding, default 100 |
| parallel_threads | the number of parallel threads, default 8 |
| path_index_type | index of anchor path mode, '2' indicates hybrid positive \& negative 1-hop anchor paths index, and '3' indicates dual 1-hop anchor path index |

## Experiment Datasets
You can run 'utils/generator.py' to get the randomly generated queries, and download the [real](https://github.com/RapidsAtHKUST/SubgraphMatching) datasets and the [synthetic](https://1drv.ms/f/s!An78MY7AdBT2a88v8kIpv7zCn2A?e=HafVfc) datasets.  

