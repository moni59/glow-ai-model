
import numpy as np

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)


def evaluate_multilabel(y_true, scores, thresholds=0.5):
    """
    Calcula métricas para clasificación multietiqueta.

    y_true: matriz binaria con las etiquetas reales.
    scores: matriz con las puntuaciones del modelo.
    thresholds: umbral común o un umbral por etiqueta.
    """
    y_true = np.asarray(y_true)
    scores = np.asarray(scores)

    y_pred = (scores >= thresholds).astype(int)

    return {
        "accuracy_exacta": accuracy_score(
            y_true, y_pred
        ),
        "precision_micro": precision_score(
            y_true,
            y_pred,
            average="micro",
            zero_division=0,
        ),
        "recall_micro": recall_score(
            y_true,
            y_pred,
            average="micro",
            zero_division=0,
        ),
        "f1_micro": f1_score(
            y_true,
            y_pred,
            average="micro",
            zero_division=0,
        ),
        "f1_macro": f1_score(
            y_true,
            y_pred,
            average="macro",
            zero_division=0,
        ),
    }
