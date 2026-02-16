# Assignment03

##  Project Overview
This project applies a non-linear transformation to NO₂ air quality data and estimates the parameters of a probability density function (PDF) for the transformed variable.

Dataset: India Air Quality Data (Kaggle)  
Feature Used: NO₂  

##  Methodology

### Step 1: Non-Linear Transformation
Each NO₂ value `x` is transformed into `z` using:

z = x + a_r sin(b_r x)

Where:
- ar = 0.05 × (r mod 7)
- br = 0.3 × ((r mod 5) + 1)
- r = University Roll Number

### Step 2: Probability Density Function Estimation

We assume the transformed variable `z` follows:

p̂(z) = c e^(−λ (z − μ)²)

This corresponds to a Gaussian distribution form.

Parameters are estimated using Maximum Likelihood Estimation (MLE):

- μ = mean of z  
- σ² = variance of z  
- λ = 1 / (2σ²)  
- c = √(λ / π)


##  Output
The project computes:
- Mean (μ)
- Lambda (λ)
- Normalization constant (c)

##  Tools & Libraries
- Python  
- NumPy  
- Pandas  
- Matplotlib  

## Conclusion
After applying the non-linear transformation, the resulting data approximately follows a Gaussian distribution.  
Using MLE, the parameters μ, λ, and c are successfully estimated.

<img width="694" height="456" alt="Screenshot 2026-02-16 at 11 22 55 PM" src="https://github.com/user-attachments/assets/96176b71-5f62-40c5-ac8d-7a070204d3c8" />

