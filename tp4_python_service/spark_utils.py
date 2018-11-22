from pyspark.mllib.fpm import FPGrowth
from pyspark import SparkContext

sc = SparkContext(appName="FPGrowth")

def getFrequentData(source):
    data = sc.textFile(source)
    data.collect()
    transactions = data.map(lambda line: line.strip().split(' '))
    model = FPGrowth.train(transactions, minSupport=0.2, numPartitions=10)
    result = model.freqItemsets().collect()
    out = []
    for r in result:
        out.append({"items": r.items, "freq": r.freq})
    return out