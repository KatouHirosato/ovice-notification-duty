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

def normalize_per_people():
    df = pandas.read_csv(CSV_THISWEEK)
    df['calculation'] = df['monday'] + df['tuesday'] + df['wednesday'] + df['thursday'] + df['friday']
    df.iloc[:, 2:] = df.iloc[:, 2:].mul(df['sum'] / df['calculation'], axis=0)
    df.drop('calculation', axis=1, inplace=True)
    df.to_csv(CSV_THISWEEK, index=False)

def todays_weights(day):
    df = pandas.read_csv(CSV_THISWEEK)
    weights = df.set_index('people').iloc[:, day + 1].to_dict()
    return weights

def select(sample):
    total_weight = sum(sample.values())
    weights = [value / total_weight for value in sample.values()]
    people = list(sample.keys())
    persons = numpy.random.choice(people, size=3, replace=False, p=weights)
    return persons
