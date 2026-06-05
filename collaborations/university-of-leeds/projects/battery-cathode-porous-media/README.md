# Leeds Battery Cathode Case Study

## Overview

This case study summarises the interdisciplinary project **“A computational framework for predicting porous media properties of lithium-ion battery cathode.”** The collaboration brought together the University of Leeds, the University of York, and industry.

My role was as an **industry co-supervisor and AI/ML collaborator**, supporting the machine-learning methodology, evaluation thinking, and translation of the computational workflow into a practical AI-enabled engineering framework.

## Motivation

Battery performance depends on upstream manufacturing and material behaviour. The project connected fabrication variables with porous-media property prediction, focusing on **porosity**, **permeability**, and **tortuosity**.

## Workflow

![Leeds battery cathode workflow](../../../../../assets/leeds-battery-cathode-framework.svg)

The workflow combined:

1. **Coating and calendering** using validated CFD, a shear-thinning non-Newtonian fluid assumption, and design of experiments over five key process parameters.
2. **Porous-media generation** in MATLAB using Gamma and Weibull particle-radius distributions.
3. **Image processing and porosity extraction** in Python.
4. **Physics-based reference generation** using lattice-Boltzmann modelling for permeability and tortuosity.
5. **CNN training** for fast prediction of porous-media properties from generated structures.

A total of **243 test cases** were used in the coating study, and a **60% thickness reduction** was applied for dried and calendered coatings.

## Results snapshot

| Distribution | Porosity (Python) | Porosity (CNN) | Permeability (LBM) | Permeability (CNN) | Tortuosity (LBM) | Tortuosity (CNN) |
|---|---:|---:|---:|---:|---:|---:|
| Gamma | 0.51 | 0.52 | 1.36 | 1.18 | 2.08 | 2.43 |
| Weibull | 0.47 | 0.48 | 1.62 | 1.51 | 1.77 | 1.94 |

These results illustrate CNN-based surrogate prediction against porosity calculations and LBM-derived reference properties.

## My contribution

My contribution focused on:

- AI/ML methodology;
- model evaluation and interpretation;
- technical supervision of the machine-learning elements;
- interdisciplinary translation between data-driven methods and engineering simulation.

## Why this matters

This work demonstrates how AI can support advanced engineering workflows when combined with physics-based models rather than treated as a standalone black box. It reflects broader interests in physics-informed AI, advanced manufacturing, battery and energy-storage applications, research-to-industry translation, and interdisciplinary supervision.

## Next steps

The project highlighted two natural extensions:

- incorporating more physics-driven fabrication models, particularly drying and calendering;
- coupling the framework with downstream electrochemical-thermal modelling for battery-performance analysis.

## Public note

This page is based on project material that I am permitted to share as part of the collaboration. It is presented as a concise portfolio case study rather than a full reproduction of the original research outputs.