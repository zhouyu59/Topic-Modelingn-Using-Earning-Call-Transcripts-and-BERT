# Topic-Modelingn-Using-Earning-Call-Transcripts-and-BERT

This project uses topic modeling techniques to identify topics in earning call transcripts. The results of the topic model can be used
to gain insights about econimic situation and help people to make decision for business problems.

Below are some important insights that were found from the results:

1.
<img src="https://github.com/zhouyu59/Topic-Modelingn-Using-Earning-Call-Transcripts-and-BERT/assets/124629778/98ee9c89-70b3-40bb-8c3e-161bef0c6db5" width="500">

Pearsons correlation: -0.708

Frequency of Topic 1 (COVID-19 panmdeic) is negatively correlated with Topic 6 (insurance, reinsurance). The results demonstrated that COVID-19 pandemic had a negative impact on insurance industry. Reports from Deloitte and PwC also showed and confirmed that there was a negative impact on insurance industry during COVID pandemic. Customers stopped paying and renewing their insurance during COVID pandemic because they cannot afford premium or anuity payment. Furthermore, people are less likely to travel and leave their home. As a result, people will not renew car insurance or other types of insurances. Thus, during pandemic, insurance companies had reduced claims, and this led to insurers purchasing less reinsurance (1,2).

2.
<img src="https://github.com/zhouyu59/Topic-Modelingn-Using-Earning-Call-Transcripts-and-BERT/assets/124629778/693d3c23-53c6-4f90-8765-9166d747bf5e"
 width="500">

Pearsons correlation: 0.609

Frequency of Topic 2 (deposit rate, deposit, deposit beta) is positively correlated with Topic 18 (volatility, VIX). The results demonstrated that high deposit rate might indicate that the market is more volatile. The correlation could also be observed from the graph of VIX and the graph of deposit rate. 

Graph of deposit rate (3):



<img src="https://github.com/zhouyu59/Topic-Modelingn-Using-Earning-Call-Transcripts-and-BERT/assets/124629778/c6451e57-f2c8-456e-bcd4-cada936af43d"
 width="500">


Graph of VIX (4):

<img src="https://github.com/zhouyu59/Topic-Modelingn-Using-Earning-Call-Transcripts-and-BERT/assets/124629778/84f5bef6-24bd-458e-ad6d-57c4cf333b26"
 width="500">


Both graphs peak at 2008 and 2020.

Please check the notebook and function folder to know the whole pipeline and the detailed implementation.

Citation:
1. https://www2.deloitte.com/ie/en/pages/covid-19/articles/impact-COVID-19-insurance-industry.html
2. https://www.pwc.com/jg/en/issues/covid-19/covid-19-and-insurance-industry.pdf
3. https://libertystreeteconomics.newyorkfed.org/2023/04/deposit-betas-up-up-and-away/
4. https://en.wikipedia.org/wiki/VIX#/media/File:CBOE_Volatlity_Index,_VIX.png



