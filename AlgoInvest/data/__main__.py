import matplotlib.pyplot as plt

from AlgoInvest.utils.utils import csv_to_DataFrame
from AlgoInvest.utils.path_manager import folder_path, path_join


if __name__ == '__main__':
    default_data_folder = path_join(
        folder_path(__file__)
        )
    path_dataset1 = path_join(
        default_data_folder, "dataset1_Python+P7.csv")
    path_dataset2 = path_join(
        default_data_folder, "dataset2_Python+P7.csv")
    
    # Get df of shares from dataset1 and dataset2
    df_dataset1 = csv_to_DataFrame(path_dataset1)
    df_dataset2 = csv_to_DataFrame(path_dataset2)

    df_dataset1 = df_dataset1[1:]
    df_dataset2 = df_dataset2[1:]

    for i in range(1,3):
        df_dataset1[i] = df_dataset1[i].astype(float)
        df_dataset2[i] = df_dataset2[i].astype(float)

    df_dataset1.plot()
    plt.show(block=False)
    # plt.figure()
    df_dataset2.plot()
    plt.show(block=False)

    print(
        "\n\tNumber of data in dataset2_Python+P7.csv <= 0 :\n\t\t",
        df_dataset2[1][df_dataset2[1] <= 0].count())
    input("\n\tPress enter to close this program")
