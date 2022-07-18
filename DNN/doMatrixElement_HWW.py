import pandas as pd
import ROOT
import numpy as np


if __name__ == '__main__':
    

    df = pd.read_pickle('dataset_HWW_MAOS.pkl')

    #df = df.loc[0:10000]

    df = df.reset_index()

    L1_pt = df["Lepton_pt[0]"].values
    L2_pt = df["Lepton_pt[1]"].values
    
    L1_phi = df["Lepton_phi[0]"].values
    L2_phi = df["Lepton_phi[1]"].values
    
    L1_eta = df["Lepton_eta[0]"].values
    L2_eta = df["Lepton_eta[1]"].values
    
    L1_pdgId = df["Lepton_pdgId[0]"].values
    L2_pdgId = df["Lepton_pdgId[1]"].values

    N1_pt = df["NeutrinoGen_pt[0]"].values
    N2_pt = df["NeutrinoGen_pt[1]"].values

    N1_phi = df["NeutrinoGen_phi[0]"].values
    N2_phi = df["NeutrinoGen_phi[1]"].values

    N1_eta = df["NeutrinoGen_eta[0]"].values
    N2_eta = df["NeutrinoGen_eta[1]"].values

    N1_pdgId = df["NeutrinoGen_pdgId[0]"].values
    N2_pdgId = df["NeutrinoGen_pdgId[1]"].values
    
    df.loc[:, "met_x"] = df.MET_pt * np.cos(df.MET_phi)
    df.loc[:, "met_y"] = df.MET_pt * np.sin(df.MET_phi)
    
    lp_px = []
    lm_px = []
    
    lp_py = []
    lm_py = []
    
    lp_pz = []
    lm_pz = []
    
    lp_e = []
    lm_e = []
    
    lp_pt  = []
    lp_phi = []
    lp_eta = []
    lp_pdgId = []
    
    lm_pt  = []
    lm_phi = []
    lm_eta = []
    lm_pdgId = []
    
    met_x = []
    met_y = []
    pll_z = []

    D_00 = []
    D_TT = []
    D_T0 = []
    D_0T = []
    

    ROOT.gROOT.ProcessLineSync('gSystem->Load("/afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/JHUGenMELA/MELA/data/slc7_amd64_gcc820/libmcfm_707.so","", kTRUE);')
    ROOT.gROOT.ProcessLineSync('gSystem->Load("/afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/lib/slc7_amd64_gcc820/libJHUGenMELAMELA.so","", kTRUE);')
    ROOT.gROOT.ProcessLineSync('gSystem->Load("/afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/lib/libmomemta.so","", kTRUE);')

    ROOT.gROOT.ProcessLineSync(".L ./RecoMoMEMta_HWW_00_LL.C+")

    
    for event in df.index:

        if (event%10000==0):
            print("\n")
            print(str(event) + " Events completed from " + str(len(df)))

        if (len(N2_eta[event])>1 or len(N2_pt[event])>1 or len(N2_phi[event])>1 or len(N2_pdgId[event])>1 or len(N2_eta[event])==0 or len(N2_pt[event])==0 or len(N2_phi[event])==0 or len(N2_pdgId[event])==0):
            D_00_LL.append(-999.9)
            print(N2_eta[event])
            print(N2_pt[event])
            print(N2_phi[event])
            print(N2_pdgId[event])
        else:
            D_00.append(ROOT.RecoMoMEMta_HWW_00_LL(L1_pt[event], L1_eta[event], L1_phi[event], L1_pdgId[event], L2_pt[event], L2_eta[event], L2_phi[event], L2_pdgId[event], N1_pt[event], N1_eta[event], N1_phi[event], N1_pdgId[event], N2_pt[event], N2_eta[event], N2_phi[event], N2_pdgId[event], "00"))
            D_TT.append(ROOT.RecoMoMEMta_HWW_00_LL(L1_pt[event], L1_eta[event], L1_phi[event], L1_pdgId[event], L2_pt[event], L2_eta[event], L2_phi[event], L2_pdgId[event], N1_pt[event], N1_eta[event], N1_phi[event], N1_pdgId[event], N2_pt[event], N2_eta[event], N2_phi[event], N2_pdgId[event], "TT"))
            D_T0.append(ROOT.RecoMoMEMta_HWW_00_LL(L1_pt[event], L1_eta[event], L1_phi[event], L1_pdgId[event], L2_pt[event], L2_eta[event], L2_phi[event], L2_pdgId[event], N1_pt[event], N1_eta[event], N1_phi[event], N1_pdgId[event], N2_pt[event], N2_eta[event], N2_phi[event], N2_pdgId[event], "T0"))
            D_0T.append(ROOT.RecoMoMEMta_HWW_00_LL(L1_pt[event], L1_eta[event], L1_phi[event], L1_pdgId[event], L2_pt[event], L2_eta[event], L2_phi[event], L2_pdgId[event], N1_pt[event], N1_eta[event], N1_phi[event], N1_pdgId[event], N2_pt[event], N2_eta[event], N2_phi[event], N2_pdgId[event], "0T"))

        L1 = ROOT.TLorentzVector(0.0, 0.0, 0.0, 0.0)
        L2 = ROOT.TLorentzVector(0.0, 0.0, 0.0, 0.0)
        LL = ROOT.TLorentzVector(0.0, 0.0, 0.0, 0.0)
        
        if (L1_pdgId[event]<0):    
            L1.SetPtEtaPhiM(L1_pt[event], L1_eta[event], L1_phi[event], 0.0)
            L2.SetPtEtaPhiM(L2_pt[event], L2_eta[event], L2_phi[event], 0.0)
            lp_pdgId.append(L1_pdgId[event])
            lm_pdgId.append(L2_pdgId[event])
        else:
            L2.SetPtEtaPhiM(L1_pt[event], L1_eta[event], L1_phi[event], 0.0)
            L1.SetPtEtaPhiM(L2_pt[event], L2_eta[event], L2_phi[event], 0.0)
            lp_pdgId.append(L2_pdgId[event])
            lm_pdgId.append(L1_pdgId[event])
        
        LL = L1 + L2
        
        
        pll_z.append(LL.Pz())
        
        lp_px.append(L1.Px())
        lp_py.append(L1.Py())
        lp_pz.append(L1.Pz())
        lp_e.append(L1.E())
        
        lp_pt.append(L1.Pt()) 
        lp_phi.append(L1.Phi())
        lp_eta.append(L1.Eta())
        
        lm_px.append(L2.Px())
        lm_py.append(L2.Py())
        lm_pz.append(L2.Pz())
        lm_e.append(L2.E())
        
        lm_pt.append(L2.Pt()) 
        lm_phi.append(L2.Phi())
        lm_eta.append(L2.Eta())
        
    df["pll_z"] = pll_z
    
    df["lp_pt"] = lp_pt
    df["lp_phi"] = lp_phi
    df["lp_eta"] = lp_eta
    df["lp_px"] = lp_px
    df["lp_py"] = lp_py
    df["lp_pz"] = lp_pz
    df["lp_e"] = lp_e
    df["lp_pdgId"] = lp_pdgId
    
    df["lm_pt"] = lm_pt
    df["lm_phi"] = lm_phi
    df["lm_eta"] = lm_eta
    df["lm_px"] = lm_px
    df["lm_py"] = lm_py
    df["lm_pz"] = lm_pz
    df["lm_e"] = lm_e
    df["lm_pdgId"] = lm_pdgId
    
    df.loc[:, "ll_px"] = df.lp_px + df.lm_px
    df.loc[:, "ll_py"] = df.lp_py + df.lm_py
    df.loc[:, "ll_pz"] = df.lp_pz + df.lm_pz
    
    df.loc[:, "llm_px"] = df.lp_px + df.lm_px + df.met_x
    df.loc[:, "llm_py"] = df.lp_py + df.lm_py + df.met_y
    df.loc[:, "llm_pz"] = df.lp_pz + df.lm_pz - df.MET_pt


    df.loc[:, "D_00"] = D_00
    df.loc[:, "D_TT"] = D_TT
    df.loc[:, "D_0T"] = D_0T
    df.loc[:, "D_T0"] = D_T0


    df.to_pickle("dataset_HWW_ME.pkl")

    
