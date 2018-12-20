import React from 'react';
import ReactDom from 'react-dom';
import axiosDefaults from 'axios/lib/defaults';
import { AppComponent } from './components/app';

axiosDefaults.xsrfHeaderName = "X-CSRFToken";
axiosDefaults.validateStatus = function (status) {
  return status >= 200 && status < 500;
};
axiosDefaults.timeout = 10000; // 10s

ReactDom.render(
    <AppComponent />
  , document.getElementById('todos-wrapper'))

