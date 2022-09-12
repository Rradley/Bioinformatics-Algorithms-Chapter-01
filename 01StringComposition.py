#!/usr/bin/env python3
"""
Created on Tue Aug 30 16:59:09 2022

@author: radleyrp
"""
file = "../datasets/dataset_746262_3.txt"

def read_file(file_name):
    with open(file_name, "r") as file:
        k = int(file.readline())
        string = file.readline()
        file.close()
    return k,string


def composition(k, text):
    result = []
    for i in range(len(text) - k + 1): #+1 if using any debugging datasets, +0 if using downloaded file
        result.append(text[i:i+k])
    return result


k, text = read_file(file)

k=5
text='CAATCCAAC'

output = (', '.join(composition(k, text)))
output = output.replace(',', '')
print(output)

#f = open("answer.txt", "w")
#f.write(output)
#f.close()
