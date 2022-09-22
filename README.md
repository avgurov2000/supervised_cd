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
