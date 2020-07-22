#### Pair Problem

For today's pair, your goal is to predict whether or not a patient died during their ICU stay based on their lab values and vital sign measurements.

The dataset is from the MIMIC database. Our target variable will be the `hospital_expire_flag` column, which equals 1 if the patient died during the ICU stay. The other variables will be used as predictors.

Go through the following steps.

1. Load the dataset "MIMIC_Data_small.csv" into a dataframe. Set y = 'hospital_expire_flag' and X = remaining columns.
2. Split the data into train and test sets (80/20) with `random_state=42`
3. Determine what is the "baseline" probability of mortality in the ICU (looking only at the training set).
4. We want to understand the relationship between the predictors and the target (looking only at the training set). Let's start with `resprate_mean`. What is the (empirical) probability of mortality for patients with `resprate_mean` between 30 and 32? What about between 16 and 18? Between 6 and 12? What does this info tell you?
5. Try to use the `hist` function to get bin counts and plot how the empirical probability changes with the value of `resprate_mean`.  Then do it for the other predictor variables. (Hint: see code snippet below)
6. Before doing any logistic regression, guess which predictor variable you think will yield the best (single predictor) logistic regression model. Then run 6 logistic regression models - one for each variable. Was your prediction right?  Use the `log_loss` function in `sklearn.metrics` to measure model performance (the closer to 0, the better).
7. Fit a logistic regression model using all of the variables. What is the `log_loss`?

Here is a code snippet that may be useful (on step 5 above):

```
fig, ax = plt.subplots(3, 1, figsize=(10, 12))  # 3 Rows, 1 Col

count0, bins_0, _ = ax[0].hist(X_train.loc[(y_train==0),'resprate_mean'], bins=25, range=(0,50))
count1, bins_1, _ = ax[1].hist(X_train.loc[(y_train==1),'resprate_mean'], bins=25, range=(0,50))
ax[2].plot((bins_0[:-1]+bins_0[1:])/2,count1/(count1 + count0))
```