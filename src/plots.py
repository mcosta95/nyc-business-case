import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


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


def plot_violation_code_analysis(violation_risk_dist, violation_critical_map):

    plt.figure(figsize=(14,11))

    bars = []
    bottom = pd.Series([0] * len(violation_risk_dist), index=violation_risk_dist.index)

    colors = {
        'High': '#d73027',
        'Moderate': '#fc8d59',
        'Low': 'green'
    }

    # Draw stacked bars for each risk category
    for risk in colors.keys():
        if risk in violation_risk_dist.columns:
            bar = plt.barh(
                y=violation_risk_dist.index,
                width=violation_risk_dist[risk],
                left=bottom,
                label=risk,
                color=colors[risk]
            )
            bottom += violation_risk_dist[risk]
            bars.append(bar)

    # Draw red circles for critical violations
    for i, vc in enumerate(violation_risk_dist.index):
        if violation_critical_map.get(vc) == 'Critical':
            plt.plot(-5, i, 'o', color='red')  # circle left of the bar

    # Formatting
    plt.title('Violation Codes with Risk Category Breakdown')
    plt.xlabel('Inspection Count')
    plt.ylabel('Violation Code')

    # Custom legend to include red circle for critical
    critical_legend = Line2D([0], [0], marker='o', color='w', label='Critical',
                             markerfacecolor='red', markersize=8)
    plt.legend(handles=[*bars, critical_legend], loc='center left', bbox_to_anchor=(1, 0.5), title='Risk Category')

    plt.tight_layout()
    plt.show()




def stacked_bar_plot(df, col_a, col_b, label_a, title, legend_title="Risk Category"):

    df_plot = pd.crosstab(df[col_a], df[col_b], normalize='index').sort_values(by='High', ascending=False)
    df_plot.plot(kind='bar', stacked=True, figsize=(12,6), colormap='coolwarm')
    plt.title(title)
    plt.xlabel(label_a)
    plt.ylabel("Proportion")
    plt.xticks(rotation=45, ha='right')
    plt.legend(title=legend_title)
    plt.tight_layout()
    plt.show()