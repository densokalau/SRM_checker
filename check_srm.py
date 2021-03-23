from scipy import stats
import numpy as np
import pandas as pd


def check_srm(df, groups, proportion, dimensions=None):
    """Function takes pandas data frame, column name for groups names, expected proportion between the groups, and names of dimensions
    and returns data frame with dimension name, p_value and adjusted p_value.
    df - pandas data frame with data for experiment;  
    groups - name of a column in data frame that contains user groups names;
    proportion - dict of expected proportion of each user group. Sum of proportions should be equal to 1;
    dimensions - list of columns that indicate dimensions (like country, os, demographical categories etc). None by default.
    """
    
    results = {
        'split': [],
        'p value': []
    }
    
    # calculate for groups
    observed = []
    expected = []
    
    # for every class in the column calculate observed and expected number of records
    for key in proportion.keys():
        observed.append(df[df[groups]==key].shape[0])
        expected.append(proportion[key] * df.shape[0])
    
    contingency_table = np.array([observed, expected])
    
    # execute chi2 test and get p value
    p_value = stats.chi2_contingency(contingency_table, correction=False)[1]
    
    results['split'].append('groups')
    results['p value'].append(round(p_value, 3))
    
    
    # if dimensions are specified, compare distribution of classes between test and control groups
    if dimensions is not None:
        for dimension in dimensions:
            # get unique classes
            classes = set(df[dimension])
            
            # create dict to store proportions
            groups_dimension = {}
            
            # for each group 
            for key in proportion.keys():
                groups_dimension[key] = []
                
                for c in classes:
                    # append number of records for the group & class combination
                    groups_dimension[key].append(df[(df[groups]==key) & (df[dimension]==c)].shape[0])
            
            
            contingency_table = np.array([groups_dimension[key] for key in groups_dimension.keys()])
            
            p_value = stats.chi2_contingency(contingency_table, correction=False)[1]
    
            results['split'].append(dimension)
            results['p value'].append(round(p_value, 3))
    
    return pd.DataFrame(results)