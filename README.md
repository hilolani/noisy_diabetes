# noisy_diabetes
The toy datasets included with Scikit-learn tend to achieve overly high accuracy when used for machine learning, so noise is added to intentionally lower the accuracy. Please run

pip install git+https://github.com/hilolani/noisy_diabetes.git

to use the contents. The purpose of setting up this repository is to confirm to the learner that modeling machine learning with erroneous data augmentation leads to magical voodoo-like correlation (Kriegeskorte), double dipping, and information leakage, resulting in wrong results. Here, data augmentation is assumed to be realized as a result of repeated measurements on the same experimental participant. An example of data augmentation with noise is described in noisy_diabetes/noisyy_diabetes/noisyy_diabetes.py
and the actual pseudo datasets are stored in noisy_diabetes/noisyy_diabetes/data.

The original diabetes dataset with our noise can be loaded in the same way as in Scikit-learn.

noisy_diabetes = load_noisy_diabetes()

Noisy pseudo datasets with repeated measurements mimicked for data augmentation can be loaded as follows

total_noisy_diabetes = load_total_noisy_diabetes()

In this way, we demonstrated the following through a basic method of applying the simplest multilayer perceptron to diabetes public toy data augmented with systematic noise. Specifically, our partially adjusted double dipping, which focuses on specific areas of interest and applies data augmentation selectively, is more effective than conventional double dipping, which applies data augmentation uniformly across the entire dataset, in successfully achieving magical voodoo correlation.

#############################################################

Scikit Learn's medical toy dataset, diabetes

http://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html#sklearn.datasets.load_diabetes

is suitable for regression problems.

The dataset gives 10 baseline independent variables for each of 442 diabetes patients: age, gender, body mass index, mean blood pressure, and six blood serum measures.
The objective variable is a quantitative measure of disease progression from baseline to one year as the response of interest.
Note that this data is already normalized, so there is no need to use Scalor.

cf.
https://scikit-learn.org/stable/datasets/toy_dataset.html#diabetes-dataset
https://www4.stat.ncsu.edu/~boos/var.select/diabetes.html

References.

Bradley Efron, Trevor Hastie, Iain Johnstone and Robert Tibshirani (2004) “Least Angle Regression,” Annals of Statistics (with discussion), 407-499. (https://web.stanford.edu/~hastie/Papers/LARS/LeastAngle_2002.pdf)

However, this dataset is characterized by the oddly high accuracy typical of toy datasets, and we do not think it is suitable for machine learning training. What we provide here is a private API-compatible noisy toy dataset with normal noise, uniform noise, and data augmentation, in the wake of sklearn.datasets.load_diabetes(), which uses fully public data and code, so manipulation on the Cloud is not a problem. Also in that sense, it is possible for the learner to !git clone the public repository on GitHub on Colab.

Here, we have made it object-oriented, like a Scikit-learn dataset, returning a Bunch, and loaded the data in a form like load_diabetes(), which can be used in Pandas from hilolani's GitHub public repository.You can load it from the public GitHub repository of hilolani by running

!pip install git+https://github.com/hilolani/noisy_diabetes.git

on Colab.

Here is how to create a private dataset with Gaussian noise with a mean of 0 and standard deviation of 0.1 is added to the data to reduce the accuracy of the data.To simulate repeated measurements for data augmentation, we added a constant (in the range of [-0.001, 0.001]) uniform noise to this default row data, which was created by adding Gaussian noise, for 5 iterations.We also added the numbering of participants and sessions corresponding to each generated row. For this reason, we used Pandas' to_csv() function with the index=false option, and when reading using the read_csv() function, in addition to the existing feature names in the diabetes data set, we added dtype={‘participants’: int, 'sessions': int} to the existing feature names in the diabetes dataset.

Strictly speaking, this addition of noise is not correct and requires using the raw data from GitHub and back-transforming to obtain the mean and standard deviation as follows.However, we did not use this method here for the sake of simplicity.

df_raw = pd.read_csv(“diabetes_data_raw_revised.csv”, header=None)

X_raw = df_raw.iloc[:, :-1]

y_raw = df_raw.iloc[:, -1]

mean = X_raw.mean(axis=0)

std = X_raw.std(axis=0)

X_recovered = X_std * std.values + mean.values

The objective variable is also noisy as follows. We created the additional 5 session noisy target index values as ‘y_noisy’, using a random integer that follows a uniform distribution [-2, 2] range to be added to each original y value.
