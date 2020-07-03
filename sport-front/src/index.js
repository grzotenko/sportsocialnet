import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter } from 'react-router-dom';
import { ScreenWidth } from './context';
import Layout from './components/Layout/Main/Main';
const contextData = {
  screenWidth: window.innerWidth
};
ReactDOM.render(
  <ScreenWidth.Provider value={contextData}>
    <BrowserRouter>
      <Layout />
    </BrowserRouter>
  </ScreenWidth.Provider>,
  document.getElementById('root')
);


