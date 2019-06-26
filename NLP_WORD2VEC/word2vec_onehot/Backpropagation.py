import torch
import math
import numpy as np

def input_layer(vec, word_size):
    input = torch.zeros(4, word_size)
    temp = torch.Tensor([1, 1, 1, 1])
    for i in range(0, word_size - 1):
        input[i, vec[i]] = 1
    return temp.mm(input)


def hidden_layer(W0, input, W1, hidden_size, word_size, pre_out):
    '''
    forward
    '''
    result1 = input.mm(W0)
    result1 = result1 / word_size
    result2 = result1.mm(W1)
    result3 = torch.exp(result2)
    sum_num = 0
    for i in range(0,result3.size()):
        sum_num = sum_num + result3[i]
    result3 = result3 / sum_num
    '''
    back
    '''
    loss = 0
    for i in range(0, word_size):
        loss += (result3[i] - pre_out[i])*(result3[i] - pre_out[i])
    for i in range(0, word_size):
        for j in range(0, hidden_size):
            sub = 0
            for k in range(0, word_size):
                sub += (2 * result3[k] - 2 * pre_out[k])
                sub *= result2[k] * (loss - result2[k]) / (loss * loss)
                sub *= W1[i ,j] * input[i] / 4
            W0[i][j] -= sub
    for i in range(0, hidden_size):
        sub = 0
        for j in range(0, word_size):
            sub = 2 * result3[j] - 2 * pre_out[j]
            sub = sub * math.exp(result2[j]) * (loss - math.exp(result2[j])) / (loss * loss)
            sub = sub * result1[i]
            W1[i, j] -= sub
    return [W0, W1]