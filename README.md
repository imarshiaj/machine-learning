# Machine Learning Learning Path (2026)

A practical, notebook-first introduction to machine learning, from problem framing and reliable data preparation to classical algorithms, introductory deep learning/LLMs, deployment, monitoring, and responsible AI. All notebook prose and code comments are in English.

> This is an educational learning path, not a guarantee of employability. Tools and API details evolve; validate package versions and model licenses for a real project.

## Learning path

| Folder | Focus | Suggested outcome |
|---|---|---|
| `1. Foundations` | Problem framing, Python/NumPy/pandas refresher, visual EDA | Define task, target, split, baseline, and metric |
| `2. Data Preparation & Feature Engineering` | Missing values, outliers, encoding, scaling, splits, pipelines | Build leakage-safe preprocessing |
| `3. Classical Machine Learning` | Regression, logistic regression, tree ensembles, SVM/KNN/NB, clustering, PCA, evaluation, tuning | Compare models with suitable metrics |
| `4. Deep Learning & LLM Foundations` | Neurons, CNN/RNN concepts, attention, transformers, prompting, fine-tuning, RAG | Understand concepts before a dedicated DL course |
| `5. MLOps & Production` | Persistence, FastAPI, experiment tracking, CI/CD, drift | Reproducibility and serving basics |
| `6. Emerging & Responsible AI` | Agents/tool calling, fairness, interpretability, LLMOps, specialist tracks | Safety and system-level evaluation |
| `7. Portfolio Projects` | Churn, rare-event detection, local RAG retrieval | Small, reproducible portfolio examples |

## Setup

Python 3.10+ is recommended. Create and activate a virtual environment, then run:

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Optional packages for specialist topics can be installed from `requirements-optional.txt`. Do not install large deep-learning or LLM dependencies unless you are working through those lessons. Optional notebooks are designed not to require API credentials by default.

Open the folder in JupyterLab or VS Code and run the notebooks in numerical order. A Jupyter kernel should be registered from the same virtual environment.

## Notebook outputs and continuous validation

The notebooks include saved outputs for key demonstrations, including plots, DataFrame previews, metric tables, and model-serving examples, so the GitHub preview is useful before you run them locally. Re-run the cells in numerical order to reproduce the results in your own environment.

A small GitHub Actions workflow checks notebook JSON and compiles each Python code cell on pushes and pull requests. Run the same check locally with:

```bash
python tools/validate_notebooks.py
```

This lightweight CI check catches malformed notebooks and Python syntax errors; it does not replace execution tests, data-quality review, or evaluation of model suitability.

## Datasets and reproducibility

- `datasets/telecom_churn_synthetic.csv` and `datasets/transactions_synthetic.csv` are synthetic teaching data generated with fixed seeds. They are **not** real customer or fraud data and must not be presented as real-world evidence.
- Most other examples use small built-in scikit-learn datasets or generated arrays and do not require network access.
- Set random seeds for demonstrations where suitable, and record package versions / dataset versions for real work.
- Some code snippets describe optional integrations; see the notebook text before enabling network calls or external models.

## Core concepts emphasized

- Establish baselines before complex models.
- Fit preprocessing on training data only; use pipelines to reduce leakage.
- Select evaluation metrics based on error costs, prevalence, and operational capacity.
- Preserve an untouched test set for final evaluation.
- Save the full pipeline and record model/data/config versions.
- Treat fairness, privacy, security, and post-deployment monitoring as core engineering concerns.

## Official references

- scikit-learn Pipeline: https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html
- scikit-learn model evaluation: https://scikit-learn.org/stable/modules/model_evaluation.html
- XGBoost Python documentation: https://xgboost.readthedocs.io/en/stable/python/
- Hugging Face Transformers Trainer: https://huggingface.co/docs/transformers/trainer
- MLflow tracking: https://mlflow.org/docs/latest/ml/tracking/
- MLflow Model Registry: https://mlflow.org/docs/latest/registry/
- FastAPI first steps: https://fastapi.tiangolo.com/tutorial/first-steps/
- Fairlearn guide: https://fairlearn.org/main/user_guide/index.html

## License and use
Choose an explicit repository license before public release. Check the licenses and terms for any third-party datasets, pretrained models, APIs, or packages you add. This repository is an educational starting point; validate all workflows before using them for real decisions.
