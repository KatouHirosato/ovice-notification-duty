import pandas
import numpy
import shutil

CSV_THISWEEK = './thisweek.csv'
CSV_NEXTWEEK = './nextweek.csv'

def reset():
    shutil.copyfile(CSV_NEXTWEEK, CSV_THISWEEK)
    df = pandas.read_csv(CSV_NEXTWEEK)
    df.iloc[:, 2:] = 1
    df.to_csv(CSV_THISWEEK, index=False)

def normalize_per_person():
    df = pandas.read_csv(CSV_THISWEEK)
    df['calculation'] = df['monday'] + df['tuesday'] + df['wednesday'] + df['thursday'] + df['friday']
    df.loc[df['calculation'] == 0, ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']] = 1
    df.iloc[:, 2:] = df.iloc[:, 2:].mul(df['sum'] / df['calculation'], axis=0)
    df.drop('calculation', axis=1, inplace=True)
    df.to_csv(CSV_THISWEEK, index=False)

def todays_weights(day):
    df = pandas.read_csv(CSV_THISWEEK)
    weights = df.set_index('person').iloc[:, day + 1].to_dict()
    return weights

def select(sample):
    total_weight = sum(sample.values())
    weights = [value / total_weight for value in sample.values()]
    person = list(sample.keys())
    persons = numpy.random.choice(person, size=3, replace=False, p=weights)
    return persons
