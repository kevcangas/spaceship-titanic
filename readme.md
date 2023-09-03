## [Kaggle's spaceship challenge](https://www.kaggle.com/competitions/spaceship-titanic/overview)

### Python module implemented:

- Scikit-Learn
- Seaborn
- Matplotlib
- Numpy

### Description

In this repository are a solution for the Kaggles's spaceship challenge that implements different models to classify a group of people according the challenge. This models are:

- Histogram-based Gradient Bossting Classifier
- Random Forest
- Tree Classifier

Inside the carpet __models__ are the models.

### Data analysis

The data given by Kaggle has the features:

- PassengerId - A unique Id for each passenger. Each Id takes the form gggg_pp where gggg indicates a group the passenger is travelling with and pp is their number within the group. People in a group are often family members, but not always.
- HomePlanet - The planet the passenger departed from, typically their planet of permanent residence.
- CryoSleep - Indicates whether the passenger elected to be put into suspended animation for the duration of the voyage. Passengers in cryosleep are confined to their cabins.
- Cabin - The cabin number where the passenger is staying. Takes the form deck/num/side, where side can be either P for - Port or S for Starboard.
- Destination - The planet the passenger will be debarking to.
- Age - The age of the passenger.
- VIP - Whether the passenger has paid for special VIP service during the voyage.
- RoomService, FoodCourt, ShoppingMall, Spa, VRDeck - Amount the passenger has billed at each of the Spaceship Titanic's many luxury amenities.
- Name - The first and last names of the passenger.
- Transported - Whether the passenger was transported to another dimension. This is the target, the column you are trying to predict.

The features __PassengerId__ and __Name__ are not functionally to the models implemented, so, they can be erased from the dataset. The feature __Cabin__ can be separated in three different new features that are Deck, Num, Side, all this to improve the data.

All these analysis can be founded in the notebook [dataAnalysis.ipynb](dataAnalysis.ipynb).

### Results

The results of the different models are the following.

- Histogram-based Gradient Bosting Classifier:

        precision    recall  f1-score   support

        False       0.80      0.79      0.80      1203
        True       0.80      0.81      0.81      1240

        accuracy                           0.80      2443
        macro avg       0.80      0.80      0.80      2443
        weighted avg       0.80      0.80      0.80      2443

- Random Forest:

        precision    recall  f1-score   support

        False       0.77      0.80      0.78      1203
        True       0.80      0.77      0.78      1240

        accuracy                           0.78      2443
        macro avg       0.78      0.78      0.78      2443
        weighted avg       0.78      0.78      0.78      2443

- Tree Classifier:

        precision    recall  f1-score   support

        False       0.75      0.83      0.79      1303
        True       0.81      0.72      0.77      1305

        accuracy                           0.78      2608
        macro avg       0.78      0.78      0.78      2608
        weighted avg       0.78      0.78      0.78      2608