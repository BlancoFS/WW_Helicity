#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"

#include "TMath.h"
#include <vector>
#include <iostream>
#include "TLorentzVector.h"

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

using namespace std;

class GetCosTheta : public multidraw::TTreeFunction{
public:
  GetCosTheta(char const* name);

  char const* getName() const override{
    return "GetCosTheta";
  }
  
  TTreeFunction* clone() const override { 
    return new GetCosTheta(name_.c_str()); 
  }

  unsigned getNdata() override { 
    return 1; 
  }

  double evaluate(unsigned) override;

protected:
  void bindTree_(multidraw::FunctionLibrary&) override;

  std::string name_;

  FloatValueReader* MET_pt{};
  FloatValueReader* PuppiMET_pt{};
  FloatValueReader* PuppiMET_phi{};
  FloatArrayReader* Lepton_pt{};
  FloatArrayReader* Lepton_phi{};
  FloatArrayReader* Lepton_eta{};
  IntArrayReader*  Lepton_pdgId{};
  UIntValueReader*  nLepton{};

};

GetCosTheta::GetCosTheta(char const* name) :
  TTreeFunction()
{
  name_ = name;
}

// Function implementation

double GetCosTheta::evaluate(unsigned){

  unsigned nLep{*nLepton->Get()};

  if (nLep > 1){

    TLorentzVector L1;
    TLorentzVector L2;    

    // Lepton 1 is positive
    if (Lepton_pdgId->At(0)<0){
      L1.SetPtEtaPhiM(Lepton_pt->At(0), Lepton_eta->At(0), Lepton_phi->At(0), 0.0);
      L2.SetPtEtaPhiM(Lepton_pt->At(1), Lepton_eta->At(1), Lepton_phi->At(1), 0.0);
    }else{
      L2.SetPtEtaPhiM(Lepton_pt->At(0), Lepton_eta->At(0), Lepton_phi->At(0), 0.0);
      L1.SetPtEtaPhiM(Lepton_pt->At(1), Lepton_eta->At(1), Lepton_phi->At(1), 0.0);
    }

    //double theta_1 = L1.Theta();
    //double theta_2 = L2.Theta();

    ROOT::Math::PtEtaPhiEVector lep1;
    ROOT::Math::PtEtaPhiEVector lep2;

    lep1.SetCoordinates(L1.Pt(), L1.Phi(), L1.Eta(), L1.E());
    lep2.SetCoordinates(L2.Pt(), L2.Phi(), L2.Eta(), L2.E());


    Double_t theta_ll = ROOT::Math::VectorUtil::Angle(lep1, lep2);

    double cos = ROOT::Math::cos(theta_ll);

    double dphi = lep1.Theta()-lep2.Theta();

    double rap1 = 0.5*log( (L1.E()+L1.Pz()) / (L1.E()-L1.Pz()) );
    double rap2 = 0.5*log( (L2.E()+L2.Pz()) / (L2.E()-L2.Pz()) );

    if (name_=="cos_ll"){
      return cos;
    }else if (name_=="dphi"){
      return dphi;
    }else if (name_=="rap1"){
      return rap1;
    }else if (name_=="rap2"){
      return rap2;
    }else{
      return -9999.9;
    }

  }else  
    return -9999.;
}

void GetCosTheta::bindTree_(multidraw::FunctionLibrary& _library){

  _library.bindBranch(Lepton_pt, "Lepton_pt");
  _library.bindBranch(Lepton_phi, "Lepton_phi");
  _library.bindBranch(Lepton_eta, "Lepton_eta");
  _library.bindBranch(nLepton,    "nLepton");
  _library.bindBranch(Lepton_pdgId, "Lepton_pdgId");
}
