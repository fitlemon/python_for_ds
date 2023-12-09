def get_params(data):
    means = data.mean(axis=0)
    stds = data.std(axis=0)
    
    params = {
        'mean': means,
        'std': stds
    }

    return params

def apply_params(data, params):
    data_transformed = (data - params['mean']) / params['std']

    return data_transformed
