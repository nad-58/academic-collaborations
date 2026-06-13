# Architecture and Technical Insights

## Smart-grid model triad

A practical flexibility service requires three connected analytical components:

1. electricity-demand forecasting;
2. renewable-generation forecasting;
3. flexibility-offer optimisation using forecasts and market signals.

This project implements the demand-forecasting component and defines interfaces that can later feed an optimisation layer.

## Five-stage machine-learning pipeline

```text
Data cleansing
    ↓
Shape-factor engineering
    ↓
Feature and lag selection
    ↓
Behavioural clustering
    ↓
Baseline and regression benchmarking
```

Continuous error analysis should be applied after every stage rather than only after model training.

## Baseline-first forecasting

Before selecting a machine-learning model, the project now evaluates two simple forecasting baselines:

- persistence baseline: uses the most recent observed lag as the prediction;
- seasonal-naive baseline: uses the same quarter-hour period from the previous day.

These baselines are important because short-term demand data is strongly autocorrelated. A complex model should only be preferred when it consistently improves on these transparent references under chronological validation.

## Why shape factors matter

Direct Euclidean comparison of two daily load curves can overstate their difference when one household performs the same activity a few minutes later. Shape factors summarise demand over behavioural time windows, reducing sensitivity to minor temporal shifts.

The public implementation includes seven factors describing:

- daily average relative to daily peak;
- office-hour average relative to peak;
- office-hour average relative to daily average;
- lunch-period demand;
- minimum office-hour demand;
- evening demand;
- overnight peak relative to evening peak.

## Cluster-based architecture

```text
Smart-meter demand
    ↓
Shape-factor extraction
    ↓
K-means routing
    ├── Baseline and forecast model 1
    ├── Baseline and forecast model 2
    ├── Baseline and forecast model 3
    └── Baseline and forecast model 4
    ↓
Aggregated grid-demand forecast
```

Cluster labels are behavioural summaries, not verified personal attributes.

## Aggregation effect

Individual residential demand contains unpredictable activity-level noise. Aggregating multiple profiles can reduce relative variability because independent peaks and troughs partly offset one another. The code therefore includes an aggregation utility for constructing combined demand profiles.

## Model-selection interpretation

The academic comparison considered linear regression, random forest, and LSTM. Random forest provided the strongest reported balance between forecasting error and computational cost. This should not be interpreted as a universal result: model choice depends on dataset size, region, horizon, baseline performance, and deployment constraints.

## Next technical extensions

The next planned extensions are rolling-window retraining and prediction intervals. Rolling retraining should be evaluated only after the static chronological split and baseline comparisons are stable. Prediction intervals should then be added to quantify uncertainty around point forecasts.

## Deployment implications

The architecture supports:

- day-ahead scheduling;
- local-energy-community forecasting;
- aggregator portfolio planning;
- distribution-network demand estimation;
- later integration with renewable-generation and flexibility optimisation models.
