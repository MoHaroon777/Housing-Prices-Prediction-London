{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "77b27d40",
   "metadata": {
    "_cell_guid": "b98b777e-4045-431b-9974-59c5690d9ca0",
    "_uuid": "663539d1-63d6-4f6a-887b-d41d6b8baa84",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-02-03T02:23:50.621069Z",
     "iopub.status.busy": "2022-02-03T02:23:50.614937Z",
     "iopub.status.idle": "2022-02-03T02:23:51.987214Z",
     "shell.execute_reply": "2022-02-03T02:23:51.988016Z",
     "shell.execute_reply.started": "2022-02-03T02:20:39.083377Z"
    },
    "jupyter": {
     "outputs_hidden": false
    },
    "papermill": {
     "duration": 1.388694,
     "end_time": "2022-02-03T02:23:51.988408",
     "exception": false,
     "start_time": "2022-02-03T02:23:50.599714",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Predicted Price : [1675000.  786250.  695000. 1765000.  675000.]\n",
      "0    1675000\n",
      "1     650000\n",
      "2     735000\n",
      "3    1765000\n",
      "4     675000\n",
      "Name: Price, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "# This Python 3 environment comes with many helpful analytics libraries installed\n",
    "# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python\n",
    "# For example, here's several helpful packages to load\n",
    "\n",
    "import numpy as np # linear algebra\n",
    "import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)\n",
    "from sklearn.tree import DecisionTreeRegressor\n",
    "\n",
    "# Input data files are available in the read-only \"../input/\" directory\n",
    "# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory\n",
    "\n",
    "import os\n",
    "# for dirname, _, filenames in os.walk('/kaggle/input'):\n",
    "#     for filename in filenames:\n",
    "#         print(os.path.join(dirname, filename))\n",
    "London_Housing_file_data = \"/kaggle/input/housing-prices-in-london/London.csv\"\n",
    "house_data = pd.read_csv(London_Housing_file_data)\n",
    "\n",
    "#From data columns, store the input columns into a list\n",
    "feature_inputs = [\"Area in sq ft\", \"No. of Bedrooms\", \"No. of Bathrooms\"] \n",
    "\n",
    "X = house_data[feature_inputs]  # use the input list as our inputs\n",
    "y = house_data.Price # store the expected value (Price) into a new variable (y)\n",
    "\n",
    "#create a model and assign a random number to ensure same result on every run\n",
    "London_model = DecisionTreeRegressor(random_state = 7)\n",
    "#Fit data into model\n",
    "London_model.fit(X, y) #where X is our input and y is our desired output\n",
    "\n",
    "print(\"Predicted Price :\" , end=\" \")\n",
    "# Print the top 5 result of the predicted price column\n",
    "print(London_model.predict(X.head()))\n",
    "# Print the top 5 result of the original price column\n",
    "print(house_data.Price.head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3cd2ff8a",
   "metadata": {
    "_cell_guid": "30a388a0-f378-4bbc-97ec-c1481803e031",
    "_uuid": "790dd8c4-a335-4614-8e77-2d986bf6ac0c",
    "collapsed": false,
    "jupyter": {
     "outputs_hidden": false
    },
    "papermill": {
     "duration": 0.00336,
     "end_time": "2022-02-03T02:23:51.996942",
     "exception": false,
     "start_time": "2022-02-03T02:23:51.993582",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.12"
  },
  "papermill": {
   "default_parameters": {},
   "duration": 12.239786,
   "end_time": "2022-02-03T02:23:52.711217",
   "environment_variables": {},
   "exception": null,
   "input_path": "__notebook__.ipynb",
   "output_path": "__notebook__.ipynb",
   "parameters": {},
   "start_time": "2022-02-03T02:23:40.471431",
   "version": "2.3.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
