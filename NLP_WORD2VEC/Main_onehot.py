from word2vec_onehot import Backpropagation
from word2vec_onehot import Read_Cut
from word2vec_onehot import Window_dispose
import torch

vec_size = 10
hiden_size = 1
article = Read_Cut.read_the_file_as_string()
word_list1 = Read_Cut.cut_the_strings_into_words(article)
word_list2 = []
for i in word_list1:
    word_list2.append(i.lower())
word_list2 = list(set(word_list1))
W0 = torch.randn(len(word_list2), 10)
W1 = torch.randn(10, len(word_list2))
matrexlist = [W0, W1]
matrexlist = Window_dispose.window_and_move(word_list1, word_list2, matrexlist)
