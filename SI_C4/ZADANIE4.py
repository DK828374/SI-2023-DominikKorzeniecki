# https://drive.google.com/file/d/18NFdJqUeSTdWe1RpHN9xa_zxO-A9SJ2L/view
import pandas as pd


def reduct(ds):
    n, m = ds.shape
    attributes = set(range(m - 1))
    zm = set()
    while attributes:
        min_moc = float('inf')
        min_element = None
        for attr in attributes:
            moc = sum(ds.iloc[:, attr].duplicated(keep=False))
            if moc < min_moc:
                min_moc = moc
                min_element = attr
        zm.add(min_element)
        attributes.remove(min_element)
    return zm


def reduct2(ds):
    n, m = ds.shape
    attributes = set(range(m - 1))
    z = set()
    while attributes:
        min_moc = float('inf')
        min_element = None
        for attr in attributes:
            moc = sum(ds.iloc[:, attr].duplicated(keep=False))
            if moc < min_moc:
                min_moc = moc
                min_element = attr
        z.add(min_element)
        attributes.remove(min_element)
    return z


fig1 = pd.DataFrame({
    'b': [2, 2, 0, 1],
    'c': [1, 2, 2, 1],
    'd': [0, 1, 1, 1],
    'dec': [0, 1, 2, 1]
})

fig2 = pd.DataFrame({
    'a1': ['wysoka', 'wysoka', 'wysoka', 'więcej niż średnia', 'więcej niż średnia', 'więcej niż średnia', 'wysoka',
           'więcej niż średnia', 'więcej niż średnia'],
    'a2': ['bliski', 'bliski', 'bliski', 'daleki', 'daleki', 'daleki', 'bliski', 'daleki', 'daleki'],
    'a3': ['średni', 'średni', 'średni', 'silny', 'silny', 'lekki', 'średni', 'lekki', 'lekki'],
    'dec': ['tak', 'tak', 'tak', 'nie pewne', 'nie', 'nie', 'tak', 'nie', 'tak']
})

reduct = reduct(fig1)
print("Zadanie 1.4: Redukt decyzyjny dla Fig1:\n", reduct)

reduct2 = reduct2(fig2)
print("Zadanie 1.4: Redukt decyzyjny dla Fig2:\n", reduct2)
