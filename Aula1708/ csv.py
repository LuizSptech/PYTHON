import csv
import time

time.sleep(3)
with open('./teste.csv','w') as csvfile:
    csv.writer(csvfile).writerow(['João', '30'])
    csv.writer(csvfile).writerow(['José','27'])