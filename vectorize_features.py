# -*- coding: utf-8 -*-
#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction import DictVectorizer
import sys
from collections import defaultdict
from sklearn.decomposition import PCA


datasets_file = "sma++_data.txt"
morph_dataset_dict = []
morph_dataset_strings = open(datasets_file)

for datapoint in morph_dataset_strings:
    datapoint = datapoint.split(',')
    datapoint_dict = defaultdict()

    datapoint_dict['current_token'] = datapoint[0]
    datapoint_dict['POS'] = datapoint[1]
    datapoint_dict['suffix_1'] = datapoint[2]
    datapoint_dict['suffix_2'] = datapoint[3]
    datapoint_dict['suffix_3'] = datapoint[4]
    datapoint_dict['suffix_4'] = datapoint[5]
    datapoint_dict['suffix_5'] = datapoint[6]
    datapoint_dict['suffix_6'] = datapoint[7]
    datapoint_dict['suffix_7'] = datapoint[8]
    datapoint_dict['G_prev1'] = datapoint[9]
    datapoint_dict['G_prev2'] = datapoint[10]
    datapoint_dict['G_prev3'] = datapoint[11]
    datapoint_dict['N_prev1'] = datapoint[12]
    datapoint_dict['N_prev2'] = datapoint[13]
    datapoint_dict['N_prev3'] = datapoint[14]
    datapoint_dict['P_prev1'] = datapoint[15]
    datapoint_dict['P_prev2'] = datapoint[16]
    datapoint_dict['P_prev3'] = datapoint[17]
    datapoint_dict['C_prev1'] = datapoint[18]
    datapoint_dict['C_prev2'] = datapoint[19]
    datapoint_dict['C_prev3'] = datapoint[20]
    datapoint_dict['G_next1'] = datapoint[21]
    datapoint_dict['N_next1'] = datapoint[22]
    datapoint_dict['P_next1'] = datapoint[23]
    datapoint_dict['C_next1'] = datapoint[24]
    datapoint_dict['token_prev'] = datapoint[25]
    datapoint_dict['token_next'] = datapoint[26]
    datapoint_dict['len_curr_tok'] = datapoint[27]
    datapoint_dict['chartype_curr_tok'] = datapoint[28]

    morph_dataset_dict.append(datapoint_dict)

#print morph_dataset_dict
vec = DictVectorizer()
morph_dataset =  vec.fit_transform(morph_dataset_dict).toarray()
morph_dataset2 = vec.fit(morph_dataset_dict)
edible = []
poisonous = []
print vec.get_feature_names()

'''
for i in xrange(morph_dataset.shape[0]):
    if morph_dataset[i,22] == 1:
        edible.append(morph_dataset[i])
    elif morph_dataset[i,23] == 1:
        poisonous.append(morph_dataset[i])

edible_dataset = np.array(edible)
poisonous_dataset = np.array(poisonous)

if "a" in sys.argv:
    np.set_printoptions(threshold=np.nan)
    print morph_dataset

if "b" in sys.argv:
    pca = PCA(n_components=2)
    morph_pca = pca.fit_transform(morph_dataset)
    print morph_pca.shape
    print morph_pca
    edible = []
    poisonous = []
    for i in xrange(morph_pca.shape[0]):
        if morph_dataset[i,22] == 1:
            edible.append(morph_pca[i])
        elif morph_dataset[i,23] == 1:
            poisonous.append(morph_pca[i])
        else:
            print "ERROR", morph_dataset[i]


    plt.plot(edible, 'go', label="edible")
    plt.plot(poisonous, 'ro', label="poisionous")
    plt.ylabel("Y axis")
    plt.xlabel("X axis")
    plt.show()

if "c" in sys.argv:
    print "="*50
    num_samples = morph_dataset.shape[0]
    num_features = morph_dataset.shape[1]

    fisher = np.zeros(num_features, dtype=float)
    c1_class_size = edible_dataset.shape[0]
    c2_class_size = poisonous_dataset.shape[0]


    for i in xrange(num_features):
        if i == 22 or  i == 23:
            fisher[i] = 0
            continue

        c1_mean = edible_dataset[:,i].mean()
        c2_mean = poisonous_dataset[:,i].mean()

        c1_var = edible_dataset[:,i].var()
        c2_var = edible_dataset[:,i].var()

        denom = (c1_class_size * c1_var) + (c2_class_size * c2_var)

        if denom == 0:
            denom = 0.000000000001

        numer = (c1_mean - c2_mean) * (c1_mean - c2_mean)

        fisher[i] = numer/denom
    print fisher
    print "="*50
    print len(fisher)
    indices = fisher.argsort()[-10:][::-1]
    vocab = morph_dataset2.vocabulary_
    print "="*50
    print indices
    print "="*50
    print vocab
    print "="*50

    for index in indices:
        for item in vocab:
            if vocab[item] == index:
                print item, fisher[index]
'''
