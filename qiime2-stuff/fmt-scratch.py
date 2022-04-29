def decompose_distance_matrix_to_df(dist_matrix):
     if type(dist_matrix) != "pandas.core.frame.DataFrame":
         raise ValueError("input not a pandas dataframe")

     output_dict = dict()
     for row in dist_matrix.index:
         for col in dist_matrix.columns:
             k = frozenset([row, col])
             v = dist_matrix.loc[row, col]
             if k not in output_dict and len(k) == 2:
                 output_dict[k] = v

     return output_dict


def string_to_unirep(string: str):
    uni_out = "".join(r"\u{:04X}".format(ord(chr)) for chr in string)
    return uni_out
