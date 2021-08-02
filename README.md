# Options Portfolio #
- - - -
This Django project is for simulating a portfolio of options strategies (butterfly, condor, straddle, ...) using the [yfinance](https://github.com/ranaroussi/yfinance) api.

## Try it Here! ##
https://options-portfolio.herokuapp.com/

## How It Works ##

* ### Call/Put Tables ###
    * Options chains were given as data frames from [yfinance](https://github.com/ranaroussi/yfinance) and were rendered dynamically using django template tags
      [](/tables.png)

* ### Graphing ###
    * Pay-off diagrams were made with [Chart.js](https://github.com/chartjs/Chart.js)
    [](/graphs.png)

* ### Database ###
    * Uses postgreSQL and django models to store portfolio data

## Current Progress ##
- [ ] Configure database with Heroku
- [ ] Upgrade data source
- [ ] Finish implementing all strategies
- [ ] Portfolio performance time-series graph
- [x] Add pay-off diagrams using [Chart.js](https://github.com/chartjs/Chart.js)
- [x] Create Django models for data 
- [x] Render options chains in scrollable tables 
