Morphanalyser-in-Hindi
======================

Morphanalyser in Hindi

Akshita Jha 201225081
Prathyusha Danda 201225156


|-- training_files.txt - file names of all the training files
						 class_labels.py and feature_extraction.py takes this file as input, opens each file in the training_files.txt, and performs its operations

|-- class_labels.py - python file to extract class_labels using edit_distance.py 
					  Run : python class_labels.py training_files.txt > unique_class_labels.txt

|-- unique_class_labels.txt - contains all the unique class_labels

|-- edit_distance.py - computes the edit distance between two words and gives the operations (class_labels)

|-- feature_extraction.py - extracts all the features using morphanalysis.py
							Run: python features.py training_file.txt > sma++_data.txt

|-- sma++_data.txt - contains all the extracted features

|-- morphanalysis.py - extracts the various features

|-- training_tokens.txt - contains all the tokens of training data

|-- vectorize_features.py - code to vectorize sma++_data.txt

|-- __init__.py

|-- readme.txt
