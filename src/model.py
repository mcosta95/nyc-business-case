import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.utils.class_weight import compute_sample_weight
from sklearn.model_selection import RandomizedSearchCV


def plot_feature_importance(best_model, X_train, top_n):
    importances = best_model.feature_importances_

    # Create a DataFrame
    feature_importances = pd.DataFrame({
        'Feature': X_train.columns,
        'Importance': importances
    })

    # Sort by importance
    feature_importances = feature_importances.sort_values(by='Importance', ascending=False)

    # Optional: Plot
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Importance', y='Feature', data=feature_importances.head(top_n))
    plt.title(f'Top {top_n} Feature Importances')
    plt.tight_layout()
    plt.show()

    return feature_importances


def train_with_random_search(
    estimator,
    param_dist,
    X_train,
    y_train,
    model_name='model',
    n_iter=20,
    scoring='f1_macro',
    cv=5,
    sample_weighting=True,
    random_state=42,
    save_model=True,
    verbose=1,
    n_jobs=-1
):

    # Sample weights for class imbalance
    sample_weights = None
    if sample_weighting:
        sample_weights = compute_sample_weight(class_weight='balanced', y=y_train)

    # Randomized Search
    model_search = RandomizedSearchCV(
        estimator=estimator,
        param_distributions=param_dist,
        n_iter=n_iter,
        scoring=scoring,
        cv=cv,
        verbose=verbose,
        random_state=random_state,
        n_jobs=n_jobs
    )

    print(f"Starting RandomizedSearchCV for {model_name}...")
    model_search.fit(X_train, y_train, sample_weight=sample_weights)

    best_model = model_search.best_estimator_
    print(f"Best Parameters for {model_name}:", model_search.best_params_)

    if save_model:
        model_path = f'best_model_{model_name}.joblib'
        joblib.dump(best_model, model_path)
        print(f"Model saved to: {model_path}")

    return best_model



def confusion_matrix(best_model, y_test, y_pred):

    cm = confusion_matrix(y_test, y_pred, labels=best_model.classes_)
    plt.figure(figsize=(8,6))
    sns.heatmap(cm, annot=True, fmt='d', xticklabels=best_model.classes_, yticklabels=best_model.classes_, cmap='Blues')
    plt.title("Confusion Matrix")
    plt.ylabel("Actual")
    plt.xlabel("Predicted")
    plt.show()