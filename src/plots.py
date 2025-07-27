import seaborn as sns
import matplotlib.pyplot as plt

def plot_box_plot(
    df, 
    feature_x='grade', 
    feature_y='score', 
    title="Discrepancies Between Grade and Score", 
    xlabel="Grade Assigned", 
    ylabel="Score", 
    line1_y=13, 
    line1_label='A (13)', 
    line2_y=27, 
    line2_label='B (27)', 
    palette='Set2',
    distribute=True,
    limited_lines=True
):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=feature_x, y=feature_y, data=df, palette=palette)

    if distribute:
        sns.stripplot(x=feature_x, y=feature_y, data=df, color='black', alpha=0.2, jitter=0.2)

    if limited_lines:
        plt.axhline(line1_y, color='green', linestyle='--', label=line1_label)
        plt.axhline(line2_y, color='orange', linestyle='--', label=line2_label)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_paralel_bar_plot(
    df, 
    title="Distribution of Unique Values per Inspection", 
    xlabel="Columns", 
    ylabel="Unique Count", 
    ):
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df)
    plt.xticks(rotation=45)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.show()


def plot_corr_heatmap(df, num_cols):
    corr = df[num_cols].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title("Correlation Matrix")
    plt.show()