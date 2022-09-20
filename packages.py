import os, io
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import seaborn as sns  # visualization tool
import matplotlib
import matplotlib.pyplot as plt
import missingno as msno
import streamlit as st

from googletrans import Translator

from sklearn.impute import SimpleImputer
import plotly.express as px
from sklearn.cluster import KMeans

import sys
import time

import plotly.graph_objects as go
st.set_option('deprecation.showPyplotGlobalUse', False)

import nltk
from nltk.corpus import stopwords