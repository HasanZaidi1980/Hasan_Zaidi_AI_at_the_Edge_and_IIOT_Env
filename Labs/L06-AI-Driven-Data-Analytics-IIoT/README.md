## L06: AI-Driven Data Analytics for IIoT
- What I did: I performed time-series forecasting on IoT temperature data. I implemented a pipeline including data cleaning, feature extraction, and used Nixtla AutoML and a Variational Autoencoder (VAE) for data augmentation.
- What I learned: I learned that frameworks like Nixtla significantly reduce manual hyperparameter tuning and that feature engineering (like seasonal labels) is often more impactful than model complexity.
- Challenges faced: Handling irregular sampling and "glitches" in high-frequency IIoT data required applying spline interpolation to ensure a continuous time-series for the models.
