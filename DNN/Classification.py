#!/usr/bin/env python
from ROOT import TMVA, TFile, TTree, TCut, TChain
from subprocess import call
from os.path import isfile
import ROOT

# Setup TMVA
def runJob():
    TMVA.Tools.Instance()
    TMVA.PyMethodBase.PyInitialize()

    inputfile_0 = ROOT.TFile.Open("/afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/WW/Full2016_v7/WW_helicity/DNN/MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7__WPWPVarsDNN/nanoLatino_WWTo2L2NuHerwigPS__part0.root")
    inputfile_1 = ROOT.TFile.Open("/afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/WW/Full2016_v7/WW_helicity/DNN/MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7__WPWPVarsDNN/nanoLatino_WWTo2L2NuHerwigPS__part1.root")
    inputfile_2 = ROOT.TFile.Open("/afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/WW/Full2016_v7/WW_helicity/DNN/MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7__WPWPVarsDNN/nanoLatino_WWTo2L2NuHerwigPS__part2.root")
    inputfile_3 = ROOT.TFile.Open("/afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/WW/Full2016_v7/WW_helicity/DNN/MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7__WPWPVarsDNN/nanoLatino_WWTo2L2NuHerwigPS__part3.root")

    tree_0 = inputfile_0.Get("Events")
    tree_1 = inputfile_1.Get("Events")
    tree_2 = inputfile_2.Get("Events")
    tree_3 = inputfile_3.Get("Events")

    dataloader = TMVA.DataLoader('dataset')
    dataloader.AddSignalTree(tree_0)
    dataloader.AddSignalTree(tree_1)

    dataloader.AddBackgroundTree(tree_2)
    dataloader.AddBackgroundTree(tree_3)

    dataloader.SetSignalWeightExpression("Weight_LL")
    dataloader.SetBackgroundWeightExpression("Weight_Bkg")

    output = TFile.Open('TMVA_DNN_2.root', 'RECREATE')
    

    factory = TMVA.Factory('TMVAClassification', output,
            '!V:!Silent:Color:DrawProgressBar:AnalysisType=Classification')

    dataloader.AddVariable('mll')
    dataloader.AddVariable('lep1pt')
    dataloader.AddVariable('lep2pt')
    dataloader.AddVariable('lep1eta')
    dataloader.AddVariable('lep2eta')
    dataloader.AddVariable('lep1phi')
    dataloader.AddVariable('lep2phi')
    dataloader.AddVariable('drll')
    dataloader.AddVariable('ptll')
    dataloader.AddVariable('mtw1')
    dataloader.AddVariable('mtw2')
    dataloader.AddVariable('dphill')
    dataloader.AddVariable('costheta')
    dataloader.AddVariable('metpt')
    dataloader.AddVariable('metphi')
    dataloader.AddVariable('mpmet')
    dataloader.AddVariable('mth')
    dataloader.AddVariable('rap1')
    dataloader.AddVariable('rap2')
    dataloader.AddVariable('dphilmet')
    dataloader.AddVariable('dphilmet1')
    dataloader.AddVariable('dphilmet2')

    #dataloader.AddVariable('D_00TT')
    #dataloader.AddVariable('D_00T0')
    #dataloader.AddVariable('D_TTT0')

    #dataloader.AddVariable('P_00')
    #dataloader.AddVariable('P_TT')

    dataloader.PrepareTrainingAndTestTree(TCut(""),'SplitMode=Random::SplitSeed=10:NormMode=EqualNumEvents')

    factory.BookMethod(dataloader, TMVA.Types.kBDT, "BDT", "!H:!V:NTrees=500:MinNodeSize=0.5%:MaxDepth=3:BoostType=AdaBoost:AdaBoostBeta=0.1:SeparationType=GiniIndex:nCuts=500" );
    factory.BookMethod(dataloader, TMVA.Types.kBDT, "BDT1", "!H:!V:NTrees=1000:MinNodeSize=0.5%:MaxDepth=2:BoostType=AdaBoost:AdaBoostBeta=0.1:SeparationType=GiniIndex:nCuts=1000" );
    factory.BookMethod(dataloader, TMVA.Types.kBDT, "BDT2", "!H:!V:NTrees=800:MinNodeSize=0.5%:MaxDepth=1:BoostType=AdaBoost:AdaBoostBeta=0.2:SeparationType=GiniIndex:nCuts=1000" );
    factory.BookMethod(dataloader, TMVA.Types.kBDT, "BDTG4D3",   "!H:!V:NTrees=500:MinNodeSize=1.5%:BoostType=Grad:Shrinkage=0.05:UseBaggedBoost:GradBaggingFraction=0.5:nCuts=500:MaxDepth=3" );
    factory.BookMethod(dataloader, TMVA.Types.kBDT, "BDTG4C3", "!H:!V:NTrees=500:MinNodeSize=1.5%:BoostType=Grad:Shrinkage=0.05:UseBaggedBoost:GradBaggingFraction=0.5:nCuts=300:MaxDepth=2" );
    factory.BookMethod(dataloader, TMVA.Types.kBDT, "BDTG4SK01",   "!H:!V:NTrees=500:MinNodeSize=1.5%:BoostType=Grad:Shrinkage=0.01:UseBaggedBoost:GradBaggingFraction=0.5:nCuts=500:MaxDepth=2" );
    factory.BookMethod(dataloader, TMVA.Types.kBDT, "BDTG4F07"    ,   "!H:!V:NTrees=500:MinNodeSize=1.5%:BoostType=Grad:Shrinkage=0.05:UseBaggedBoost:GradBaggingFraction=0.7:nCuts=500:MaxDepth=2" );
    factory.BookMethod(dataloader, TMVA.Types.kBDT, "BDTG4SK01F07",   "!H:!V:NTrees=500:MinNodeSize=1.5%:BoostType=Grad:Shrinkage=0.01:UseBaggedBoost:GradBaggingFraction=0.7:nCuts=500:MaxDepth=2" );
    factory.BookMethod(dataloader, TMVA.Types.kBDT, "BDTB",   "!H:!V:NTrees=400:BoostType=Bagging:SeparationType=GiniIndex:nCuts=20" );
    factory.BookMethod(dataloader, TMVA.Types.kBDT, "BDTB2",   "!H:!V:NTrees=800:BoostType=Bagging:SeparationType=GiniIndex:nCuts=50" );
    factory.BookMethod(dataloader, TMVA.Types.kBDT, "BDTB3",   "!H:!V:NTrees=1000:BoostType=Bagging:SeparationType=GiniIndex:nCuts=100" );

    factory.BookMethod(dataloader, TMVA.Types.kMLP, "MLP", "!H:!V:NeuronType=tanh:VarTransform=N:NCycles=100:HiddenLayers=N+5:TestRate=5:!UseRegulator");
    factory.BookMethod(dataloader, TMVA.Types.kLikelihood, "Likelihood", "H:!V:TransformOutput:PDFInterpol=Spline2:NSmoothSig[0]=20:NSmoothBkg[0]=20:NSmoothBkg[1]=10:NSmooth=1:NAvEvtPerBin=50" )
    factory.BookMethod(dataloader, TMVA.Types.kLikelihood, "LikelihoodKDE", "!H:!V:!TransformOutput:PDFInterpol=KDE:KDEtype=Gauss:KDEiter=Adaptive:KDEFineFactor=0.3:KDEborder=None:NAvEvtPerBin=50" )


    inputLayoutString = "InputLayout=1|1|22"
    batchLayoutString= "BatchLayout=1|128|22"
    layoutString = "Layout=DENSE|150|TANH,DENSE|75|TANH,DENSE|50|TANH,DENSE|25|TANH,DENSE|1|LINEAR"
    training1 = "LearningRate=1e-3,Momentum=0.9,ConvergenceSteps=10,BatchSize=128,TestRepetitions=1,MaxEpochs=30,WeightDecay=1e-4,Regularization=None,Optimizer=ADAM,ADAM_beta1=0.9,ADAM_beta2=0.999,ADAM_eps=1.E-7,DropConfig=0.0+0.0+0.0+0."
    training2 = "LearningRate=1e-3,Momentum=0.9,ConvergenceSteps=10,BatchSize=128,TestRepetitions=1,MaxEpochs=20,WeightDecay=1e-4,Regularization=NoneOptimizer=SGD,DropConfig=0.0+0.0+0.0+0."
    trainingStrategyString = "TrainingStrategy="
    trainingStrategyString = trainingStrategyString + training1 + "|" + training2

    dnnOptions = "!H:V:ErrorStrategy=CROSSENTROPY:VarTransform=G:WeightInitialization=XAVIER"

    dnnOptions = dnnOptions + ":" + inputLayoutString + ":" + batchLayoutString + ":" + layoutString + ":" + trainingStrategyString 

    dnnOptions = dnnOptions + ":Architecture=CPU"

    dnnMethodName = "DNN_CPU"
 
    factory.BookMethod(dataloader, TMVA.Types.kDL, dnnMethodName, dnnOptions);


    # Run training, test and evaluation
    factory.TrainAllMethods()
    factory.TestAllMethods()
    factory.EvaluateAllMethods()

    output.Close()

if __name__ == "__main__":
    runJob()
