"""
Read the diabetes2.csv file using the csv library.
On the basis of this file a new file is to be created, which considers only the columns BMI, age and outcome.
Furthermore only entries are to be considered with outcome = 1

Write the data comma separated into a new file:
diabetes_positive_outcome.csv

In addition, we are interested in the following values, which are to be output at the end of the writing process:

For all entries with outcome=1
Mean value BMI
Mean age
Median BMI
Median age
Max BMI, Min BMI
MAX BloodPRESSURE

for median and mean use the statistics module
import statistics
median = statistics.median([2, 3, 4, 5])
mean = statistics.mean([2, 3, 4, 5])

for min/max use the builtin functions min([1, 2, 3])
and max([3, 2, 1])

"""

import csv
from pathlib import Path 

with open(Path(__file__).parent / 'diabetes2.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    
    with open(Path(__file__).parent / 'outcome.csv', 'w', newline = '') as outcome:
        writer = csv.writer(outcome, delimiter=',')
        header = next(reader)
        list_bmi = []
        list_age = []
        list_BP = []
        writer.writerow(["BMI", "Age", "Outcome"])
        for line in reader:
            if line[8] != '0':
                writer.writerow((line[5], line[7], line[8]))
                list_bmi.append(float(line[5]))
                list_age.append(float(line[7]))
                list_BP.append(float(line[2]))


               
import statistics
medianbmi = statistics.median(list_bmi)
meanbmi = statistics.mean(list_bmi)

medianage = statistics.median(list_age)
meanage = statistics.mean(list_age)

minbmi = min(list_bmi)
maxbmi = max(list_bmi)

maxBP = max(list_BP)


list = [['BMI_median', medianbmi],
             ['BMI_mean', meanbmi], 
             ['age_median', medianage],
             ['age_mean', meanage],
             ['BMI_min', minbmi],
             ['BMI_max', maxbmi],
             ['BP_max', maxBP] 
]

with open(Path(__file__).parent / 'outcome.csv', 'a', newline = '') as outcome:
    writer = csv.writer(outcome, delimiter=',')
    writer.writerows(list)