from datetime import datetime

import matplotlib.pyplot as plt
import pandas as pd
from nlp_rake import Rake
import calendar
import inflection_point
import rake


def get_cluster_keywords(df, n_cluster_keywords=3):
    cluster_articles = []
    for i, row in df.iterrows():
        cluster_articles.append(row["headline"])
    cluster_keywords = rake.most_common_words(cluster_articles, n_themes=n_cluster_keywords)
    return cluster_keywords


def get_valid_articles(articles, cluster_keywords: set, k_threshold, max_words_to_rake=1):
    rk = Rake(max_words=max_words_to_rake)
    valid_articles = []
    for i, article in enumerate(articles):
        a_keywords = rk.apply(article)
        a_k_list = set([k[0] for k in a_keywords])
        overlap = a_k_list.intersection(cluster_keywords)
        if len(overlap) >= k_threshold:
            valid_articles.append(i)
    return valid_articles


def get_knee_from_frequencies(date_frequencies):
    k = inflection_point.identify_single_knee_point(list(date_frequencies.keys()), list(date_frequencies.values()),
                                                    show_plot=True)
    xtix = [str(datetime.fromtimestamp(key).month)+"/"+str(datetime.fromtimestamp(key).day) for key in date_frequencies]
    plt.xticks(list(date_frequencies.keys()), xtix, rotation='vertical')
    plt.subplots_adjust(bottom=0.25)
    plt.xlabel("Day")
    plt.ylabel("Number of articles published")
    plt.show()
    return k


def get_date_frequencies(df):
    date_frequencies = {}
    for i, row in df.iterrows():
        date_frequencies[row["yearmonth"]] = row["count"]
    return date_frequencies


def execute_clustering():
    df = pd.read_csv("/Users/csatyajith/Datasets/UBS/balanced_dataset_with_cluster_id.csv", index_col=False)
    print("Total rows in file are: ", df.shape[0])
    df1 = df.loc[df["cluster"] == 5]
    df1["datetime"] = pd.to_datetime(df1["data"], format="%d/%m/%y")
    df1["yearmonth"] = df1["datetime"].apply(lambda x: datetime(x.year, x.month, 1).timestamp())
    df2 = df1.groupby("yearmonth")["headline"].size().reset_index(name="count")
    knee = get_knee_from_frequencies(get_date_frequencies(df2.iloc[34:]))
    author_sets = df1.loc[df1["yearmonth"] == list(knee)[0]]["authors"].tolist()
    author_list = []
    for author_set in author_sets:
        prelim_list = author_set.split(", and")
        for author in prelim_list:
            author_list.append(author.split(",")[0])
    print(author_list)


def execute_clustering_2():
    df = pd.read_csv("/Users/csatyajith/Datasets/UBS/balanced_dataset_with_cluster_id.csv", index_col=False)
    print("Total rows in file are: ", df.shape[0])
    df1 = df.loc[df["cluster"] == 32]
    cluster_keywords = get_cluster_keywords(df1)
    df1["datetime"] = pd.to_datetime(df1["data"], format="%d/%m/%y")
    df1["yearmonth"] = df1["datetime"].apply(lambda x: datetime(x.year, x.month, 1).timestamp())
    df2 = df1.groupby("yearmonth")["headline"].size().reset_index(name="count")
    knee = get_knee_from_frequencies(get_date_frequencies(df2.iloc[20:]))
    author_sets = df1.loc[df1["yearmonth"] == list(knee)[0]]["authors"].tolist()
    articles = df1.loc[df1["yearmonth"] == list(knee)[0]]["headline"].tolist()
    print(articles)
    author_list = []
    for author_set in author_sets:
        prelim_list = author_set.split(", and")
        for author in prelim_list:
            author_list.append(author.split(",")[0])
    print(knee)
    print(author_list)
    print(cluster_keywords)


def execute_clustering_3():
    df = pd.read_csv("/Users/csatyajith/Datasets/UBS/balanced_dataset_with_cluster_id.csv", index_col=False)
    print("Total rows in file are: ", df.shape[0])
    df1 = df.loc[df["cluster"] == 24]
    df1["datetime"] = pd.to_datetime(df1["data"], format="%d/%m/%y")
    df1["yearmonth"] = df1["datetime"].apply(lambda x: datetime(x.year, x.month, 1).timestamp())
    df2 = df1.groupby("yearmonth")["headline"].size().reset_index(name="count")
    knee = get_knee_from_frequencies(get_date_frequencies(df2.iloc[20:]))
    author_sets = df1.loc[df1["yearmonth"] == list(knee)[0]]["authors"].tolist()
    author_list = []
    for author_set in author_sets:
        prelim_list = author_set.split(", and")
        for author in prelim_list:
            author_list.append(author.split(",")[0])
    print(knee)
    print(author_list)


def execute_clustering_4_lstm_day_wise_politics():
    df = pd.read_csv("/Users/csatyajith/Datasets/UBS/articlesToClusterID-LSTM.csv", index_col=False)
    print("Total rows in file are: ", df.shape[0])
    df1 = df.loc[df["Cluster ID"] == 22]
    print(df1)
    cluster_keywords = get_cluster_keywords(df1)
    df1["datetime"] = pd.to_datetime(df1["date"], format="%d/%m/%y")
    df1["yearmonth"] = df1["datetime"].apply(lambda x: datetime(x.year, x.month, x.day).timestamp())
    df2 = df1.groupby("yearmonth")["headline"].size().reset_index(name="count")
    knee = get_knee_from_frequencies(get_date_frequencies(df2.iloc[7:14, :]))
    author_sets = df1.loc[df1["yearmonth"] == list(knee)[0]]["authors"].tolist()
    author_list = []
    for author_set in author_sets:
        prelim_list = author_set.split(", and")
        for author in prelim_list:
            author_list.append(author.split(",")[0])
    print(author_list)
    print(cluster_keywords)


def execute_clustering_5_black_voices():
    df = pd.read_csv("/Users/csatyajith/Datasets/UBS/articlesToClusterID-LSTM.csv", index_col=False)
    print("Total rows in file are: ", df.shape[0])
    df1 = df.loc[df["Cluster ID"] == 1]
    df1["datetime"] = pd.to_datetime(df1["date"], format="%d/%m/%y")
    df1["yearmonth"] = df1["datetime"].apply(lambda x: datetime(x.year, x.month, 1).timestamp())
    df2 = df1.groupby("yearmonth")["headline"].size().reset_index(name="count")
    knee = get_knee_from_frequencies(get_date_frequencies(df2.iloc[:, :]))
    author_sets = df1.loc[df1["yearmonth"] == list(knee)[0]]["authors"].tolist()
    author_list = []
    for author_set in author_sets:
        prelim_list = author_set.split(", and")
        for author in prelim_list:
            author_list.append(author.split(",")[0])

    print(author_list)


if __name__ == '__main__':
    execute_clustering()
    execute_clustering_2()
    execute_clustering_3()
    execute_clustering_4_lstm_day_wise_politics()
    execute_clustering_5_black_voices()
