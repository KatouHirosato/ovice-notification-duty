import pandas
import numpy
import shutil

def normalize_per_person(csvfile):
    df = pandas.read_csv(csvfile)
    df['calculation'] = df['monday'] + df['tuesday'] + df['wednesday'] + df['thursday'] + df['friday']
    df.loc[df['calculation'] == 0, ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']] = 1
    df.iloc[:, 2:] = df.iloc[:, 2:].mul(df['sum'] / df['calculation'], axis=0)
    df.drop('calculation', axis=1, inplace=True)
    df.to_csv(csvfile, index=False)

def select(day,csvfile):
    df = pandas.read_csv(csvfile)
    distribution = df.set_index('person').iloc[:, day + 1].to_dict()
    total_weight = sum(distribution.values())
    weights = [value / total_weight for value in weights.values()]
    person = list(distribution.keys())
    persons = numpy.random.choice(person, size=3, replace=False, p=weights)
    return persons