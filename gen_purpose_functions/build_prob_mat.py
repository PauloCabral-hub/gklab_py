def build_prob_mat(ctxs, prob_vec, alphabet):
    """ Function Description"""
    pm = [[0 for j in range(alphabet)] for i in range(len(ctxs))]
    
    entry = 1
    for i in range(len(ctxs)):
        for j in range(len(alphabet)):
            pm[i,j] = prob_vec[entry]

    return pm