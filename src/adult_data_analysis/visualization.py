import matplotlib.pyplot as plt
import seaborn as sns


def statistical_plots(adult_df, var, separate_by="income"):
    plt.subplot(131)
    sns.histplot(data=adult_df, x=var, hue=separate_by, multiple="stack")

    plt.subplot(132)
    sns.kdeplot(data=adult_df, x=var, hue=separate_by, multiple="stack")

    plt.subplot(133)
    sns.boxplot(data=adult_df, y=var, x=separate_by)


def normalized_count_heatmap(adult_df, var, separate_by="income"):
    sns.heatmap(
        adult_df.groupby(separate_by)[[var]].value_counts(normalize=True).unstack(),
        cmap="Blues",
        annot=True,
        linewidths=1,
        vmin=0.0,
        vmax=1.0,
        fmt=".1%",
    )
