import itertools
import pandas as pd

def get_group_distances(dist_matrix, metadata, group_by_column):
    output_df = pd.DataFrame(
        columns=["distance_measure", "{}".format(group_by_column)])

    grouped_samples = md.groupby(metadata[group_by_column])

    for group_label, group in grouped_samples:
        group_combs = itertools.combinations(group.index, 2)

        for each in group_combs:
            row = pd.DataFrame([
                [dist_matrix[each[0]][each[1]],
                 group_label]
                ],
                columns=["distance_measure", "{}".format(group_by_column)],
                index=[frozenset(each)],
                )
            output_df = output_df.append(row)

    return output_df

if __name__ == "__main__":
    # demo distance matrix
    df = pd.DataFrame(
        [[0, 1, 5, 3, 9, 8, 1, 2],
         [1, 0, 2, 7, 14, 4, 5, 9],
         [5, 2, 0, 4, 10, 3, 4, 5],
         [3, 7, 4, 0, 8, 9, 3, 13],
         [9, 14, 10, 8, 0, 11, 2, 6],
         [8, 4, 3, 9, 11, 0, 3, 7],
         [1, 5, 4, 3, 2, 3, 0, 12],
         [2, 9, 5, 13, 6, 7, 12, 0]],
        columns=["a", "b", "c", "d", "e", "f", "g", "h"],
        index=["a", "b", "c", "d", "e", "f", "g", "h"])

    md = pd.DataFrame(
            [["red", 3], ["red", 9], ["blue", 3], ["blue", 9],
             ["red", 15], ["blue", 15], ["red", 21], ["blue", 21]],
            columns=["team", "days"],
            index=["a", "b", "c", "d", "e", "f", "g", "h"]
            )

    demo_group_distances_days = get_group_distances(df, md, "days")
    print("By days:\n" + str(demo_group_distances_days))

    print("\n" + "-"*25 + "\n")

    demo_group_distances_team = get_group_distances(df, md, "team")
    print("By Team:\n" + str(demo_group_distances_team))
