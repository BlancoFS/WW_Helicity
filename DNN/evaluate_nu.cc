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
#include "model_cos_theta.h"
#include "model_cos_theta_m.h"
#include "model_cos_theta_p.h"
#include <math.h>
#include <bits/stdc++.h>

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


class evaluate_cos_theta: public multidraw::TTreeFunction {
public:
  evaluate_cos_theta(int const nclass);

  char const* getName() const override { return "evaluate_cos_theta"; }
  TTreeFunction* clone() const override { return new evaluate_cos_theta(nclass_); }

  unsigned getNdata() override { return 1; }
  double evaluate(unsigned) override;

protected:
  int nclass_;
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
  FloatValueReader* mth{};
  FloatValueReader* PuppiMET_pt{};
  FloatValueReader* PuppiMET_phi{};
};


evaluate_cos_theta::evaluate_cos_theta(int const nclass) :
  TTreeFunction()
{
  nclass_ = nclass;
}

double
evaluate_cos_theta::evaluate(unsigned)
{

  int nlep = (int)*nLepton->Get();

  if (nlep<2) return -9999;

  float L1_pt = Lepton_pt->At(0); 
  float L2_pt = Lepton_pt->At(1);

  float L1_eta = Lepton_eta->At(0);
  float L2_eta = Lepton_eta->At(1);

  float L1_phi = Lepton_phi->At(0);
  float L2_phi = Lepton_phi->At(1);

  int L1_pdgId = Lepton_pdgId->At(0);
  int L2_pdgId = Lepton_pdgId->At(1);

  TLorentzVector L1(0.0, 0.0, 0.0, 0.0);
  TLorentzVector L2(0.0, 0.0, 0.0, 0.0);

  TLorentzVector mu(0.0, 0.0, 0.0, 0.0);
  TLorentzVector el(0.0, 0.0, 0.0, 0.0);
  TLorentzVector MET(0.0, 0.0, 0.0, 0.0);
  TLorentzVector LL(0.0, 0.0, 0.0, 0.0);


  int lp_pdgId;
  int lm_pdgId;

  
  if (L1_pdgId<0){
    //L1.SetPtEtaPhiM(L1_pt, L1_eta, L1_phi, 0.0);
    //L2.SetPtEtaPhiM(L2_pt, L2_eta, L2_phi, 0.0);
    lp_pdgId = L1_pdgId;
    lm_pdgId = L2_pdgId;
  }else{
    //L2.SetPtEtaPhiM(L1_pt, L1_eta, L1_phi, 0.0);
    //L1.SetPtEtaPhiM(L2_pt, L2_eta, L2_phi, 0.0);
    lp_pdgId = L2_pdgId;
    lm_pdgId = L1_pdgId;
  }

  if (abs(L1_pdgId)==13){
    mu.SetPtEtaPhiM(L1_pt, L1_eta, L1_phi, 0.0);
    el.SetPtEtaPhiM(L2_pt, L2_eta, L2_phi, 0.0);
  }else{
    el.SetPtEtaPhiM(L1_pt, L1_eta, L1_phi, 0.0);
    mu.SetPtEtaPhiM(L2_pt, L2_eta, L2_phi, 0.0);
  }

  L1 = mu;
  L2 = el;

  
  //std::vector<float> phi[200];

  /**
  std::vector<float> phi = {0., 0.010507, 0.021014, 0.031521, 0.042028, 
			    0.05253499, 0.06304199, 0.07354899, 0.08405599, 0.09456299,
			    0.10506999, 0.11557699, 0.12608399, 0.13659098, 0.14709798,
			    0.15760498, 0.16811198, 0.17861898, 0.18912598, 0.19963298,
			    0.21013998, 0.22064698, 0.23115397, 0.24166097, 0.25216797,
			    0.26267497, 0.27318197, 0.28368897, 0.29419597, 0.30470297,
			    0.31520997, 0.32571696, 0.33622396, 0.34673096, 0.35723796,
			    0.36774496, 0.37825196, 0.38875896, 0.39926596, 0.40977295,
			    0.42027995, 0.43078695, 0.44129395, 0.45180095, 0.46230795,
			    0.47281495, 0.48332195, 0.49382895, 0.50433594, 0.51484294,
			    0.52534994, 0.53585694, 0.54636394, 0.55687094, 0.56737794,
			    0.57788494, 0.58839194, 0.59889893, 0.60940593, 0.61991293,
			    0.63041993, 0.64092693, 0.65143393, 0.66194093, 0.67244793,
			    0.68295492, 0.69346192, 0.70396892, 0.71447592, 0.72498292,
			    0.73548992, 0.74599692, 0.75650392, 0.76701092, 0.77751791,
			    0.78802491, 0.79853191, 0.80903891, 0.81954591, 0.83005291,
			    0.84055991, 0.85106691, 0.8615739 , 0.8720809 , 0.8825879 ,
			    0.8930949 , 0.9036019 , 0.9141089 , 0.9246159 , 0.9351229 ,
			    0.9456299 , 0.95613689, 0.96664389, 0.97715089, 0.98765789,
			    0.99816489, 1.00867189, 1.01917889, 1.02968589, 1.04019289,
			    1.05069988, 1.06120688, 1.07171388, 1.08222088, 1.09272788,
			    1.10323488, 1.11374188, 1.12424888, 1.13475587, 1.14526287,
			    1.15576987, 1.16627687, 1.17678387, 1.18729087, 1.19779787,
			    1.20830487, 1.21881187, 1.22931886, 1.23982586, 1.25033286,
			    1.26083986, 1.27134686, 1.28185386, 1.29236086, 1.30286786,
			    1.31337486, 1.32388185, 1.33438885, 1.34489585, 1.35540285,
			    1.36590985, 1.37641685, 1.38692385, 1.39743085, 1.40793784,
			    1.41844484, 1.42895184, 1.43945884, 1.44996584, 1.46047284,
			    1.47097984, 1.48148684, 1.49199384, 1.50250083, 1.51300783,
			    1.52351483, 1.53402183, 1.54452883, 1.55503583, 1.56554283,
			    1.57604983, 1.58655683, 1.59706382, 1.60757082, 1.61807782,
			    1.62858482, 1.63909182, 1.64959882, 1.66010582, 1.67061282,
			    1.68111981, 1.69162681, 1.70213381, 1.71264081, 1.72314781,
			    1.73365481, 1.74416181, 1.75466881, 1.76517581, 1.7756828 ,
			    1.7861898 , 1.7966968 , 1.8072038 , 1.8177108 , 1.8282178 ,
			    1.8387248 , 1.8492318 , 1.85973879, 1.87024579, 1.88075279,
			    1.89125979, 1.90176679, 1.91227379, 1.92278079, 1.93328779,
			    1.94379479, 1.95430178, 1.96480878, 1.97531578, 1.98582278,
			    1.99632978, 2.00683678, 2.01734378, 2.02785078, 2.03835778,
			    2.04886477, 2.05937177, 2.06987877, 2.08038577, 2.09089277,
			    2.10139977, 2.11190677, 2.12241377, 2.13292076, 2.14342776,
			    2.15393476, 2.16444176, 2.17494876, 2.18545576, 2.19596276,
			    2.20646976, 2.21697676, 2.22748375, 2.23799075, 2.24849775,
			    2.25900475, 2.26951175, 2.28001875, 2.29052575, 2.30103275,
			    2.31153975, 2.32204674, 2.33255374, 2.34306074, 2.35356774,
			    2.36407474, 2.37458174, 2.38508874, 2.39559574, 2.40610273,
			    2.41660973, 2.42711673, 2.43762373, 2.44813073, 2.45863773,
			    2.46914473, 2.47965173, 2.49015873, 2.50066572, 2.51117272,
			    2.52167972, 2.53218672, 2.54269372, 2.55320072, 2.56370772,
			    2.57421472, 2.58472171, 2.59522871, 2.60573571, 2.61624271,
			    2.62674971, 2.63725671, 2.64776371, 2.65827071, 2.66877771,
			    2.6792847 , 2.6897917 , 2.7002987 , 2.7108057 , 2.7213127 ,
			    2.7318197 , 2.7423267 , 2.7528337 , 2.7633407 , 2.77384769,
			    2.78435469, 2.79486169, 2.80536869, 2.81587569, 2.82638269,
			    2.83688969, 2.84739669, 2.85790368, 2.86841068, 2.87891768,
			    2.88942468, 2.89993168, 2.91043868, 2.92094568, 2.93145268,
			    2.94195968, 2.95246667, 2.96297367, 2.97348067, 2.98398767,
			    2.99449467, 3.00500167, 3.01550867, 3.02601567, 3.03652267,
			    3.04702966, 3.05753666, 3.06804366, 3.07855066, 3.08905766,
			    3.09956466, 3.11007166, 3.12057866, 3.13108565, 3.14159265};
  **/

  std::vector<float> phi = {0.        , 0.01259155, 0.02518311, 0.03777466, 0.05036621,
			    0.06295777, 0.07554932, 0.08814088, 0.10073243, 0.11332398,
			    0.12591554, 0.13850709, 0.15109864, 0.1636902 , 0.17628175,
			    0.18887331, 0.20146486, 0.21405641, 0.22664797, 0.23923952,
			    0.25183107, 0.26442263, 0.27701418, 0.28960574, 0.30219729,
			    0.31478884, 0.3273804 , 0.33997195, 0.3525635 , 0.36515506,
			    0.37774661, 0.39033817, 0.40292972, 0.41552127, 0.42811283,
			    0.44070438, 0.45329593, 0.46588749, 0.47847904, 0.4910706 ,
			    0.50366215, 0.5162537 , 0.52884526, 0.54143681, 0.55402836,
			    0.56661992, 0.57921147, 0.59180302, 0.60439458, 0.61698613,
			    0.62957769, 0.64216924, 0.65476079, 0.66735235, 0.6799439 ,
			    0.69253545, 0.70512701, 0.71771856, 0.73031012, 0.74290167,
			    0.75549322, 0.76808478, 0.78067633, 0.79326788, 0.80585944,
			    0.81845099, 0.83104255, 0.8436341 , 0.85622565, 0.86881721,
			    0.88140876, 0.89400031, 0.90659187, 0.91918342, 0.93177498,
			    0.94436653, 0.95695808, 0.96954964, 0.98214119, 0.99473274,
			    1.0073243 , 1.01991585, 1.03250741, 1.04509896, 1.05769051,
			    1.07028207, 1.08287362, 1.09546517, 1.10805673, 1.12064828,
			    1.13323983, 1.14583139, 1.15842294, 1.1710145 , 1.18360605,
			    1.1961976 , 1.20878916, 1.22138071, 1.23397226, 1.24656382,
			    1.25915537, 1.27174693, 1.28433848, 1.29693003, 1.30952159,
			    1.32211314, 1.33470469, 1.34729625, 1.3598878 , 1.37247936,
			    1.38507091, 1.39766246, 1.41025402, 1.42284557, 1.43543712,
			    1.44802868, 1.46062023, 1.47321179, 1.48580334, 1.49839489,
			    1.51098645, 1.523578  , 1.53616955, 1.54876111, 1.56135266,
			    1.57394422, 1.58653577, 1.59912732, 1.61171888, 1.62431043,
			    1.63690198, 1.64949354, 1.66208509, 1.67467664, 1.6872682 ,
			    1.69985975, 1.71245131, 1.72504286, 1.73763441, 1.75022597,
			    1.76281752, 1.77540907, 1.78800063, 1.80059218, 1.81318374,
			    1.82577529, 1.83836684, 1.8509584 , 1.86354995, 1.8761415 ,
			    1.88873306, 1.90132461, 1.91391617, 1.92650772, 1.93909927,
			    1.95169083, 1.96428238, 1.97687393, 1.98946549, 2.00205704,
			    2.0146486 , 2.02724015, 2.0398317 , 2.05242326, 2.06501481,
			    2.07760636, 2.09019792, 2.10278947, 2.11538103, 2.12797258,
			    2.14056413, 2.15315569, 2.16574724, 2.17833879, 2.19093035,
			    2.2035219 , 2.21611346, 2.22870501, 2.24129656, 2.25388812,
			    2.26647967, 2.27907122, 2.29166278, 2.30425433, 2.31684588,
			    2.32943744, 2.34202899, 2.35462055, 2.3672121 , 2.37980365,
			    2.39239521, 2.40498676, 2.41757831, 2.43016987, 2.44276142,
			    2.45535298, 2.46794453, 2.48053608, 2.49312764, 2.50571919,
			    2.51831074, 2.5309023 , 2.54349385, 2.55608541, 2.56867696,
			    2.58126851, 2.59386007, 2.60645162, 2.61904317, 2.63163473,
			    2.64422628, 2.65681784, 2.66940939, 2.68200094, 2.6945925 ,
			    2.70718405, 2.7197756 , 2.73236716, 2.74495871, 2.75755027,
			    2.77014182, 2.78273337, 2.79532493, 2.80791648, 2.82050803,
			    2.83309959, 2.84569114, 2.85828269, 2.87087425, 2.8834658 ,
			    2.89605736, 2.90864891, 2.92124046, 2.93383202, 2.94642357,
			    2.95901512, 2.97160668, 2.98419823, 2.99678979, 3.00938134,
			    3.02197289, 3.03456445, 3.047156  , 3.05974755, 3.07233911,
			    3.08493066, 3.09752222, 3.11011377, 3.12270532, 3.13529688,
			    3.14788843, 3.16047998, 3.17307154, 3.18566309, 3.19825465,
			    3.2108462 , 3.22343775, 3.23602931, 3.24862086, 3.26121241,
			    3.27380397, 3.28639552, 3.29898708, 3.31157863, 3.32417018,
			    3.33676174, 3.34935329, 3.36194484, 3.3745364 , 3.38712795,
			    3.3997195 , 3.41231106, 3.42490261, 3.43749417, 3.45008572,
			    3.46267727, 3.47526883, 3.48786038, 3.50045193, 3.51304349,
			    3.52563504, 3.5382266 , 3.55081815, 3.5634097 , 3.57600126,
			    3.58859281, 3.60118436, 3.61377592, 3.62636747, 3.63895903,
			    3.65155058, 3.66414213, 3.67673369, 3.68932524, 3.70191679,
			    3.71450835, 3.7270999 , 3.73969146, 3.75228301, 3.76487456,
			    3.77746612, 3.79005767, 3.80264922, 3.81524078, 3.82783233,
			    3.84042389, 3.85301544, 3.86560699, 3.87819855, 3.8907901 ,
			    3.90338165, 3.91597321, 3.92856476, 3.94115631, 3.95374787,
			    3.96633942, 3.97893098, 3.99152253, 4.00411408, 4.01670564,
			    4.02929719, 4.04188874, 4.0544803 , 4.06707185, 4.07966341,
			    4.09225496, 4.10484651, 4.11743807, 4.13002962, 4.14262117,
			    4.15521273, 4.16780428, 4.18039584, 4.19298739, 4.20557894,
			    4.2181705 , 4.23076205, 4.2433536 , 4.25594516, 4.26853671,
			    4.28112827, 4.29371982, 4.30631137, 4.31890293, 4.33149448,
			    4.34408603, 4.35667759, 4.36926914, 4.3818607 , 4.39445225,
			    4.4070438 , 4.41963536, 4.43222691, 4.44481846, 4.45741002,
			    4.47000157, 4.48259312, 4.49518468, 4.50777623, 4.52036779,
			    4.53295934, 4.54555089, 4.55814245, 4.570734  , 4.58332555,
			    4.59591711, 4.60850866, 4.62110022, 4.63369177, 4.64628332,
			    4.65887488, 4.67146643, 4.68405798, 4.69664954, 4.70924109,
			    4.72183265, 4.7344242 , 4.74701575, 4.75960731, 4.77219886,
			    4.78479041, 4.79738197, 4.80997352, 4.82256508, 4.83515663,
			    4.84774818, 4.86033974, 4.87293129, 4.88552284, 4.8981144 ,
			    4.91070595, 4.92329751, 4.93588906, 4.94848061, 4.96107217,
			    4.97366372, 4.98625527, 4.99884683, 5.01143838, 5.02402993,
			    5.03662149, 5.04921304, 5.0618046 , 5.07439615, 5.0869877 ,
			    5.09957926, 5.11217081, 5.12476236, 5.13735392, 5.14994547,
			    5.16253703, 5.17512858, 5.18772013, 5.20031169, 5.21290324,
			    5.22549479, 5.23808635, 5.2506779 , 5.26326946, 5.27586101,
			    5.28845256, 5.30104412, 5.31363567, 5.32622722, 5.33881878,
			    5.35141033, 5.36400189, 5.37659344, 5.38918499, 5.40177655,
			    5.4143681 , 5.42695965, 5.43955121, 5.45214276, 5.46473432,
			    5.47732587, 5.48991742, 5.50250898, 5.51510053, 5.52769208,
			    5.54028364, 5.55287519, 5.56546675, 5.5780583 , 5.59064985,
			    5.60324141, 5.61583296, 5.62842451, 5.64101607, 5.65360762,
			    5.66619917, 5.67879073, 5.69138228, 5.70397384, 5.71656539,
			    5.72915694, 5.7417485 , 5.75434005, 5.7669316 , 5.77952316,
			    5.79211471, 5.80470627, 5.81729782, 5.82988937, 5.84248093,
			    5.85507248, 5.86766403, 5.88025559, 5.89284714, 5.9054387 ,
			    5.91803025, 5.9306218 , 5.94321336, 5.95580491, 5.96839646,
			    5.98098802, 5.99357957, 6.00617113, 6.01876268, 6.03135423,
			    6.04394579, 6.05653734, 6.06912889, 6.08172045, 6.094312  ,
			    6.10690356, 6.11949511, 6.13208666, 6.14467822, 6.15726977,
			    6.16986132, 6.18245288, 6.19504443, 6.20763598, 6.22022754,
			    6.23281909, 6.24541065, 6.2580022 , 6.27059375, 6.28318531};


  float met_x = *PuppiMET_pt->Get() * ROOT::Math::cos(*PuppiMET_phi->Get());
  float met_y = *PuppiMET_pt->Get() * ROOT::Math::sin(*PuppiMET_phi->Get());

  LL = L1+L2;

  float met_e = ROOT::Math::sqrt(met_x*met_x + met_y*met_y + 30.0*30.0);

  MET.SetPxPyPzE(met_x, met_y, 0.0, met_e);


  std::vector<float> mt1_p = {};
  std::vector<float> mt1_m = {};

  float phi_00;
  float c;
  float f;
  float g;
 
  float r_m;
  float r_p;

  phi_00 = TMath::ACos( (LL.Px()*MET.Px() + LL.Py()*MET.Py()) / (LL.Pt() * MET.Pt()));
  c = (L2.Px()*MET.Px() + L2.Py()*MET.Py())*(L2.Px()*MET.Px() + L2.Py()*MET.Py()) - MET.Pt()*MET.Pt()*L2.Pt()*L2.Pt();

  for (int i=0; i<500; i++){
        
    f = L1.Pt()*L1.Pt() + (LL.Pt()*LL.Pt())*(ROOT::Math::cos(phi[i])*ROOT::Math::cos(phi[i])) - 2 * L1.Pt()*LL.Pt()*ROOT::Math::cos(phi[i]) - L2.Pt()*L2.Pt();
    g = 2 * (L1.Pt() - LL.Pt()*ROOT::Math::cos(phi[i]))* (L2.Px()*MET.Px() + L2.Py()*MET.Py()) + 2 * (L2.Pt()*L2.Pt()) * (MET.Pt()) * ROOT::Math::cos(phi[i] + phi_00);

    if (((g * g - 4 * c * f) < 0) || (f==0)){

      mt1_p.push_back(1e99);
      mt1_m.push_back(1e99);

    }else{
      
      r_p = ((-1 * g + ROOT::Math::sqrt(g*g - 4*c*f))/(2*f));
      r_m = ((-1 * g - ROOT::Math::sqrt(g*g - 4*c*f))/(2*f));

      if (r_p < 0){
	mt1_p.push_back(1e99);
      }else{
	mt1_p.push_back( 2 * (L1.Pt() * r_p - L1.Px()*(r_p*ROOT::Math::cos(phi[i])) + L1.Py()*(r_p*ROOT::Math::sin(phi[i]))));
      }
      if (r_m < 0){
	mt1_m.push_back( 2 * (L1.Pt() * abs(r_m) - L1.Px()*( abs(r_m) * ROOT::Math::cos(phi[i])) + L1.Py()*( abs(r_m) * ROOT::Math::sin(phi[i]))));
      }else{
	mt1_m.push_back( 2 * (L1.Pt() * r_m - L1.Px()*(r_m*ROOT::Math::cos(phi[i])) + L1.Py()*(r_m*ROOT::Math::sin(phi[i]))));
      }

    }

    //cout << "phi -> " << phi[i] << endl;
    //cout << "pos -> " << r_p << endl;
    //cout << "neg -> " << r_m << endl;
    //cout << "mt1 p -> " << mt1_p[i] << endl;
    //cout << "mt1 m -> " << mt1_m[i] << endl;
    //cout << "-------------------------------------" << endl;

  }

  //int minind_p = std::min_element(mt1_p.begin(),mt1_p.end()) - mt1_p.begin();  
  //int minind_m = std::min_element(mt1_m.begin(),mt1_m.end()) - mt1_m.begin();

  int minind_p = 0;
  int minind_m = 0;

  float min_mt1_p = mt1_p[0];
  float min_mt1_m = mt1_m[0];

  for (int i=0; i<500; i++){

    if (mt1_p[i]==1e99){
      
    }else if (min_mt1_p > mt1_p[i]){
      min_mt1_p = mt1_p[i];
      minind_p = i;
    }
    if (mt1_m[i]==1e99){

    }else if (min_mt1_m > mt1_m[i]){
      min_mt1_m= mt1_p[i];
      minind_m = i;
    }

  }

  float min_phi_p = phi[minind_p];
  float min_phi_m = phi[minind_m];

  float f_p = L1.Pt()*L1.Pt() + (LL.Pt()*LL.Pt())*(ROOT::Math::cos(min_phi_p)*ROOT::Math::cos(min_phi_p)) - 2 * L1.Pt()*LL.Pt()*ROOT::Math::cos(min_phi_p) - L2.Pt()*L2.Pt();
  float g_p = 2 * (L1.Pt() - LL.Pt()*ROOT::Math::cos(min_phi_p))* (L2.Px()*MET.Px() + L2.Py()*MET.Py()) + 2 * (L2.Pt()*L2.Pt()) * (MET.Pt()) * ROOT::Math::cos(min_phi_p + phi_00);

  float f_m = L1.Pt()*L1.Pt() + (LL.Pt()*LL.Pt())*(ROOT::Math::cos(min_phi_m)*ROOT::Math::cos(min_phi_m)) - 2 * L1.Pt()*LL.Pt()*ROOT::Math::cos(min_phi_m) - L2.Pt()*L2.Pt();
  float g_m = 2 * (L1.Pt() - LL.Pt()*ROOT::Math::cos(min_phi_m))* (L2.Px()*MET.Px() + L2.Py()*MET.Py()) + 2 * (L2.Pt()*L2.Pt()) * (MET.Pt()) * ROOT::Math::cos(min_phi_m + phi_00);

  float p1_p = ((-1 * g_p + ROOT::Math::sqrt(g_p*g_p - 4*c*f_p))/(2*f_p));
  float p1_m = ((-1 * g_m - ROOT::Math::sqrt(g_m*g_m - 4*c*f_m))/(2*f_m));

  
  float positive_numu_px = p1_p * ROOT::Math::cos(min_phi_p);
  float positive_numu_py = p1_p * ROOT::Math::sin(min_phi_p);
  float positive_nuel_px = MET.Px() - p1_p * ROOT::Math::cos(min_phi_p);
  float positive_nuel_py = MET.Py() - p1_p * ROOT::Math::sin(min_phi_p);

  float negative_numu_px = p1_m * ROOT::Math::cos(min_phi_m);
  float negative_numu_py = p1_m * ROOT::Math::sin(min_phi_m);
  float negative_nuel_px = MET.Px() - p1_m * ROOT::Math::cos(min_phi_m);
  float negative_nuel_py = MET.Py() - p1_m * ROOT::Math::sin(min_phi_m);
  

  float pos_nup_px;
  float pos_nup_py;
  float pos_num_px;
  float pos_num_py;

  float neg_nup_px;
  float neg_nup_py;
  float neg_num_px;
  float neg_num_py;


  float lp_px;
  float lp_py;
  float lp_pz;

  float lm_px;
  float lm_py;
  float lm_pz;

  float lp_e;
  float lm_e;

  float lp_pt;
  float lp_eta;
  float lp_phi;
  
  float lm_pt;
  float lm_eta;
  float lm_phi;


  if (abs(lp_pdgId)==13){

    pos_nup_px = positive_numu_px;
    pos_nup_py = positive_numu_py;
    pos_num_px = positive_nuel_px;
    pos_num_py = positive_nuel_py;

    neg_nup_px = negative_numu_px;
    neg_nup_py = negative_numu_py;
    neg_num_px = negative_nuel_px;
    neg_num_py = negative_nuel_py;

    lp_px = L1.Px();
    lp_py = L1.Py();
    lp_pz = L1.Pz();

    lm_px = L2.Px();
    lm_py = L2.Py();
    lm_pz = L2.Pz();

    lp_e = L1.E();
    lm_e = L2.E();

    lp_pt = L1.Pt();
    lp_eta = L1.Eta();
    lp_phi = L1.Phi();

    lm_pt = L2.Pt();
    lm_eta = L2.Eta();
    lm_phi = L2.Phi();

  }else{

    pos_nup_px = positive_nuel_px;
    pos_nup_py = positive_nuel_py;
    pos_num_px = positive_numu_px;
    pos_num_py = positive_numu_py;

    neg_nup_px = negative_nuel_px;
    neg_nup_py = negative_nuel_py;
    neg_num_px = negative_numu_px;
    neg_num_py = negative_numu_py;

    lp_px = L2.Px();
    lp_py = L2.Py();
    lp_pz = L2.Pz();

    lm_px = L1.Px();
    lm_py = L1.Py();
    lm_pz = L1.Pz();

    lp_e = L2.E();
    lm_e = L1.E();

    lp_pt = L2.Pt();
    lp_eta = L2.Eta();
    lp_phi = L2.Phi();

    lm_pt = L1.Pt();
    lm_eta = L1.Eta();
    lm_phi = L1.Phi();
    
  }
  
  
  ////// Cos theta* //////


  TLorentzVector l_p(0.0, 0.0, 0.0, 0.0);
  TLorentzVector l_m(0.0, 0.0, 0.0, 0.0);
  TLorentzVector nup(0.0, 0.0, 0.0, 0.0);
  TLorentzVector num(0.0, 0.0, 0.0, 0.0);

  TLorentzVector pos_nup(0.0, 0.0, 0.0, 0.0);
  TLorentzVector pos_num(0.0, 0.0, 0.0, 0.0);

  TLorentzVector neg_nup(0.0, 0.0, 0.0, 0.0);
  TLorentzVector neg_num(0.0, 0.0, 0.0, 0.0);

  l_p.SetPxPyPzE(lp_px, lp_py, lp_pz, lp_e);
  l_m.SetPxPyPzE(lm_px, lm_py, lm_pz, lm_e);

  pos_nup.SetPxPyPzE(pos_nup_px, pos_nup_py, 0.0, ROOT::Math::sqrt(pos_nup_px*pos_nup_px + pos_nup_py*pos_nup_py + 30.0*30.0));
  pos_num.SetPxPyPzE(pos_num_px, pos_num_py, 0.0, ROOT::Math::sqrt(pos_num_px*pos_num_px + pos_num_py*pos_num_py + 30.0*30.0));

  neg_nup.SetPxPyPzE(neg_nup_px, neg_nup_py, 0.0, ROOT::Math::sqrt(neg_nup_px*neg_nup_px + neg_nup_py*neg_nup_py + 30.0*30.0));
  neg_num.SetPxPyPzE(neg_num_px, neg_num_py, 0.0, ROOT::Math::sqrt(neg_num_px*neg_num_px + neg_num_py*neg_num_py + 30.0*30.0));

  if(min_mt1_p<min_mt1_m || min_mt1_m<0.0){
    
    nup.SetPxPyPzE(pos_nup_px, pos_nup_py, 0.0, ROOT::Math::sqrt(pos_nup_px*pos_nup_px + pos_nup_py*pos_nup_py + 30.0*30.0));
    num.SetPxPyPzE(pos_num_px, pos_num_py, 0.0, ROOT::Math::sqrt(pos_num_px*pos_num_px + pos_num_py*pos_num_py + 30.0*30.0));

    //cout << "positive" << endl;
    //cout << "phi min p -> " << min_phi_p << endl;
    //cout << "phi min m -> " << min_phi_m << endl;
    //cout << "mt1 min -> " << min_mt1_p << endl;
    //cout << "mt1 min negative-> " << min_mt1_m << endl;

  }else{
    
    nup.SetPxPyPzE(neg_nup_px, neg_nup_py, 0.0, ROOT::Math::sqrt(neg_nup_px*neg_nup_px + neg_nup_py*neg_nup_py + 30.0*30.0));
    num.SetPxPyPzE(neg_num_px, neg_num_py, 0.0, ROOT::Math::sqrt(neg_num_px*neg_num_px + neg_num_py*neg_num_py + 30.0*30.0));

    //cout << "negative" << endl;
    //cout << "phi min p -> " << min_phi_p << endl;
    //cout << "phi min m -> " << min_phi_m << endl;
    //cout << "mt1 min -> " << min_mt1_m << endl;
    //cout << "mt1 min positive -> " << min_mt1_p << endl;

  }

  TLorentzVector W_p(0.0, 0.0, 0.0, 0.0);
  TLorentzVector W_m(0.0, 0.0, 0.0, 0.0);

  TLorentzVector pos_W_p(0.0, 0.0, 0.0, 0.0);
  TLorentzVector pos_W_m(0.0, 0.0, 0.0, 0.0);

  TLorentzVector neg_W_p(0.0, 0.0, 0.0, 0.0);
  TLorentzVector neg_W_m(0.0, 0.0, 0.0, 0.0);

  W_p = l_p + nup;
  W_m = l_m + num;

  pos_W_p = l_p + pos_nup;
  pos_W_m = l_m + pos_num;

  neg_W_p = l_p + neg_nup;
  neg_W_m = l_m + neg_num;

  ROOT::Math::PtEtaPhiEVector Wp;
  ROOT::Math::PtEtaPhiEVector Wm;
  ROOT::Math::PtEtaPhiEVector lp;
  ROOT::Math::PtEtaPhiEVector lm;

  ROOT::Math::PtEtaPhiEVector pos_Wp;
  ROOT::Math::PtEtaPhiEVector pos_Wm;

  ROOT::Math::PtEtaPhiEVector neg_Wp;
  ROOT::Math::PtEtaPhiEVector neg_Wm;

  Wp.SetCoordinates(W_p.Pt(), W_p.Eta(), W_p.Phi(), W_p.E());
  Wm.SetCoordinates(W_m.Pt(), W_m.Eta(), W_m.Phi(), W_m.E());

  pos_Wp.SetCoordinates(pos_W_p.Pt(), pos_W_p.Eta(), pos_W_p.Phi(), pos_W_p.E());
  pos_Wm.SetCoordinates(pos_W_m.Pt(), pos_W_m.Eta(), pos_W_m.Phi(), pos_W_m.E());

  neg_Wp.SetCoordinates(neg_W_p.Pt(), neg_W_p.Eta(), neg_W_p.Phi(), neg_W_p.E());
  neg_Wm.SetCoordinates(neg_W_m.Pt(), neg_W_m.Eta(), neg_W_m.Phi(), neg_W_m.E());

  lp.SetCoordinates(l_p.Pt(), l_p.Eta(), l_p.Phi(), l_p.E());
  lm.SetCoordinates(l_m.Pt(), l_m.Eta(), l_m.Phi(), l_m.E());
  
  ROOT::Math::XYZVector wpRF;
  ROOT::Math::XYZVector wmRF;

  ROOT::Math::XYZVector pos_wpRF;
  ROOT::Math::XYZVector pos_wmRF;

  ROOT::Math::XYZVector neg_wpRF;
  ROOT::Math::XYZVector neg_wmRF;

  wpRF = Wp.BoostToCM();
  wmRF = Wm.BoostToCM();

  pos_wpRF = pos_Wp.BoostToCM();
  pos_wmRF = pos_Wm.BoostToCM();

  neg_wpRF = neg_Wp.BoostToCM();
  neg_wmRF = neg_Wm.BoostToCM();

  ROOT::Math::XYZVector leppWRF;
  ROOT::Math::XYZVector lepmWRF;

  ROOT::Math::XYZVector pos_leppWRF;
  ROOT::Math::XYZVector pos_lepmWRF;

  ROOT::Math::XYZVector neg_leppWRF;
  ROOT::Math::XYZVector neg_lepmWRF;

  leppWRF = ROOT::Math::VectorUtil::boost(lp, wpRF);
  lepmWRF = ROOT::Math::VectorUtil::boost(lm, wmRF);

  pos_leppWRF = ROOT::Math::VectorUtil::boost(lp, pos_wpRF);
  pos_lepmWRF = ROOT::Math::VectorUtil::boost(lm, pos_wmRF);

  neg_leppWRF = ROOT::Math::VectorUtil::boost(lp, neg_wpRF);
  neg_lepmWRF = ROOT::Math::VectorUtil::boost(lm, neg_wmRF);

  Double_t theta_Wp_star = ROOT::Math::VectorUtil::Angle(leppWRF, Wp);
  Double_t theta_Wm_star = ROOT::Math::VectorUtil::Angle(lepmWRF, Wm);

  Double_t pos_theta_Wp_star = ROOT::Math::VectorUtil::Angle(pos_leppWRF, pos_Wp);
  Double_t pos_theta_Wm_star = ROOT::Math::VectorUtil::Angle(pos_lepmWRF, pos_Wm);

  Double_t neg_theta_Wp_star = ROOT::Math::VectorUtil::Angle(neg_leppWRF, neg_Wp);
  Double_t neg_theta_Wm_star = ROOT::Math::VectorUtil::Angle(neg_lepmWRF, neg_Wm);

  float cos_theta_p = (float)ROOT::Math::cos(theta_Wp_star);
  float cos_theta_m = (float)ROOT::Math::cos(theta_Wm_star);

  float pos_cos_theta_p = (float)ROOT::Math::cos(pos_theta_Wp_star);
  float pos_cos_theta_m = (float)ROOT::Math::cos(pos_theta_Wm_star);

  float neg_cos_theta_p = (float)ROOT::Math::cos(neg_theta_Wp_star);
  float neg_cos_theta_m = (float)ROOT::Math::cos(neg_theta_Wm_star);

  float input[22];
  
  input[0] = lp_px;
  input[1] = lp_py;
  input[2] = lp_pz;
  input[3] = lp_pt;
  input[4] = lp_phi;
  input[5] = lp_eta;
  input[6] = lm_pt;
  input[7] = lm_phi;
  input[8] = lm_eta;
  input[9] = lm_px;
  input[10] = lm_py;
  input[11] = lm_pz;
  //input[12] = LL.Pz();
  input[12] = met_x;
  input[13] = met_y;
  input[14] = *PuppiMET_pt->Get();
  input[15] = *PuppiMET_phi->Get();
  //input[17] = *ptll->Get();
  input[16] = pos_nup.Px();
  input[17] = neg_nup.Px();
  input[18] = pos_nup.Py();
  input[19] = neg_nup.Py();
  input[20] = pos_cos_theta_p;
  input[21] = neg_cos_theta_p;


  float input_m[22];

  input_m[0] = lp_px;
  input_m[1] = lp_py;
  input_m[2] = lp_pz;
  input_m[3] = lp_pt;
  input_m[4] = lp_phi;
  input_m[5] = lp_eta;
  input_m[6] = lm_pt;
  input_m[7] = lm_phi;
  input_m[8] = lm_eta;
  input_m[9] = lm_px;
  input_m[10] = lm_py;
  input_m[11] = lm_pz;
  input_m[12] = met_x;
  input_m[13] = met_y;
  input_m[14] = *PuppiMET_pt->Get();
  input_m[15] = *PuppiMET_phi->Get();
  input_m[16] = pos_num.Px();
  input_m[17] = neg_num.Px();
  input_m[18] = pos_num.Py();
  input_m[19] = neg_num.Py();
  input_m[20] = pos_cos_theta_m;
  input_m[21] = neg_cos_theta_m;


  float cos_theta_p_dnn = guess_digit_cos(input, 0);

  float cos_theta_m_dnn = guess_digit_cos_m(input_m, 0);;


  if (nclass_==0){
    return cos_theta_p_dnn;
  }else if (nclass_==1){
    return cos_theta_m_dnn;
  }else if (nclass_==2){
    return pos_cos_theta_p;
  }else if (nclass_==3){
    return neg_cos_theta_p;
  }else if (nclass_==4){
    return pos_cos_theta_m;
  }else if (nclass_==5){
    return neg_cos_theta_m;
  }
  
}

void
evaluate_cos_theta::bindTree_(multidraw::FunctionLibrary& _library)
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
}
