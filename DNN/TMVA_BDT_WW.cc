#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"
#include <vector>
#include "TVector2.h"
#include "TLorentzVector.h"
#include "Math/Vector4Dfwd.h"
#include "Math/GenVector/LorentzVector.h"
#include "Math/GenVector/PtEtaPhiM4D.h"
#include <iostream>
#include <TMath.h>
#include <math.h>

#include "Math/Point3D.h"
#include "Math/Vector3D.h"
#include "Math/Vector4D.h"
#include "Math/Rotation3D.h"
#include "Math/EulerAngles.h"
#include "Math/AxisAngle.h"
#include "Math/Quaternion.h"
#include "Math/RotationX.h"
#include "Math/RotationY.h"
#include "Math/RotationZ.h"
#include "Math/RotationZYX.h"
#include "Math/LorentzRotation.h"
#include "Math/Boost.h"
#include "Math/BoostX.h"
#include "Math/BoostY.h"
#include "Math/BoostZ.h"
#include "Math/Transform3D.h"
#include "Math/Plane3D.h"
#include "Math/VectorUtil.h"
#include "TMatrixD.h"
#include "TVectorD.h"
#include "TMath.h"

#include "TFile.h"
#include "TTree.h"
#include "TString.h"
#include "TSystem.h"
#include "TROOT.h"
#include "TStopwatch.h"

#include "TMVA/Tools.h"
#include "TMVA/Reader.h"
#include "TMVA/MethodCuts.h"



class TMVA_WW: public multidraw::TTreeFunction {
public:
  TMVA_WW(char const* name);

  char const* getName() const override { return "TMVA_WW"; }
  TTreeFunction* clone() const override { return new TMVA_WW(name_.c_str()); }

  unsigned getNdata() override { return 1; }
  double evaluate(unsigned) override;

protected:

  std::string name_;
  void bindTree_(multidraw::FunctionLibrary&) override;

  UIntValueReader*   nLepton{};
  UIntValueReader*   nCleanJet{};
  IntArrayReader*   Lepton_pdgId{};
  FloatArrayReader* Lepton_pt{};
  FloatArrayReader* Lepton_eta{};
  FloatArrayReader* Lepton_phi{};
  FloatArrayReader* CleanJet_pt{};
  FloatArrayReader* CleanJet_eta{};
  FloatArrayReader* CleanJet_phi{};
  FloatArrayReader* Jet_qgl{};
  FloatValueReader* metpt{};
  FloatValueReader* metphi{};
  FloatValueReader* mjj{};
  FloatValueReader* mll{};
  FloatValueReader* ptll{};
  FloatValueReader* detajj{};
  FloatValueReader* dphill{};
  FloatValueReader* dphijjmet{};
  FloatValueReader* dphilljj{};
  FloatValueReader* mti{};
  FloatValueReader* mtw1{};
  FloatValueReader* mtw2{};
  FloatValueReader* drll{};
  FloatValueReader* mpmet{};
  FloatValueReader* mth{};
  FloatValueReader* PuppiMET_pt{};
  FloatValueReader* PuppiMET_phi{};
  IntArrayReader* CleanJet_jetIdx{};
  FloatArrayReader* Jet_btagDeepFlavB{};
};


TMVA_WW::TMVA_WW(char const* name) :
  TTreeFunction()
{
  name_ = name;
}

double
TMVA_WW::evaluate(unsigned)
{


  std::map<std::string,int> Use;
  Use["BDT"] = 1;
  Use["BDT1"] = 1;
  Use["BDTG4SK01F07"] = 1;
  Use["BDTG4SK01"] = 1;
  Use["BDTG4F07"] = 1;
  Use["BDT2"]  = 1;
  Use["BDTG4C3"] = 1;
  Use["BDTB"]   = 1;
  Use["BDTB2"]   = 1;
  Use["BDTB3"]  = 1;
  Use["BDTG4D3"]       = 1;
  Use["LikelihoodKDE"] = 1;
  Use["Likelihood"] = 1;

  unsigned njet = *nCleanJet->Get();


  float Jet_btagDeepFlavB_CleanJet_jetIdx_0_;
  float Jet_btagDeepFlavB_CleanJet_jetIdx_1_;
  if (njet==0){

  }else if (njet == 1){
    int jetIdx0 = CleanJet_jetIdx->At(0);
    Jet_btagDeepFlavB_CleanJet_jetIdx_0_ = jetIdx0 >= 0 ? Jet_btagDeepFlavB->At(jetIdx0) : 0.0;
  }
  else {
    int jetIdx0 = CleanJet_jetIdx->At(0);
    int jetIdx1 = CleanJet_jetIdx->At(1);
    Jet_btagDeepFlavB_CleanJet_jetIdx_0_ = jetIdx0 >= 0 ? Jet_btagDeepFlavB->At(jetIdx0) : 0.0;
    Jet_btagDeepFlavB_CleanJet_jetIdx_1_ = jetIdx1 >= 0 ? Jet_btagDeepFlavB->At(jetIdx1) : 0.0;
  }
  


  float dphill_user{*dphill->Get()};
  float drll_user{*drll->Get()};
  float lep1eta_user = Lepton_eta->At(0);
  float lep2eta_user = Lepton_eta->At(1);
  float lep1phi_user = Lepton_phi->At(0);
  float lep2phi_user = Lepton_phi->At(1);
  float lep1pt_user = Lepton_pt->At(0);
  float lep2pt_user = Lepton_pt->At(1);
  float puppimet_pt_user{*PuppiMET_pt->Get()};
  float puppimet_phi_user{*PuppiMET_phi->Get()};
  float mth_user{*mth->Get()};
  float mtw1_user{*mtw1->Get()};
  float mtw2_user{*mtw2->Get()};
  float mpmet_user{*mpmet->Get()};
  float ptll_user{*ptll->Get()};
  float mll_user{*mll->Get()};
  float btag_user = (float)Jet_btagDeepFlavB_CleanJet_jetIdx_0_;
  float btag_user_1 = (float)Jet_btagDeepFlavB_CleanJet_jetIdx_1_;
  
  TMVA::Reader *reader = new TMVA::Reader( "!Color:Silent" );

  reader->AddVariable("dphill", &dphill_user);
  reader->AddVariable("drll", &drll_user);
  reader->AddVariable("lep1eta", &lep1eta_user);
  reader->AddVariable("lep2eta", &lep2eta_user);
  reader->AddVariable("lep1phi", &lep1phi_user);
  reader->AddVariable("lep2phi", &lep2phi_user);
  reader->AddVariable("lep1pt", &lep1pt_user);
  reader->AddVariable("lep2pt", &lep2pt_user);
  reader->AddVariable("PuppiMET_pt", &puppimet_pt_user);
  reader->AddVariable("PuppiMET_phi", &puppimet_phi_user);
  reader->AddVariable("mth", &mth_user);
  reader->AddVariable("mtw1", &mtw1_user);
  reader->AddVariable("mtw2", &mtw2_user);
  reader->AddVariable("mpmet", &mpmet_user);
  reader->AddVariable("ptll", &ptll_user);
  reader->AddVariable("mll", &mll_user);
  reader->AddVariable("btagDeepFlavB", &btag_user);
  reader->AddVariable("btagDeepFlavB_1", &btag_user_1);

  //TString dir    = "/afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/WW/Full2016_v7/DNN/dataset/weights/";
  TString dir    = "/afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/WW/Full2016_v7/WWj_Full2016_v7/DNN/dataset_for_BDT/weights/";
  TString prefix = "TMVAClassification";

  TString methodName = TString(name_) + TString(" method");
  TString weightfile = dir + prefix + TString("_") + TString(name_) + TString(".weights.xml");
  reader->BookMVA( methodName, weightfile );


  return reader->EvaluateMVA(methodName);


}

void
TMVA_WW::bindTree_(multidraw::FunctionLibrary& _library)
{
  _library.bindBranch(nLepton, "nLepton");
  _library.bindBranch(nCleanJet, "nCleanJet");
  _library.bindBranch(Lepton_pdgId, "Lepton_pdgId");
  _library.bindBranch(Lepton_pt, "Lepton_pt");
  _library.bindBranch(Lepton_eta, "Lepton_eta");
  _library.bindBranch(Lepton_phi, "Lepton_phi");
  _library.bindBranch(CleanJet_pt, "CleanJet_pt");
  _library.bindBranch(CleanJet_eta, "CleanJet_eta");
  _library.bindBranch(CleanJet_phi, "CleanJet_phi");
  _library.bindBranch(metpt, "MET_pt");
  _library.bindBranch(metphi, "MET_phi");
  _library.bindBranch(Jet_qgl, "Jet_qgl");
  _library.bindBranch(mjj, "mjj");
  _library.bindBranch(mll, "mll");
  _library.bindBranch(ptll, "ptll");
  _library.bindBranch(detajj, "detajj");
  _library.bindBranch(dphill, "dphill");
  _library.bindBranch(dphijjmet, "dphijjmet");
  _library.bindBranch(dphilljj, "dphilljetjet");
  _library.bindBranch(PuppiMET_pt, "PuppiMET_pt");
  _library.bindBranch(PuppiMET_phi, "PuppiMET_phi");
  _library.bindBranch(mti, "mTi");
  _library.bindBranch(mth, "mth");
  _library.bindBranch(mtw1, "mtw2");
  _library.bindBranch(mtw2, "mtw1");
  _library.bindBranch(drll, "drll");
  _library.bindBranch(mpmet, "mpmet");
  _library.bindBranch(Jet_btagDeepFlavB,"Jet_btagDeepFlavB");
  _library.bindBranch(CleanJet_jetIdx,"CleanJet_jetIdx");
}
