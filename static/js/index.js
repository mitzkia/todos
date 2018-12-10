import React from 'react';
import ReactDom from 'react-dom';
import axiosDefaults from 'axios/lib/defaults';

axiosDefaults.xsrfHeaderName = "X-CSRFToken";
axiosDefaults.validateStatus = function (status) {
  return status >= 200 && status < 500;
};
axiosDefaults.timeout = 10000; // 10s


ReactDom.render((
    <h1>Hello from index.js</h1>
  ), document.getElementById('todos-wrapper'))
