#!/usr/bin/env python
import os
import glob
import numpy as np
import pandas as pd
import ROOT
import sys


##
## L1 (muon), L2 (electron), P1(neutrino muon), P2(neutrino electron)
##
##



if __name__ == "__main__":
    
    df = pd.read_pickle("dataset_ww.pkl")

    #df = df.loc[280000:290000]
    #df = df.reset_index()
    
    print("\n")
    print("======================================")
    print("    Running cos theta star maker")
    print("======================================")
    
    
    cos_theta_p = []
    cos_theta_m = []
    
    cos_theta_p_gen = []
    cos_theta_m_gen = []
    
    
    nu1_pt = df["NeutrinoGen_pt[0]"].values
    nu2_pt = df["NeutrinoGen_pt[1]"].values
    
    nu1_phi = df["NeutrinoGen_phi[0]"].values
    nu2_phi = df["NeutrinoGen_phi[1]"].values
    
    nu1_eta = df["NeutrinoGen_eta[0]"].values
    nu2_eta = df["NeutrinoGen_eta[1]"].values
    
    nu1_pdgId = df["NeutrinoGen_pdgId[0]"].values
    nu2_pdgId = df["NeutrinoGen_pdgId[1]"].values
    
    nup_px = []
    num_px = []
    
    nup_py = []
    num_py = []
    
    nup_pz = []
    num_pz = []
        
    print("\n")
    print("0 Events completed from " + str(len(df)))
    
    
    for event in range(0, len(df)):
        
        if (event%10000==0):
            print("\n")
            print(str(event) + " Events completed from " + str(len(df)))
          
            
        tmp = df.loc[event]

        # Get GenParticles as input 

        GenPart_eta = tmp.GenPart_eta
        GenPart_pt = tmp.GenPart_pt
        GenPart_mass = tmp.GenPart_mass
        GenPart_phi = tmp.GenPart_phi
        GenPartgenPartIdxMother = tmp.GenPart_genPartIdxMother
        GenPart_status = tmp.GenPart_status
        GenPart_pdgId = tmp.GenPart_pdgId
        
        Lepton_pt_0 = tmp["Lepton_pt[0]"]
        Lepton_phi_0 = tmp["Lepton_phi[0]"]
        Lepton_eta_0 = tmp["Lepton_eta[0]"]
        Lepton_pdgId_0 = tmp["Lepton_pdgId[0]"]
        
        Lepton_pt_1 = tmp["Lepton_pt[1]"]
        Lepton_phi_1 = tmp["Lepton_phi[1]"]
        Lepton_eta_1 = tmp["Lepton_eta[1]"]
        Lepton_pdgId_1 = tmp["Lepton_pdgId[1]"]
        
        met_pt = tmp.PuppiMET_pt
        met_phi = tmp.PuppiMET_phi
        
        met_x = met_pt * np.cos(met_phi)
        met_y = met_pt * np.sin(met_phi)
        
        L1 = ROOT.TLorentzVector(0.0, 0.0, 0.0, 0.0)
        L2 = ROOT.TLorentzVector(0.0, 0.0, 0.0, 0.0)
        LL = ROOT.TLorentzVector(0.0, 0.0, 0.0, 0.0)
        MET = ROOT.TLorentzVector(0.0, 0.0, 0.0, 0.0)
        
        if (abs(Lepton_pdgId_0)==13):
            L1.SetPtEtaPhiM(Lepton_pt_0, Lepton_eta_0, Lepton_phi_0, 0.0)
            L2.SetPtEtaPhiM(Lepton_pt_1, Lepton_eta_1, Lepton_phi_1, 0.0)
        else:
            L2.SetPtEtaPhiM(Lepton_pt_0, Lepton_eta_0, Lepton_phi_0, 0.0)
            L1.SetPtEtaPhiM(Lepton_pt_1, Lepton_eta_1, Lepton_phi_1, 0.0)
            
        LL = L1 + L2
        
        met_e = np.sqrt(met_x*met_x + met_y*met_y + 30.0*30.0)
        MET.SetPxPyPzE(met_x, met_y, 0.0, met_e)
        


        ROOT.gROOT.ProcessLineSync(".L /afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/WW/Full2016_v7/WW_helicity/DNN/CosThetaWW.C+")

        if (Lepton_pdgId_0 < 0):            
            result_cos = ROOT.CosThetaWW(Lepton_pt_0, Lepton_eta_0, Lepton_phi_0, Lepton_pt_1, Lepton_eta_1, Lepton_phi_1, met_x, met_y)
        else:
            result_cos = ROOT.CosThetaWW(Lepton_pt_1, Lepton_eta_1, Lepton_phi_1, Lepton_pt_0, Lepton_eta_0, Lepton_phi_0, met_x, met_y)

        cos_theta_p.append(result_cos[0])
        cos_theta_m.append(result_cos[1])
            
            
        Nu1 = ROOT.TLorentzVector(0.0, 0.0, 0.0, 0.0)
        Nu2 = ROOT.TLorentzVector(0.0, 0.0, 0.0, 0.0)
    
        #print(nu2_pt[event])
        #print(nu2_phi[event])
        #print(nu2_eta[event])

        if (len(nu2_pt[event])==0 or len(nu2_eta[event])==0 or len(nu2_phi[event])==0):
            Nu1.SetPtEtaPhiM(0.0, 0.0, 0.0, 0.0)
        elif (len(nu1_pt[event])==0 or len(nu1_eta[event])==0 or len(nu1_phi[event])==0):
            Nu1.SetPtEtaPhiM(0.0, 0.0, 0.0, 0.0)
        elif (nu1_pdgId[event]>0):    
            Nu1.SetPtEtaPhiM(nu1_pt[event], nu1_eta[event], nu1_phi[event], 0.0)
            Nu2.SetPtEtaPhiM(nu2_pt[event], nu2_eta[event], nu2_phi[event], 0.0)
        else:
            Nu2.SetPtEtaPhiM(nu1_pt[event], nu1_eta[event], nu1_phi[event], 0.0)
            Nu1.SetPtEtaPhiM(nu2_pt[event], nu2_eta[event], nu2_phi[event], 0.0)
            
        nup_px.append(Nu1.Px())
        nup_py.append(Nu1.Py())
        nup_pz.append(Nu1.Pz())
        
        num_px.append(Nu2.Px())
        num_py.append(Nu2.Py())
        num_pz.append(Nu2.Pz())
    
        gennu_p = ROOT.TLorentzVector(0.0, 0.0, 0.0, 0.0)
        gennu_m = ROOT.TLorentzVector(0.0, 0.0, 0.0, 0.0)
        
        gen_e_p = np.sqrt(nup_px[event]*nup_px[event] + nup_py[event]*nup_py[event] + nup_pz[event]*nup_pz[event] + 30.0*30.0)
        gen_e_m = np.sqrt(num_px[event]*num_px[event] + num_py[event]*num_py[event] + num_pz[event]*num_pz[event] + 30.0*30.0)
        
        gennu_p.SetPxPyPzE(nup_px[event], nup_py[event], nup_pz[event], gen_e_p)
        gennu_m.SetPxPyPzE(num_px[event], num_py[event], num_pz[event], gen_e_m)
        
        
        genWp = ROOT.Math.PtEtaPhiEVector()
        genWm = ROOT.Math.PtEtaPhiEVector()

        W_p_gen = l_p + gennu_p
        W_m_gen = l_m + gennu_m
        
        genWp.SetCoordinates(W_p_gen.Pt(), W_p_gen.Eta(), W_p_gen.Phi(), W_p_gen.E())
        genWm.SetCoordinates(W_m_gen.Pt(), W_m_gen.Eta(), W_m_gen.Phi(), W_m_gen.E())
        
                
        genwmRF = ROOT.Math.XYZVector()
        genwpRF = ROOT.Math.XYZVector()
        
        genwpRF = genWp.BoostToCM()
        genwmRF = genWm.BoostToCM()
        
        leppWRF = ROOT.Math.XYZVector()
        lepmWRF = ROOT.Math.XYZVector()
        leppWRF = ROOT.Math.VectorUtil.boost(reclp, genwpRF)
        lepmWRF = ROOT.Math.VectorUtil.boost(reclm, genwmRF)
        
        theta_Wp_star_gen = ROOT.Math.VectorUtil.Angle(leppWRF, genWp)
        theta_Wm_star_gen = ROOT.Math.VectorUtil.Angle(lepmWRF, genWm)
        
        cos_Wp_theta_star_gen = np.cos(theta_Wp_star_gen)
        cos_Wm_theta_star_gen = np.cos(theta_Wm_star_gen)
        
        cos_theta_p_gen.append(cos_Wp_theta_star_gen)
        cos_theta_m_gen.append(cos_Wm_theta_star_gen)

        
    
    df["cos_theta_p"] = cos_theta_p
    df["cos_theta_m"] = cos_theta_m
    df["cos_theta_p_gen"] = cos_theta_p_gen
    df["cos_theta_m_gen"] = cos_theta_m_gen  
  

    df.to_pickle("dataset_ww_cos.pkl")
