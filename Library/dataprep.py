# -*- coding: utf-8 -*-
# pylint: disable=C0103
"""
Модуль с обработкой первоначальной БД
"""
import pandas as pd
from Scripts.config import init_path,clean_data_path

def create_data():
    """
    Функция обработки первоначальной Базы Данных
    -------
    Автор: Хасанов М.    
    """
    data = pd.read_csv(init_path, error_bad_lines=(False))
    data = data.iloc[:3000,:]
    data.drop('bookID', axis=1, inplace=True)
    data.drop('isbn', axis=1, inplace=True)
    data.drop('isbn13', axis=1, inplace=True)
    data.dropna(0, inplace=True)
    data.replace(to_replace=('en-US', 'en-GB', 'en-CA'), value='eng', inplace=True)
    data.rename(columns={'  num_pages': 'num_pages'}, inplace=True)
    data['pub_year'] = data['publication_date'].apply(lambda x: int(x.split('/')[2]))
    data['century'] = data['pub_year'].apply(lambda x: '20th' if x < 2000 else '21th')
    data['is_big_book'] = data['num_pages'].apply(lambda x: 'big' if x > 400 else 'small')
    data = data.iloc[:3000,:]
    data.to_csv(clean_data_path)
    