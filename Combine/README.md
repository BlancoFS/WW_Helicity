# Run WWHelicityFitModel using Combine

The following instructions must be run to use the model with combine. The package HiggsAnalysis is needed.

First, copy the model file in HiggsAnalysis/CombinedLimit/python. Then:

```
pushd datacards

combineCards.py WW_SR/CosThetaP_CosThetaM/datacard.txt .... > datacard_combined.txt

text2workspace.py datacard_combined.txt -m 125 -P HiggsAnalysis.CombinedLimit.WWHelicityFitModel:WWHelicityModel --PO FLL_MC=0.3743 --PO FTT_MC=0.1509 --PO FTL_MC=0.2378 --PO FLT_MC=0.2378 --PO ModCase=MCFractions -o datacard_combined.root

combineTool.py -M Impacts -d datacards/datacard_combined.root -m 125 -t -1 --rMin=-6 --rMax=10 --X-rtd MINIMIZER_analytic --cminDefaultMinimizerStrategy=0 --setParameters FLL_Fit=0.3743,FTT_Fit=0.1509,FLT_Fit=0.2378,FTL_Fit=0.2378 --doInitialFit
```



