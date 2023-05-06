# version 4 of evaltree 
def evaltree(root, xTe, bools=list()):
    """Evaluating xTe using decision tree root.
    Input:
        root: TreeNode decision tree
        xTe:  n x d matrix of data points
    Output:
        pred: n-dimensional vector of predictions
    """
#     assert root is not None
    samples = xTe.shape[0]
    
    pred = np.zeros(samples)
    # TODO:
    
        
    right = (xTe[:,root.cutoff_id]>root.cutoff_val)
    left = (xTe[:,root.cutoff_id]<=root.cutoff_val)
    
    if len(bools) < 1: 
        bools = np.ones(samples) == 1
    
    left_i = bools & left
    right_i = bools & right 
    
    rt_r = root.right
    rt_l = root.left
    rt_rr = rt_r.right
    rt_rl = rt_r.left
    rt_ll = rt_l.left
    rt_lr = rt_l.left
    
        
    if (rt_ll != None) or (rt_lr != None):
        
        pred[left_i]=evaltree(rt_l, xTe, left_i)
        
    else:
        pred[left_i]=rt_l.prediction
        
    
    if (rt_rl != None) or (rt_rr != None):
        
        pred[right_i]=evaltree(rt_r, xTe, right_i)
    
    else:
        pred[right_i]=rt_r.prediction
        
    if rt_l is None and rt_r is None:
        bools_sum = np.sum(bools)
        
        return np.ones(bools_sum) * root.prediction
      
    prediction = pred[bools]
        
    return prediction