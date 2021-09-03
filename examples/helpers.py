# standard library
from typing import List

# data wrangling
import numpy as np
import pandas as pd

# visualisation
import matplotlib.pyplot as plt
import seaborn as sns

# data modelling
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score

def plot_confusion_matrix(y_true: np.ndarray, y_hat: np.ndarray, figsize = (16, 9)):
    """
    Convenience function to display a confusion matrix in a graph.
    """
    labels = sorted(list(set(y_true)))
    df_lambda = pd.DataFrame(
        confusion_matrix(y_true, y_hat),
        index = labels,
        columns = labels
    )
    acc = accuracy_score(y_true, y_hat)
    f1s = f1_score(y_true, y_hat, average = 'weighted')
    
    fig, ax = plt.subplots(figsize = figsize)
    sns.heatmap(
        df_lambda, annot = True, square = True, cbar = False, 
        fmt = 'd', linewidths = .5, cmap = 'YlGnBu',
        ax = ax
    )
    ax.set(
        title = f'Accuracy: {acc:.2f}, F1 (weighted): {f1s:.2f}',
        xlabel = 'Predicted',
        ylabel = 'Actual'
    )
    fig.suptitle('Confusion Matrix')
    plt.tight_layout()
    
def get_top_features(vectoriser, clf, top_n: int = 25, how: str = 'long'):
    """
    Convenience function to extract top_n predictor per class from a model.
    """
    
    assert hasattr(vectoriser, 'get_feature_names')
    assert hasattr(clf, 'coef_')
    assert how in {'long', 'wide'}, f'how must be either long or wide not {how}'
    
    features = np.array(vectoriser.get_feature_names())
    axis_names = [f'freature_{x + 1}' for x in range(top_n)]
    
    if len(clf.classes_) > 2:
        results = list()
        for c, coefs in zip(clf.classes_, clf.coef_):
            idx = coefs.argsort()[::-1][:top_n]
            results.extend(tuple(zip([c] * top_n, features[idx], coefs[idx])))
    else:
        coefs = clf.coef_.flatten()
        idx = coefs.argsort()[::-1][:top_n]
        results = tuple(zip([clf.classes_[1]] * top_n, features[idx], coefs[idx]))
            
    df_lambda = pd.DataFrame(results, columns =  ['sdg', 'feature', 'coef'])
    
    if how == 'wide':
        df_lambda = pd.DataFrame(
            np.array_split(df_lambda['feature'].values, len(df_lambda) / top_n),
            index = clf.classes_ if len(clf.classes_) > 2 else [clf.classes_[1]],
            columns = axis_names
        )
    
    return df_lambda