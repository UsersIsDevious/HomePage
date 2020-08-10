#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django import forms

def Addition():
    data_1 = float(document["data_1"].value)
    data_2 = float(document["data_2"].value)

    Results_Addition = str(data_1+data_2)
    rslt = document["result_Addition"]
    rslt.text = Results_Addition

#ボタンの名前定義
addition_btn = document["Addition"]
#clickが発火したら呼ばれるって定義
addition_btn.bind("click", Addition)