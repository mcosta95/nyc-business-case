import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

COLORS = {
    'High': '#8da0cb',
    'Moderate': '#fc8d62',
    'Low': '#66c2a5'
}


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
    plt.figure(figsize=(14, 11))

    bars = []
    bottom = pd.Series([0] * len(violation_risk_dist), index=violation_risk_dist.index)

    dominant_risk = violation_risk_dist.idxmax(axis=1)
    high_risk_codes = dominant_risk[dominant_risk == 'High'].index

    for risk in COLORS.keys():
        if risk in violation_risk_dist.columns:
            bar = plt.barh(
                y=violation_risk_dist.index,
                width=violation_risk_dist[risk],
                left=bottom,
                label=risk,
                color=COLORS[risk]
            )
            bottom += violation_risk_dist[risk]
            bars.append(bar)

    # Draw red circles for critical violations
    for i, vc in enumerate(violation_risk_dist.index):
        if violation_critical_map.get(vc) == 'Critical':
            plt.plot(-5, i, 'o', color='red')  # circle to the left of the bar

    # Highlight y-axis labels (violation codes) in yellow if High is dominant
    ax = plt.gca()
    for tick_label in ax.get_yticklabels():
        code = tick_label.get_text()
        if code in high_risk_codes:
            tick_label.set_color('red')
            tick_label.set_fontweight('bold')

    # Formatting
    plt.title('Violation Codes with Risk Category Breakdown')
    plt.xlabel('Inspection Count')
    plt.ylabel('Violation Code')

    # Custom legend
    critical_legend = Line2D([0], [0], marker='o', color='w', label='Critical',
                             markerfacecolor='red', markersize=8)
    plt.legend(handles=[*bars, critical_legend], loc='center left', bbox_to_anchor=(1, 0.5), title='Risk Category')

    plt.tight_layout()
    plt.show()


def stacked_bar_plot(df, col_a, col_b, label_a, title, legend_title="Risk Category", normalize="index"):

    if normalize == "index":
        label_y = "Proportion"
    else:
        label_y = "Total number"

    df_plot = pd.crosstab(df[col_a], df[col_b], normalize=normalize).sort_values(by='High', ascending=False).sort_index()
    df_plot = df_plot[COLORS.keys()]

    df_plot.plot(kind='bar', stacked=True, figsize=(12,6), color=list(COLORS.values()))
    plt.title(title)
    plt.xlabel(label_a)
    plt.ylabel(label_y)
    plt.xticks(rotation=45, ha='right')
    plt.legend(title=legend_title)
    plt.tight_layout()
    plt.show()


def pie_distribution_category(df, col, categories):
    grp_counts = df[col].value_counts().reindex(categories)
    plt.figure(figsize=(6, 6))
    plt.pie(
        grp_counts,
        labels=grp_counts.index,
        autopct='%1.1f%%',
        startangle=140,
        colors=list(COLORS.values()),
        wedgeprops={'edgecolor': 'black'}
    )
    plt.title('Risk Category Distribution (Pie Chart)')
    plt.axis('equal')
    plt.show()