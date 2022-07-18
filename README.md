# WW_Helicity
Analysis for double polarization of H->W+W- and W+W- production at the LHC with CMS in the fully leptonic decay channel


First of all, let's start building the programming enviroment. The next part explain the instructions to execute the code. 

First, log in gridui:

```ssh -Y ***@lxplus.cern.ch -o ServerAliveInterval=240```


Set CMS enviroment for the first time:

```
bash -l

source /cvmfs/cms.cern.ch/cmsset_default.sh

export SCRAM_ARCH=slc7_amd64_gcc700

cmsrel CMSSW_10_6_10
```


Enter CMS eviroment on gridui:

```
bash -l

source /cvmfs/cms.cern.ch/cmsset_default.sh

cd CMSSW_10_6_10/src

cmsenv
```

Compile code:

```scram b -j 8```


Get some code from gitHub:

```git clone https://github.com/BlancoFS/...```


Change condor scehduler if it's not running properly: 

```
export _condor_SCHEDD_HOST="bigbird02.cern.ch"
```


## Run code:


Run and make plots with LatinoAnalysis tools:

```
mkShapesMulti.py --pycfg=configuration.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=testmatch

mkShapesMulti.py --pycfg=configuration.py --doHadd=1 --batchSplit=Samples,Files --doNotCleanup --nThreads=8

mkPlot.py --pycfg=configuration.py --inputFile=rootFile/plots_WW_2016.root --minLogC=0.01 --minLogCratio=0.01 --maxLogC=1000 --maxLogCratio=1000 --showIntegralLegend=1

Plot_Sig_Bkg.py --pycfg=configuration.py --inputFile=rootFile/plots_WW_2016.root

```

## Useful tools

How to copy files from cloud server to computer, some ways:

```
scp aaa@server.com:folder/file  local/directory
rsync -av aaa@server.com:folder/file  local/directory
```

## Make datacards and combine 

The datacards should be made in your work directory. Then, the datacard.txt has to be copied to the combine datacards folder.

```
mkDatacards.py --pycfg=configuration.py --inputFile=rootFile/plots_WW_2016.root
```

Now, in the combine folder after coping the datacard:

```
pushd datacards

combineCards.py VBF/events/datacard.txt DY/events/datacard.txt top/events/datacard.txt ggF/events/datacard.txt WW/events/datacard.txt > datacard_combined.txt

text2workspace.py datacard_combined.txt -m 125

text2workspace.py datacard_combined.txt -m 125 -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel --PO 'map=.*/qqH_hww:r_qqH_hww[1,-10,10]' --PO 'map=.*/ggH_hww:r_ggH_hww[1,-10,10]'

popd
```

## Impact plots (Asimov dataset)

```
combineTool.py -M Impacts -d datacards/datacard_combined.root -m 125 -t -1 --rMin=-6 --rMax=10 --X-rtd MINIMIZER_analytic --cminDefaultMinimizerStrategy=0 --setParameters r_WLWL=1 --redefineSignalPOIs r_WLWL --doInitialFit 

combineTool.py -M Impacts -d datacards/datacard_combined.root -m 125 -t -1 --rMin=-6 --rMax=10 --X-rtd MINIMIZER_analytic --cminDefaultMinimizerStrategy=0 --setParameters r_WLWL=1 --redefineSignalPOIs r_WLWL --doFits --job-mode=interactive --parallel=10

combineTool.py -M Impacts -d datacards/datacard_combined.root -m 125 -t -1 --rMin=-6 --rMax=10 --X-rtd MINIMIZER_analytic --cminDefaultMinimizerStrategy=0 --setParameters r_WLWL=1 --redefineSignalPOIs r_WLWL -o impacts.json

plotImpacts.py -i impacts.json -o impacts
```

## Compute significance

```
combineTool.py -M Significance -d datacards/datacard_combined.root -m 125 -t -1 --rMin=-6 --rMax=10 --X-rtd MINIMIZER_analytic --cminDefaultMinimizerStrategy=0 --setParameters r_WLWL=1 --redefineSignalPOIs r_WLWL
```
