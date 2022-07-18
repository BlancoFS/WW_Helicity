#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"
#include "TSystem.h"
#include "iostream"
#include "vector"
#include "TLorentzVector.h"
#include "TMath.h"
#include "momemta/ConfigurationReader.h"
#include "momemta/MoMEMta.h"
#include "momemta/Types.h"
#include "TSystem.h"
#include "TString.h"

using LorentzVectorM = ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiM4D<float>>;

using namespace momemta;

void normalizeInput(LorentzVector& p4) {
  if (p4.M() > 0)
    return;

  // Increase the energy until M is positive                                                                                                                                                                                                
  p4.SetE(p4.P());
  while (p4.M2() < 0) {
    double delta = p4.E() * 1e-5;
    p4.SetE(p4.E() + delta);
  };
}

float RecoMoMEMta(float nCleanJet, float nLepton, float PuppiMet_pt, float PuppiMet_phi, float Lepton_pt0, float Lepton_pt1, float Lepton_phi0, float Lepton_phi1, float Lepton_eta0, float Lepton_eta1,float CleanJet_pt0, float CleanJet_pt1, float CleanJet_phi0, float CleanJet_phi1, float CleanJet_eta0, float CleanJet_eta1, float Lepton_pdg0, float Lepton_pdg1){

  
  logging::set_level(logging::level::off);

  //Initializing 4-vectors                                                                                                                                                           
  TLorentzVector L1(0.,0.,0.,0.);
  TLorentzVector L2(0.,0.,0.,0.);
  TLorentzVector LL(0.,0.,0.,0.);
  TLorentzVector NuNu(0.,0.,0.,0.);
  TLorentzVector J1(0.,0.,0.,0.);
  TLorentzVector J2(0.,0.,0.,0.);

  //Getting some values to select the events                                                                                                                                         
  unsigned ncleanjet{*nCleanJet->Get()};
  unsigned nlep{*nLepton->Get()};
  float Pmet_pt{*PuppiMET_pt->Get()};
  float Pmet_phi{*PuppiMET_phi->Get()};

  //Conditions to select the event                                                                                                                                                   
  if(nlep>1){

    //STEP-1                                                                                                                                                                         
    //4-vectors of the leptons                                                                                                                                                       
    //Select one electron and one muon                                                                                                                                               
    int muons = 0;
    int electrons = 0;
    int lep1 = 0;
    int lep2 = 0;

    // Loop over muons and electrons                                                                                                                                                 
    for (unsigned int ilep = 0; ilep<nlep; ilep++){
      if (abs(Lepton_pdgId->At(ilep)) == 13){
        ++muons;
        if (muons == 1 && Lepton_pt->At(ilep) > 13){
          L1.SetPtEtaPhiM(Lepton_pt->At(ilep), Lepton_eta->At(ilep), Lepton_phi->At(ilep), 0.0); //Muon                                                                              
          lep1 = Lepton_pdgId->At(ilep);
        }
      }
      if (abs(Lepton_pdgId->At(ilep)) == 11){
        ++electrons;
        if (electrons == 1 && Lepton_pt->At(ilep) > 13){
          L2.SetPtEtaPhiM(Lepton_pt->At(ilep), Lepton_eta->At(ilep), Lepton_phi->At(ilep), 0.0); //Electron                                                                          
          lep2 = Lepton_pdgId->At(ilep);
        }
      }
    }

    if (muons<1 || electrons<1){
      return -9999; //If there is not an electron and a muon, return -9999                                                                                                          
    }
    
    
    LL = L1 + L2;

    double nunu_px = Pmet_pt*cos(Pmet_phi);
    double nunu_py = Pmet_pt*sin(Pmet_phi);
    double nunu_pz = LL.Pz();
    double nunu_m = 30.0; //Why 30? --> https://indico.cern.ch/event/850505/contributions/3593915/                                                                                  

    double nunu_e = sqrt(nunu_px*nunu_px + nunu_py*nunu_py + nunu_pz*nunu_pz + nunu_m*nunu_m);
    NuNu.SetPxPyPzE(nunu_px, nunu_py, nunu_pz, nunu_e);
    

    ConfigurationReader configuration_noJet("/afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/WW_leptonic_noJet_ME/WW_leptonic_noJets_2.lua");

    if (lep1 < 0){
      logging::set_level(logging::level::off);
    }else{
      ConfigurationReader configuration_noJet("/afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/WW_leptonic_noJet_ME/WW_leptonic_noJets_mue_2.lua");
    }

    MoMEMta weight_noJet(configuration_noJet.freeze());

    logging::set_level(logging::level::off);

    ParameterSet lua_parameters;
    lua_parameters.set("USE_TF", true);
    lua_parameters.set("USE_PERM", true);

    momemta::Particle lepton1 { "lepton1", LorentzVector(L1.Px(), L1.Py(), L1.Pz(), L1.E()), lep1 }; // muon                                                                      
    momemta::Particle lepton2 { "lepton2", LorentzVector(L2.Px(), L2.Py(), L2.Pz(), L2.E()), lep2 }; // electron                                                                  

    // normalize input for numerical estability                                                                                                                                  
    normalizeInput_WWj(lepton1.p4);
    normalizeInput_WWj(lepton2.p4);

    LorentzVector met_p4 {NuNu.Px(), NuNu.Py(), NuNu.Pz(), NuNu.E()};

    std::vector<std::pair<double, double>> weights_noJet = weight_noJet.computeWeights({lepton1, lepton2}, met_p4);

    double WW = (double)weights_noJet.back().first;

    return WW;
    
    
  }else{
    
    return -9999.;
    
  }

}

