from AlgoInvest.utils.combinations import combinations
from AlgoInvest.utils import path_manager
from AlgoInvest.utils.utils import csv_to_list


def brutal_force():
    file_directory = path_manager.folder_path(__file__)
    action_list_csv = path_manager.path_join(file_directory, "../data/actions_list.csv")
    action_list = csv_to_list(action_list_csv)
    # Removed header
    action_list = action_list[1:]

    # Generate all combinations of 1 to size_of_list elements of action_list
    L_combinations =[]
    for k in range(1, len(action_list) + 1):
        combinations(L_combinations, [], action_list, k)

    for x in L_combinations:
        print(x, "\n")
