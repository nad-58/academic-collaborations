# Short-Term Prosumer Demand Forecasting for Smart-Grid Flexibility

## Overview

This anonymised MSc Data Science case study developed a machine-learning workflow for **day-ahead electricity-demand forecasting** of residential prosumers. The technical objective was to support future smart-grid flexibility services by improving understanding and prediction of short-term household demand.

The public version removes all personal names, organisation-specific details, contact information, assessment declarations, and confidential material from the original thesis.

## Problem context

Residential energy systems increasingly include distributed renewable generation, smart meters, flexible devices, and local energy communities. For flexibility services, three analytical capabilities are commonly needed:

1. electricity-demand forecasting;
2. renewable-generation forecasting;
3. flexibility-offer optimisation.

This project focused only on the first capability: forecasting future electricity demand. Optimisation of flexibility offers was outside the project scope.

## Public datasets

The methodology used public household electricity-consumption data and public meteorological data.

The electricity dataset contained high-frequency measurements for multiple anonymised households, including aggregate demand and selected appliance-level channels. The weather dataset provided hourly variables including temperature, dew-point temperature, wind components, and precipitation.

The project recognised important representativeness limitations: the household sample came from one geographic area, covered a limited range of housing types, and therefore should not be assumed to generalise automatically to other populations or climates.

## End-to-end methodology

![Prosumer demand forecasting workflow](../../../../../assets/aston-prosumer-demand-forecasting.svg)

The workflow contained five main stages.

### 1. Data cleansing and integration

Separate household files were integrated and duplicate records were removed. The data contained short missing periods, longer gaps, zero readings, and implausibly large spikes.

The project applied different treatments depending on the issue:

- short missing sequences and selected invalid values were converted to missing values and imputed using a rolling mean;
- longer gaps were filled using the most recent available matching day-of-week profile;
- electricity measurements were resampled to 15-minute intervals;
- moving-average smoothing was applied;
- hourly weather variables were interpolated to the same 15-minute resolution;
- electricity and weather data were then aligned and merged.

This is an important engineering lesson: imputation strategy should depend on the type and duration of the missingness rather than applying one method to every gap.

### 2. Feature engineering

The daily demand curve contained 96 quarter-hour measurements. To characterise behavioural patterns more compactly, the project generated seven normalised **shape factors** using summary statistics over meaningful time windows such as morning, lunch, working hours, evening, and overnight periods.

These shape factors acted as a form of domain-informed dimensionality reduction. They were designed to preserve broad consumption behaviour while reducing sensitivity to small timing shifts in daily activities.

Additional time-series features included historical demand values and selected weather variables.

### 3. Feature selection

Several complementary methods were used:

- Pearson correlation;
- Spearman rank correlation;
- exploratory pairwise analysis;
- autocorrelation and partial autocorrelation;
- mutual information.

The strongest predictor of day-ahead demand was recent historical electricity consumption. Temperature and dew-point temperature had lower but measurable relationships and were strongly correlated with each other. Wind variables had limited influence, while precipitation showed little useful predictive value in this dataset.

The final forecasting features therefore prioritised the previous 96 quarter-hour demand values to capture daily seasonality. One temperature feature was retained for comparison, but adding it did not improve the selected model in the reported experiment.

### 4. Behavioural clustering

K-means clustering was applied to the seven shape factors. Min-max scaling was used because k-means is sensitive to feature magnitude.

The elbow method was used to compare candidate values of *k*, and four clusters were selected as a practical balance between lower within-cluster variation and interpretability.

The resulting profiles suggested different broad demand behaviours, including:

- daytime occupancy or working-from-home patterns;
- lower daytime occupancy;
- high overnight consumption that may indicate overnight charging or another sustained load;
- comparatively constant daily consumption.

These interpretations were treated as behavioural hypotheses rather than confirmed household characteristics.

### 5. Model benchmarking and dynamic retraining

Three regression approaches were benchmarked:

- linear regression;
- random-forest regression;
- a vanilla LSTM network.

A rolling one-month training window was used to help the models adapt to changing seasonal and behavioural conditions.

Random forest produced the best result among the three tested approaches. In one individual-household experiment, the reported MAPE was approximately **44.5%**, although the negative R² showed that performance was still weaker than a simple baseline for that case. The LSTM improved R² relative to random forest in that example but remained negative, while linear regression was substantially worse.

This is a valuable evaluation lesson: selecting the best candidate model does not necessarily mean that the model is good enough for deployment. Absolute performance and comparison against a naïve baseline remain essential.

## Effect of clustering and aggregation

The project explored whether separate models for behavioural clusters could improve forecasting. For selected households with clearer behavioural separation, cluster-specific modelling improved both MAPE and R² compared with treating all days as one homogeneous group.

The study also found that aggregating demand across multiple prosumers improved forecasting accuracy. Aggregation reduced the impact of unpredictable individual behaviour because peaks and fluctuations partially compensated across households.

The strongest reported configuration used random-forest regression on aggregated demand and followed the overall demand trend reasonably well, with larger errors concentrated around unusual sudden spikes.

## Evaluation considerations

The case study highlights several important evaluation principles:

- compare models against a naïve baseline, not only against each other;
- report multiple metrics because one metric can hide poor behaviour;
- inspect time-localised errors and unusual demand spikes;
- use time-aware validation rather than random row splitting;
- fit preprocessing and scaling only on training data;
- evaluate individual, clustered, and aggregated forecasting separately;
- avoid interpreting clusters as confirmed demographic or lifestyle labels;
- document the effect of missing-value imputation on forecasting results.

## My supervision contribution

My contribution as professional supervisor included guidance on:

- problem formulation and technical scope;
- data-quality assessment;
- feature engineering and model selection;
- validation and baseline comparison;
- interpretation of clustering and forecasting results;
- limitations, lifecycle adaptation, and research-to-industry relevance.

## Limitations

The study had several limitations:

- a small number of households from one geographic area;
- restricted housing diversity;
- substantial missing-data treatment;
- limited external validation;
- cluster interpretations based on consumption patterns rather than verified household attributes;
- poor baseline-relative performance for some individual-household forecasts;
- limited hyperparameter search;
- no completed flexibility-optimisation stage.

## Future work

Useful extensions include:

- evaluation on additional public datasets and regions;
- probabilistic forecasts and prediction intervals;
- robust metrics for near-zero demand periods;
- stronger time-series baselines;
- grouped and hierarchical forecasting;
- alternative clustering methods and dynamic time warping;
- explicit drift monitoring and retraining triggers;
- integration with renewable-generation forecasts and flexibility optimisation.

## Public note

This repository page is an independently rewritten and anonymised technical summary. It does not reproduce the original thesis, original confidential figures, named contributors, company information, signatures, contact details, or assessment material.