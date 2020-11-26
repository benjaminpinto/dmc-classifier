from src.mycsv import parse_to_array
from src.task import random_select_sample, extract_sample
from src.classifier import DMC


dataset = parse_to_array('iris.data')
sample = random_select_sample(dataset, 30)
classifier = DMC()

extract_sample(sample, dataset)

classifier.run(sample, dataset)