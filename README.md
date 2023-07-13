# Topic-Modelingn-Using-Earning-Call-Transcripts-and-BERT

This project uses topic modeling techniques to identify topics in earning call transcripts. The results of the topic model can be used
to gain insights about econimic situation and help people to make decision for business problems.

Below are some important insights that were found from the results:

1.
<img src="https://github.com/zhouyu59/Topic-Modelingn-Using-Earning-Call-Transcripts-and-BERT/assets/124629778/2be0e476-9023-4114-b99f-8af04ab6db5c" width="500">

Pearsons correlation: -0.708

Frequency of Topic 1 (COVID-19 panmdeic) is negatively correlated with Topic 6 (insurance, reinsurance). The results demonstrated that COVID-19 pandemic had a negative impact on insurance industry. Reports from Deloitte and PwC also showed and confirmed that there was a negative impact on insurance industry during COVID pandemic. Customers stopped paying and renewing their insurance during COVID pandemic because they cannot afford premium or anuity payment. Furthermore, people are less likely to travel and leave their home. As a result, people will not renew car insurance or other types of insurances. Thus, during pandemic, insurance companies had reduced claims, and this led to insurers purchasing less reinsurance (1,2).

2.
<img src="https://github.com/zhouyu59/Topic-Modelingn-Using-Earning-Call-Transcripts-and-BERT/assets/124629778/7e2035db-9f83-44d5-8026-3051c1bea5a6" width="500">

Pearsons correlation: 0.609

Frequency of Topic 2 (deposit rate, deposit, deposit beta) is positively correlated with Topic 18 (volatility, VIX). The results demonstrated that high deposit rate might indicate that the market is more volatile. The correlation could also be observed from the graph of VIX and the graph of deposit rate. 

Graph of deposit rate (3):
<img src="https://github.com/zhouyu59/Topic-Modelingn-Using-Earning-Call-Transcripts-and-BERT/assets/124629778/7988d780-8675-464c-9b3f-293a4b62f0ad" width="500">


Graph of VIX (4):
<img src="https://github.com/zhouyu59/Topic-Modelingn-Using-Earning-Call-Transcripts-and-BERT/assets/124629778/9191f885-93db-4574-add6-286272841134" width="500">


Both graphs peak at 2008 and 2020.

Please check the notebook and function folder to know the whole pipeline and the detailed implementation.

Citation:
1. https://www2.deloitte.com/ie/en/pages/covid-19/articles/impact-COVID-19-insurance-industry.html
2. https://www.pwc.com/jg/en/issues/covid-19/covid-19-and-insurance-industry.pdf
3. https://libertystreeteconomics.newyorkfed.org/2023/04/deposit-betas-up-up-and-away/
4. https://en.wikipedia.org/wiki/VIX#/media/File:CBOE_Volatlity_Index,_VIX.png



