# Yahoo-Finance-Web-Scraper

The Yahoo finance web scaper is designed to pull key statistics on certain stocks that the user inputs in the Python script. The function iterates through all the table rows in the page and pulls the data and inputs them into a dataframe that the script returns. An example of what the script returns for the company "Seattle Genetics" (SGEN), is displayed below.

                                      Metric Name        Metric
0                          Market Cap (intraday) 5        13.81B
1                               Enterprise Value 3        11.16B
2                                    Trailing P/E            N/A
3                                    Forward P/E 1       -140.00
4                      PEG Ratio (5 yr expected) 1         -2.50
5                                Price/Sales (ttm)         18.23
6                                 Price/Book (mrq)         10.85
7                       Enterprise Value/Revenue 3         14.73
8                        Enterprise Value/EBITDA 6        -54.28
9                               Beta (3Y Monthly)           1.74
10                                52-Week Change 3        -6.36%
11                         S&P500 52-Week Change 3         1.27%
12                                  52 Week High 3         88.19
13                                   52 Week Low 3         50.71
14                         50-Day Moving Average 3         73.99
15                        200-Day Moving Average 3         71.77
16                             Avg Vol (3 month) 3       987.76k
17                              Avg Vol (10 day) 3        968.3k
18                            Shares Outstanding 5       161.72M
19                                          Float           112M
20                            % Held by Insiders 1         1.16%
21                        % Held by Institutions 1       106.89%
22                   Shares Short (Aug 15, 2019) 4          7.5M
23                    Short Ratio (Aug 15, 2019) 4          5.36
24               Short % of Float (Aug 15, 2019) 4         6.92%
25  Short % of Shares Outstanding (Aug 15, 2019) 4         4.64%
26       Shares Short (prior month Jul 15, 2019) 4         9.71M
27                  Forward Annual Dividend Rate 4           N/A
28                 Forward Annual Dividend Yield 4           N/A
29                 Trailing Annual Dividend Rate 3           N/A
30                Trailing Annual Dividend Yield 3           N/A
31                 5 Year Average Dividend Yield 4           N/A
32                                  Payout Ratio 4         0.00%
33                                 Dividend Date 3           N/A
34                              Ex-Dividend Date 4           N/A
35               Last Split Factor (new per old) 2           N/A
36                               Last Split Date 3           N/A
37                               Fiscal Year Ends   Dec 31, 2018
38                       Most Recent Quarter (mrq)  Jun 30, 2019
39                                  Profit Margin        -36.94%
40                          Operating Margin (ttm)       -30.13%
41                          Return on Assets (ttm)        -9.06%
42                          Return on Equity (ttm)       -21.08%
43                                   Revenue (ttm)       757.58M
44                         Revenue Per Share (ttm)          4.72
45                  Quarterly Revenue Growth (yoy)        28.40%
46                              Gross Profit (ttm)          1.1M
47                                         EBITDA       -205.62M
48                  Net Income Avi to Common (ttm)      -279.82M
49                               Diluted EPS (ttm)         -1.74
50                 Quarterly Earnings Growth (yoy)           N/A
51                                Total Cash (mrq)       376.13M
52                      Total Cash Per Share (mrq)          2.33
53                                Total Debt (mrq)        79.38M
54                         Total Debt/Equity (mrq)          6.24
55                             Current Ratio (mrq)          3.03
56                      Book Value Per Share (mrq)          7.87
57                       Operating Cash Flow (ttm)      -126.64M
58                    Levered Free Cash Flow (ttm)       -66.69M
