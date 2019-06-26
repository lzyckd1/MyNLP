import Backpropagation

def window_and_move(word_list1, word_list2, matrexlist):
    wordsize = len(word_list2)
    vec = [0 ,0 ,0 ,0]
    for i in range(2,len(word_list1)-3):
        for j in range(0, wordsize - 1):
            if word_list2[j] == word_list1[i - 2]:
                vec[0] = j
            if word_list2[j] == word_list1[i - 1]:
                vec[0] = j
            if word_list2[j] == word_list1[i + 1]:
                vec[2] = j
            if word_list2[j] == word_list1[i + 2]:
                vec[3] = j
            if word_list2[j] == word_list1[i]:
                preout = j
        input = Backpropagation.input_layer(vec, wordsize)
        matrexlist = Backpropagation.hidden_layer(matrexlist[0], input, matrexlist[1], 10, wordsize, preout)
    return matrexlist