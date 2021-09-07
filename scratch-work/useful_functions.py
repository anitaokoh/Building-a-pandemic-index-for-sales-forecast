def transform_and_split_data(data, transform=False, split=False, **split_keys):
    if transform == True: 
        # print('yes')
        time_series = pd.Series(data['Sales'].values, index=pd.date_range(start_data, periods= row_shape, freq=date_frequency))
    else:
        time_series = data
    if split == True:
        new_data_train = time_series.ix[split_keys['train_set_row_start']:split_keys['train_set_row_end'],split_keys['train_set_column_start']:split_keys['train_set_column_end']]
        new_data_test = time_series.ix[split_keys['test_set_row_start']:split_keys['test_set_row_end'],split_keys['test_set_column_start']:split_keys['test_set_column_end']]
    else:
        new_data_train = None
        new_data_test = None
    results = {'data': time_series, 'training_data':new_data_train, 'test_data':new_data_test}
    return results


def transform_and_split_data(data, transform=False, split=False, **split_keys):
    if transform == True and split==True: 
        time_series = pd.Series(data['Sales'].values, index=pd.date_range(start_data, periods= row_shape, freq=date_frequency))
        new_data_train = time_series.iloc[split_keys['train_set_row_start']:split_keys['train_set_row_end']]
        new_data_test = time_series.iloc[split_keys['test_set_row_start']:split_keys['test_set_row_end']]
    elif transform == False and split==True:
        time_series = data
        new_data_train = time_series.iloc[split_keys['train_set_row_start']:split_keys['train_set_row_end'],split_keys['train_set_column_start']:split_keys['train_set_column_end']]
        new_data_test = time_series.iloc[split_keys['test_set_row_start']:split_keys['test_set_row_end'],split_keys['test_set_column_start']:split_keys['test_set_column_end']]
    else:
        time_series = pd.Series(data['Sales'].values, index=pd.date_range(start_data, periods= row_shape, freq=date_frequency))
        new_data_train = None
        new_data_test = None
    results = {'data': time_series, 'training_data':new_data_train, 'test_data':new_data_test}
    return results
    

start_data = '1992-01-01'
row_shape = data.shape[0]
date_frequency = 'M'

results = transform_and_split_data(data, True, False)

split_keys = {
    'train_set_row_start': 0
    , 'train_set_row_end': -8
    , 'train_set_column_start': None
    , 'train_set_column_end': None
    , 'test_set_row_start': -8
    , 'test_set_row_end': None
    , 'test_set_column_start': None
    , 'test_set_column_end': None
}