# SRM checker

Module is built for checking dataset for Sample Ratio Mismatch.  
  
Inputs:  
* df (required) - pandas data frame with experimental data, including group names (required) and dimenstions (optional)  
Example:
```tsv
|    | group        | country   | platform   |   payment |
|---:|:-------------|:----------|:-----------|----------:|
|  0 | experimental | DE        | ios        |         0 |
|  1 | control      | IT        | web        |         1 |
|  2 | experimental | UK        | android    |         0 |
|  3 | experimental | IT        | web        |         1 |
|  4 | control      | DE        | android    |         0 |
```    
* groups (required) - name of the column that contains groups names  
* proportion (required) - dictionary of group names and related proportion in the dataset  
Example:  
```json
{
    "experimental": 0.5, 
    "control": 0.5
}
```  
* dimensions (optional) - list of dimensions (column names in df) to check SRM by.  
  
Exampe of usage:  
```python
check_srm(
        df=df, 
        groups='group', 
        proportion={'experimental':0.5, 'control':0.5}, 
        dimensions=['country', 'platform'])
```  
Example of output:  
```tsv
|    | split    |   p value |
|---:|:---------|----------:|
|  0 | groups   |     0.035 |
|  1 | country  |     0.114 |
|  2 | platform |     0.714 |
```