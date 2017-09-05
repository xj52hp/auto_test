# -*- coding: utf-8 -*-

from assertpy import assert_that

class Getjosn():
    def get_josn(self, json):
        josn_T = ''
        for key, value in json.items():
            try:
                print('key:', key, 'value', value)
                # if assert_that('key_').is_subset_of(str(key)):
                    # i = key.split('_')[-1]
                    # param_T = param_T + str(mOperate[str('key_' + i)]) + '=' + str(mOperate[str('value_' + i)]) + '&'
            except AssertionError as e:
                pass
        # param_url = param_T[:-1]
        # return param_url
