import string
import pandas as pd


def abc_analysis(x, bins):
    letters =[l for l in string.ascii_uppercase[:(len(bins) - 1)]]

    share = x / x.sum()
    share.sort_values(ascending=False, inplace=True)
    contribution = share.cumsum()
    labels = pd.cut(
        contribution,
        bins,
        labels=letters,
    )

    return contribution, labels
