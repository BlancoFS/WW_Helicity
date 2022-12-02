#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"
#include "TSystem.h"
#include "iostream"
#include "vector"
#include "TLorentzVector.h"
#include "TMath.h"
#include "TSystem.h"
#include <map>
#include "TString.h"

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


/**
###################################################
##                                               ##
### COMPUTE POLARIZED FRACTIONS FOR WW ANALYSIS ### 
##                                               ##
###################################################
**/

class DoPolarizationWeight : public multidraw::TTreeFunction {
public:
  //Class Constructor 
  DoPolarizationWeight(char const* name);
  //Class Destructor 
  ~DoPolarizationWeight() {
  }
  //Functions from Multidraw namespace (TTreeFunction class)
  char const* getName() const override {return "DoPolarizationWeight"; }
  TTreeFunction* clone() const override {return new DoPolarizationWeight(name_.c_str());}
  unsigned getNdata() override {return 1; }
  //This function will return the required value
  double evaluate(unsigned) override;

protected:
  void bindTree_(multidraw::FunctionLibrary&) override;
  std::string name_;

  FloatArrayReader* GenPart_pt{};
  FloatArrayReader* GenPart_eta{};
  FloatArrayReader* GenPart_phi{};
  FloatArrayReader* GenPart_mass{};
  IntArrayReader* GenPart_pdgId{};
  IntArrayReader* GenPart_status{};
  IntArrayReader* GenPart_genPartIdxMother{};

private:

  Double_t LHCsqrts_= 13., mh_= 125.;
  
};

DoPolarizationWeight::DoPolarizationWeight(char const* name):
  TTreeFunction()
{
  name_ = name;
}

double
DoPolarizationWeight::evaluate(unsigned)
{
   
  ROOT::Math::PtEtaPhiEVector genWp;
  ROOT::Math::PtEtaPhiEVector genWm;
  ROOT::Math::PtEtaPhiEVector genlp;
  ROOT::Math::PtEtaPhiEVector genlm;
  ROOT::Math::PtEtaPhiEVector gennup;
  ROOT::Math::PtEtaPhiEVector gennum;
  ROOT::Math::PtEtaPhiEVector genH;
  TLorentzVector vector_lp; 
  TLorentzVector vector_lm; 
  TLorentzVector vector_nup;
  TLorentzVector vector_num;
  TLorentzVector vector_Wp; 
  TLorentzVector vector_Wm;
  
  TLorentzVector WP;
  TLorentzVector WM;
  TLorentzVector H;
  
  Double_t cL = 1.0;
  Double_t cR = 1.0;
  Double_t MW = 8.041900e+01;
  Double_t WW = 2.047600e+00;
  Double_t ghWW = 1.0;
    
  Int_t number_elec = 0;
  Int_t number_muon = 0;
  Int_t number_tau = 0;
  
  Int_t pos_wp = 999;
  Int_t pos_wm = 999;
  
  Int_t mother_pos = 0;

  unsigned int nGen = GenPart_pt->GetSize();
    
  for (unsigned int p = 0; p < nGen; p++){
  
    mother_pos = GenPart_genPartIdxMother->At(p);
    //if (GenPart_pdgId->At(p)==11 && GenPart_status->At(p)==1 && GenPart_pdgId->At(mother_pos)==-24){
    if (GenPart_pdgId->At(p)==11 && GenPart_pdgId->At(mother_pos)==-24 && GenPart_pdgId->At(GenPart_genPartIdxMother->At(mother_pos))!=15){

      pos_wm = mother_pos;
      number_elec++;
      vector_lm.SetPtEtaPhiM(GenPart_pt->At(p), GenPart_eta->At(p), GenPart_phi->At(p), 0.0);
      genlm.SetCoordinates(GenPart_pt->At(p), GenPart_eta->At(p), GenPart_phi->At(p), vector_lm.E());

      //}else if (GenPart_pdgId->At(p)==-11 && GenPart_status->At(p)==1 && GenPart_pdgId->At(mother_pos)==24){
    }else if (GenPart_pdgId->At(p)==-11 && GenPart_pdgId->At(mother_pos)==24 && GenPart_pdgId->At(GenPart_genPartIdxMother->At(mother_pos))!=-15){

      pos_wp = mother_pos;
      number_elec++;
      vector_lp.SetPtEtaPhiM(GenPart_pt->At(p), GenPart_eta->At(p), GenPart_phi->At(p), 0.0);
      genlp.SetCoordinates(GenPart_pt->At(p), GenPart_eta->At(p), GenPart_phi->At(p), vector_lp.E());    

      //}else if (GenPart_pdgId->At(p)==13 && GenPart_status->At(p)==1 && GenPart_pdgId->At(mother_pos)==-24){
    }else if (GenPart_pdgId->At(p)==13 && GenPart_pdgId->At(mother_pos)==-24 && GenPart_pdgId->At(GenPart_genPartIdxMother->At(mother_pos))!=15){

      pos_wm = mother_pos;
      number_muon++;
      vector_lm.SetPtEtaPhiM(GenPart_pt->At(p), GenPart_eta->At(p), GenPart_phi->At(p), 0.0);
      genlm.SetCoordinates(GenPart_pt->At(p), GenPart_eta->At(p), GenPart_phi->At(p), vector_lm.E());

      //}else if (GenPart_pdgId->At(p)==-13 && GenPart_status->At(p)==1 && GenPart_pdgId->At(mother_pos)==24){
    }else if (GenPart_pdgId->At(p)==-13 && GenPart_pdgId->At(mother_pos)==24 && GenPart_pdgId->At(GenPart_genPartIdxMother->At(mother_pos))!=-15){

      pos_wp = mother_pos;
      number_muon++;
      vector_lp.SetPtEtaPhiM(GenPart_pt->At(p), GenPart_eta->At(p), GenPart_phi->At(p), 0.0);
      genlp.SetCoordinates(GenPart_pt->At(p), GenPart_eta->At(p), GenPart_phi->At(p), vector_lp.E());    

    }else if (GenPart_pdgId->At(p)==15 && GenPart_pdgId->At(mother_pos)==-24){

      pos_wm = mother_pos;
      number_tau++;
      vector_lm.SetPtEtaPhiM(GenPart_pt->At(p), GenPart_eta->At(p), GenPart_phi->At(p), 0.0);
      genlm.SetCoordinates(GenPart_pt->At(p), GenPart_eta->At(p), GenPart_phi->At(p), vector_lm.E());

    }else if (GenPart_pdgId->At(p)==-15 && GenPart_pdgId->At(mother_pos)==24){

      pos_wp = mother_pos;
      number_tau++;
      vector_lp.SetPtEtaPhiM(GenPart_pt->At(p), GenPart_eta->At(p), GenPart_phi->At(p), 0.0);
      genlp.SetCoordinates(GenPart_pt->At(p), GenPart_eta->At(p), GenPart_phi->At(p), vector_lp.E());

    }


    // Neutrinos

    
    //if (GenPart_pdgId->At(p)==-12 && GenPart_status->At(p)==1 && GenPart_pdgId->At(mother_pos)==-24){
    if (GenPart_pdgId->At(p)==-12 && GenPart_pdgId->At(mother_pos)==-24 && GenPart_pdgId->At(GenPart_genPartIdxMother->At(mother_pos))!=15){ 

      vector_num.SetPtEtaPhiM(GenPart_pt->At(p), GenPart_eta->At(p), GenPart_phi->At(p), 0.0);
      gennum.SetCoordinates(GenPart_pt->At(p), GenPart_eta->At(p), GenPart_phi->At(p), vector_num.E());

      //}else if (GenPart_pdgId->At(p)==12 && GenPart_status->At(p)==1 && GenPart_pdgId->At(mother_pos)==24){
    }else if (GenPart_pdgId->At(p)==12 && GenPart_pdgId->At(mother_pos)==24 && GenPart_pdgId->At(GenPart_genPartIdxMother->At(mother_pos))!=-15){ 

      vector_nup.SetPtEtaPhiM(GenPart_pt->At(p), GenPart_eta->At(p), GenPart_phi->At(p), 0.0);
      gennup.SetCoordinates(GenPart_pt->At(p), GenPart_eta->At(p), GenPart_phi->At(p), vector_nup.E());    

      //}else if (GenPart_pdgId->At(p)==-14 && GenPart_status->At(p)==1 && GenPart_pdgId->At(mother_pos)==-24){
    }else if (GenPart_pdgId->At(p)==-14 && GenPart_pdgId->At(mother_pos)==-24 && GenPart_pdgId->At(GenPart_genPartIdxMother->At(mother_pos))!=15){ 

      vector_num.SetPtEtaPhiM(GenPart_pt->At(p), GenPart_eta->At(p), GenPart_phi->At(p), 0.0);
      gennum.SetCoordinates(GenPart_pt->At(p), GenPart_eta->At(p), GenPart_phi->At(p), vector_num.E());

      //}else if (GenPart_pdgId->At(p)==14 && GenPart_status->At(p)==1 && GenPart_pdgId->At(mother_pos)==24){
    }else if (GenPart_pdgId->At(p)==14 && GenPart_pdgId->At(mother_pos)==24 && GenPart_pdgId->At(GenPart_genPartIdxMother->At(mother_pos))!=-15){ 

      vector_nup.SetPtEtaPhiM(GenPart_pt->At(p), GenPart_eta->At(p), GenPart_phi->At(p), 0.0);
      gennup.SetCoordinates(GenPart_pt->At(p), GenPart_eta->At(p), GenPart_phi->At(p), vector_nup.E());    

    }else if (GenPart_pdgId->At(p)==-16 && GenPart_pdgId->At(mother_pos)==-24){

      vector_num.SetPtEtaPhiM(GenPart_pt->At(p), GenPart_eta->At(p), GenPart_phi->At(p), 0.0);
      gennum.SetCoordinates(GenPart_pt->At(p), GenPart_eta->At(p), GenPart_phi->At(p), vector_num.E());

    }else if (GenPart_pdgId->At(p)==16 && GenPart_pdgId->At(mother_pos)==24){

      vector_nup.SetPtEtaPhiM(GenPart_pt->At(p), GenPart_eta->At(p), GenPart_phi->At(p), 0.0);
      gennup.SetCoordinates(GenPart_pt->At(p), GenPart_eta->At(p), GenPart_phi->At(p), vector_nup.E());

    }

  } // End loop over particles


  
  // Assign the four-vector of the Ws
  vector_Wp.SetPtEtaPhiM(GenPart_pt->At(pos_wp), GenPart_eta->At(pos_wp), GenPart_phi->At(pos_wp), GenPart_mass->At(pos_wp)); // W plus
  genWp.SetCoordinates(GenPart_pt->At(pos_wp), GenPart_eta->At(pos_wp), GenPart_phi->At(pos_wp), vector_Wp.E());
      
  vector_Wm.SetPtEtaPhiM(GenPart_pt->At(pos_wm), GenPart_eta->At(pos_wm), GenPart_phi->At(pos_wm), GenPart_mass->At(pos_wm)); // W minus
  genWm.SetCoordinates(GenPart_pt->At(pos_wm), GenPart_eta->At(pos_wm), GenPart_phi->At(pos_wm), vector_Wm.E());
  
  
  //if (number_elec!=1 || number_muon!=1 || pos_wp==999 || pos_wm==999){
  //return  -999;
  //}

  if (((number_elec==0 || number_muon==0) && number_tau==0) || pos_wp==999 || pos_wm==999){
    return  -999;
  }

  // Boost over lepton from the Ws reference frame
  // Compute theta star  

  WP = vector_Wp;
  WM = vector_Wm;
  H = WP + WM;
  
  genH.SetCoordinates(H.Pt(), H.Eta(), H.Phi(), H.E());

  
  ROOT::Math::XYZVector hRF;  
  hRF = henH.BoostToCM();
  
  ROOT::Math::XYZVector leppWRF;
  ROOT::Math::XYZVector lepmWRF;
  
  ROOT::Math::XYZVector WpHRF;
  ROOT::Math::XYZVector WmHRF;

  WpHRF = ROOT::Math::VectorUtil::boost(genWp, hRF);
  WmHRF = ROOT::Math::VectorUtil::boost(genWm, hRF);
  
  leppWRF = ROOT::Math::VectorUtil::boost(genlp, WpHRF);
  nupWRF = ROOT::Math::VectorUtil::boost(gennum, WmHRF);
  
  Double_t theta_Wp_star = ROOT::Math::VectorUtil::Angle(leppWRF, genWp);
  Double_t theta_Wm_star = ROOT::Math::VectorUtil::Angle(nupWRF, genWm);

  Double_t cos_Wp_theta_star = ROOT::Math::cos(theta_Wp_star);
  Double_t cos_Wm_theta_star = ROOT::Math::cos(theta_Wm_star);
  Double_t dphill = leppWRF.Phi() - nupWRF.Phi();

  // https://arxiv.org/pdf/2105.07972.pdf
  
  /////////////////////////////////////
  //             |ALL|^2             //
  /////////////////////////////////////
  
  Double_t K = ((H.M()*H.M() - WP.M()*WP.M() - WM.M()*WM.M()) / (2 * WP.M() * WM.M()));
  Double_t P1 = ( (2 * ghWW * WP.M() * WP.M()) / ((WP.M() * WP.M() - MW*MW)*(WP.M() * WP.M() - MW * MW) + WW * WW * MW * MW));
  Double_t P2 = ( (2 * ghWW * WM.M() * WM.M()) / ((WM.M() * WM.M() - MW*MW)*(WM.M() * WM.M() - MW * MW) + WW * WW * MW * MW));
  Double_t ALL2 = 4 * K*K * P1 * P2 * (cL*cL + cR*cR)*(cL*cL + cR*cR) * ROOT::Math::sin(theta_Wp_star)*ROOT::Math::sin(theta_Wp_star) * ROOT::Math::sin(theta_Wm_star)*ROOT::Math::sin(theta_Wm_star);
  
  
  /////////////////////////////////////
  //             |A++|^2             //
  /////////////////////////////////////
  
  Double_t plus1 = cL*cL*cL*cL * (1 + ROOT::Math::cos(theta_Wp_star))*(1 + ROOT::Math::cos(theta_Wp_star)) * (1 + ROOT::Math::cos(theta_Wm_star))*(1 + ROOT::Math::cos(theta_Wm_star));
  Double_t plus2 = cR*cR*cR*cR * (1 - ROOT::Math::cos(theta_Wp_star))*(1 - ROOT::Math::cos(theta_Wp_star)) * (1 - ROOT::Math::cos(theta_Wm_star))*(1 - ROOT::Math::cos(theta_Wm_star));
  Double_t plus3 = cR*cR*cL*cL * (1 + ROOT::Math::cos(theta_Wp_star))*(1 + ROOT::Math::cos(theta_Wp_star)) * (1 - ROOT::Math::cos(theta_Wm_star))*(1 - ROOT::Math::cos(theta_Wm_star));
  Double_t plus4 = cR*cR*cL*cL * (1 - ROOT::Math::cos(theta_Wp_star))*(1 - ROOT::Math::cos(theta_Wp_star)) * (1 + ROOT::Math::cos(theta_Wm_star))*(1 + ROOT::Math::cos(theta_Wm_star));
  
  Double_t App2 = P1 * P2 * (plus1 + plus2 + plus3 + plus4);
  
  /////////////////////////////////////
  //             |A--|^2             //
  /////////////////////////////////////
  
  Double_t minus1 = cL*cL*cL*cL * (1 - ROOT::Math::cos(theta_Wp_star))*(1 - ROOT::Math::cos(theta_Wp_star)) * (1 - ROOT::Math::cos(theta_Wm_star))*(1 - ROOT::Math::cos(theta_Wm_star));
  Double_t minus2 = cR*cR*cR*cR * (1 + ROOT::Math::cos(theta_Wp_star))*(1 + ROOT::Math::cos(theta_Wp_star)) * (1 + ROOT::Math::cos(theta_Wm_star))*(1 + ROOT::Math::cos(theta_Wm_star));
  Double_t minus3 = cR*cR*cL*cL * (1 + ROOT::Math::cos(theta_Wp_star))*(1 + ROOT::Math::cos(theta_Wp_star)) * (1 - ROOT::Math::cos(theta_Wm_star))*(1 - ROOT::Math::cos(theta_Wm_star));
  Double_t minus4 = cR*cR*cL*cL * (1 - ROOT::Math::cos(theta_Wp_star))*(1 - ROOT::Math::cos(theta_Wp_star)) * (1 + ROOT::Math::cos(theta_Wm_star))*(1 + ROOT::Math::cos(theta_Wm_star));
  
  Double_t Amm2 = P1 * P2 * (minus1 + minus2 + minus3 + minus4);
  
  /////////////////////////////////////
  //            2Re(ALL++)           //
  /////////////////////////////////////
  
  Double_t 2ReALLpp = -4 * K * P1 * P2 * (plus1 + plus2 - plus3 - plus4) * ROOT::Math::sin(theta_Wp_star) * ROOT::Math::sin(theta_Wm_star) * ROOT::Math::cos(dphill);
  
  /////////////////////////////////////
  //            2Re(ALL--)           //
  /////////////////////////////////////
  
  Double_t 2ReALLmm = -4 * K * P1 * P2 * (minus1 + minus2 - minus3 - minus4) * ROOT::Math::sin(theta_Wp_star) * ROOT::Math::sin(theta_Wm_star) * ROOT::Math::cos(dphill);

  /////////////////////////////////////
  //            2Re(A++--)           //
  /////////////////////////////////////
  
  Double_t 2ReAppmm = 2 * P1 * P2 * (cL*cL + cR*cR)*(cL*cL + cR*cR) * ROOT::Math::sin(theta_Wp_star)*ROOT::Math::sin(theta_Wp_star) * ROOT::Math::sin(theta_Wm_star)*ROOT::Math::sin(theta_Wm_star) * ROOT::Math::cos(2*dphill);
  
  
  /////////////////////////////////////
  //             |ATT|^2             //
  /////////////////////////////////////
  
  Double_t ATT2 = App2 + Amm2 + 2ReAppmm;
  
  Double_t weight_LL = ALL2 / (ALL2 + ATT2 + 2ReALLpp + 2ReALLmm);
  
  
  
  
  
  
  

  

  if (name_=="LL"){
    return (double)weight_LL;
  }else if (name_=="TL"){
    return (double)weight_TL;
  }else if (name_=="LT"){
    return (double)weight_LT;
  }else if (name_=="TT"){
    return (double)weight_TT;
  }else if (name_=="cos_wp"){
    return (double)cos_Wp_theta_star;
  }else if (name_=="cos_wm"){
    return (double)cos_Wm_theta_star;
  }else if (name_=="f0_p"){
    return (double)weight_f0_Wp;
  }else if (name_=="fL_p"){
    return (double)weight_fL_Wp;
  }else if (name_=="fR_p"){
    return (double)weight_fR_Wp;
  }else if (name_=="f0_m"){
    return (double)weight_f0_Wm;
  }else if (name_=="fL_m"){
    return (double)weight_fL_Wm;
  }else if (name_=="fR_m"){
    return (double)weight_fR_Wm;
  }else{
    return -999;
  }
    
}  
  
void
DoPolarizationWeight::bindTree_(multidraw::FunctionLibrary& _library)
{
  //GenPart
  _library.bindBranch(GenPart_eta, "GenPart_eta");
  _library.bindBranch(GenPart_pt, "GenPart_pt");
  _library.bindBranch(GenPart_mass, "GenPart_mass");
  _library.bindBranch(GenPart_phi, "GenPart_phi");
  _library.bindBranch(GenPart_status, "GenPart_status");
  _library.bindBranch(GenPart_pdgId, "GenPart_pdgId");
  _library.bindBranch(GenPart_genPartIdxMother, "GenPart_genPartIdxMother");
}
