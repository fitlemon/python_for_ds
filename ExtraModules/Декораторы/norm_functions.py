def get_params(data):
    mins = data.min(axis=0)
    maxs = data.max(axis=0)
    
    params = {
        'min': mins,
        'max': maxs
    }

    return params

def apply_params(data, params):
    data_transformed = (data - params['min']) / (params['max'] - params['min'])

    return data_transformed
