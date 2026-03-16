"""
@file abbreviations.py
@description Known mathematical abbreviation expansions for concept normalization.
"""

# Maps lowercase abbreviation -> full lowercase expansion.
# Used during concept name normalization to improve fuzzy matching accuracy.
MATH_ABBREVIATIONS: dict[str, str] = {
    "mdp": "markov decision process",
    "pomdp": "partially observable markov decision process",
    "rl": "reinforcement learning",
    "ucb": "upper confidence bound",
    "kl": "kullback leibler",
    "erm": "empirical risk minimization",
    "sgd": "stochastic gradient descent",
    "gd": "gradient descent",
    "nn": "neural network",
    "rnn": "recurrent neural network",
    "cnn": "convolutional neural network",
    "gnn": "graph neural network",
    "vae": "variational autoencoder",
    "gan": "generative adversarial network",
    "mle": "maximum likelihood estimation",
    "map": "maximum a posteriori",
    "iid": "independent and identically distributed",
    "pde": "partial differential equation",
    "ode": "ordinary differential equation",
    "svd": "singular value decomposition",
    "pca": "principal component analysis",
}
