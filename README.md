# This is a demo repo

## Purpose

This repo was mainly created to make sure I know how to use Git and Docker.
Here you can find a linear regression example using `sklearn`.

## How it works
Using data that has been generated, a simple linear regression is completed and the associated y-value is returned.

## Usage

Install the required modules:
```
pip install -r requirements.txt
```

To create new data, use the following:
```
python3 ./src/data/createData.py
```

To run the model, use the following:
```
python3 ./src/model/main.py <x_value>
```