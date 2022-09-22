# Supervised community detection
This work is an addition to the paper "Supervised community detection in multiplex networks based on
layers convex flattening and modularity optimizatio" by Gurov et al.

## Abstract
The problem of community detection in multiplex networks (the networks with multiple layers and the same set of nodes in each layer) is fundamental 
in the field of network analysis and can be solved by a variety of methods. Usually the methods are unsupervised and detect communities by optimization of a 
chosen objective function (e.g. multiplex modularity). 

There are also semi-supervised approaches that use known metadata about communities (in the form of ground truth) on a part of the network considered to detect 
communities on the other part of network. Nevertheless, as far as we know, the field however has the lack of supervised methods that, for example, 
train a model on one multiplex network using all known ground truth metadata about communities therein and then apply it to another network to detect 
communities there (under the assumption that both networks are similar, in a sense). 

In this paper, we propose a supervised method that is based on the so-called layers convex flattening of multiplex networks 
(when multiple layers are aggregated to a single layer network for further processing) and modularity optimization of the flattened network.
Our experiments with synthetic and real-world networks show the efficiency of the supervised method, particularly, by means of promising 
Normalized Mutual Information values (from 0.37 up to 0.79 on average) observed on several real-world networks for the community detection 
models trained on another network.

## Data
We use two types of datasets in the study:
 - Four real-world multiplex biological networks [[1]](#1)
 - Synthetic multiplex generated with mLFR Benchmark [[2]](#2)

Real-world multiplex biological networks can be found in ```./Data/``` folder.

All of the synthetic data can be generated in our code using the specified mLFR app.
This app is located in:
```
./mLFR/
```
Instructions for using it can be found <a href='https://github.com/pbrodka/mLFR-benchmark'>here</a>.

For convenience, all these necessary networks are pre-generated and stored in the folder:
```
./LFR_nets/
```
## Experiments
To start the experiments, you need to download this repository to yourself and execute all the Jupyter notebooks.
In total, there are ```./notebooks``` two notebooks with experiments: 
 - ```./notebooks/BioGRID.ipynb```. Contains the experiments with real-world multiplex biological networks
 - ```./notebooks/mLFR_experiments.ipynb```. Contains the experiments with synthetic networks

After launching the corresponding Jupyter notebooks, the results will be displayed both in the notebooks themselves and will fall into the ```./Results/``` 

## References
<a id="1">[1]</a> 
Stark, C., Breitkreutz, B. J., Reguly, T., Boucher, L., Breitkreutz, A., & Tyers, M. (2006). BioGRID: a general repository for interaction datasets. Nucleic acids research, 34(Database issue), D535–D539. https://doi.org/10.1093/nar/gkj109
<a id="2">[2]</a>
Bródka, P. (2016). A method for group extraction and analysis in multilayer social networks. arXiv preprint arXiv:1612.02377.
