# Run HiggsHelicityFitModel using Combine

The following instructions must be run to use the model with combine. The package HiggsAnalysis is needed.

First, copy the model file in HiggsAnalysis/CombinedLimit/python. Then:

```
pushd datacards

combineCards.py hww2l2v_13TeV_WP50_sr_0j/mll-mth/datacard.txt hww2l2v_13TeV_top_0j/events/datacard.txt hww2l2v_13TeV_dytt_0j/events/datacard.txt hww2l2v_13TeV_WW_0j/events/datacard.txt > datacards_combined.txt
```

Construct helicity model:

```
text2workspace.py datacard_combined.txt -m 125 -P HiggsAnalysis.CombinedLimit.HiggsHelicity:higgshelicity --PO doFitFractions -o datacard_combined.root

or 

text2workspace.py datacard_combined.txt -m 125 -P HiggsAnalysis.CombinedLimit.HiggsHelicity:higgshelicity --PO doFitXsec -o datacard_combined.root

or 

text2workspace.py datacard_combined.txt -m 125 -P HiggsAnalysis.CombinedLimit.HiggsHelicity:higgshelicity --PO doInter -o datacard_combined.root

or 

text2workspace.py datacard_combined.txt -m 125 -P HiggsAnalysis.CombinedLimit.HiggsHelicity:higgshelicity --PO doIntXsec -o datacard_combined.root
```

For large combinations, useful:

```
ulimit -Ss 131072
```

Fit:

```
combineTool.py -M Impacts -d datacards/datacard_combined.root -m 125 -t -1 --X-rtd MINIMIZER_analytic --cminDefaultMinimizerStrategy=0 --doInitialFit

combineTool.py -M Impacts -d datacards/datacard_combined.root -m 125 -t -1 --X-rtd MINIMIZER_analytic --cminDefaultMinimizerStrategy=0 --doFits --job-mode=interactive --parallel=10

combineTool.py -M Impacts -d datacards/datacard_combined.root -m 125 -t -1 --X-rtd MINIMIZER_analytic --cminDefaultMinimizerStrategy=0 -o impacts.json

plotImpacts.py -i impacts.json -o impacts --POI FLL_Fit

plotImpacts.py -i impacts.json -o impacts --POI FTT_Fit

combine -M MultiDimFit --algo grid --points 1000 --setParameters r_LL=1,r_TT=1 --redefineSignalPOIs r_LL,r_TT --setParameterRanges r_LL=0,4:r_TT=0,4 -t -1 --X-rtd MINIMIZER_analytic --cminDefaultMinimizerStrategy=0 --verbose 1 -d datacards_HWW_2018/datacard_combined_RF_WW.root -m 125

root higgsCombineTest.MultiDimFit.mH125.root higgsCombineTest.MultiDimFit.mH125.root draw2D.cxx\(\"r_LL\",\"r_TT\",\"r_LL\",\"r_TT\"\)
```



# Run WWHelicityFitModel using Combine

The following instructions must be run to use the model with combine. The package HiggsAnalysis is needed.

First, copy the model file in HiggsAnalysis/CombinedLimit/python. Then:

```
pushd datacards

combineCards.py WW_SR/CosThetaP_CosThetaM/datacard.txt .... > datacard_combined.txt

text2workspace.py datacard_combined.txt -m 125 -P HiggsAnalysis.CombinedLimit.WWHelicityFitModel:WWHelicityModel --PO FLL_MC=0.3743 --PO FTT_MC=0.1509 --PO FTL_MC=0.2378 --PO FLT_MC=0.2378 --PO ModCase=MCFractions -o datacard_combined.root

combineTool.py -M Impacts -d datacards/datacard_combined.root -m 125 -t -1 --rMin=-6 --rMax=10 --X-rtd MINIMIZER_analytic --cminDefaultMinimizerStrategy=0 --setParameters FLL_Fit=0.3743,FTT_Fit=0.1509,FLT_Fit=0.2378,FTL_Fit=0.2378 --doInitialFit
```



