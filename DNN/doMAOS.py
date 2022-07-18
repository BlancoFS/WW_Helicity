#!/usr/bin/env python
import os
import glob
import numpy as np
import pandas as pd
import ROOT
import sys


###################################################
##                                               ##
### COMPUTE POLARIZED FRACTIONS FOR WW ANALYSIS ### 
##                                               ##
###################################################


##
## L1 (muon), L2 (electron), P1(neutrino muon), P2(neutrino electron)
##
##


# Phi_0 function 
def phi_0(LL, MET):
    
    phi_00 = np.arccos( (LL.Px()*MET.Px() + LL.Py()*MET.Py()) / (LL.Pt() * MET.Pt()))
    
    return phi_00


# c coefficient for second order equation
def c(L2, MET):
    
    c_val = (L2.Px()*MET.Px() + L2.Py()*MET.Py())*(L2.Px()*MET.Px() + L2.Py()*MET.Py()) - MET.Pt()*MET.Pt()*L2.Pt()*L2.Pt()
    
    return c_val


# f(phi) function
def f(L1, L2, LL, phi):
    
    f_val = L1.Pt()*L1.Pt() + (LL.Pt()*LL.Pt())*(np.cos(phi)*np.cos(phi)) - 2 * L1.Pt()*LL.Pt()*np.cos(phi) - L2.Pt()*L2.Pt()
    
    return f_val


# g(phi) function
def g(L1, L2, LL, MET, phi):
    
    phi_00 = phi_0(LL, MET)
    
    g_val = 2 * (L1.Pt() - LL.Pt()*np.cos(phi))* (L2.Px()*MET.Px() + L2.Py()*MET.Py()) + 2 * (L2.Pt()*L2.Pt()) * (MET.Pt()) * np.cos(phi + phi_00)

    return g_val


def P1(L1, L2, LL, MET, phi):

    t = f(L1, L2, LL, phi)
    tt = g(L1, L2, LL, MET, phi)*g(L1, L2, LL, MET, phi) - 4*c(L2, MET)*f(L1, L2, LL, phi)

    #print("Value of t: ")
    #print(t)
    #print("\n")

    if (type(t)==np.array or type(tt)==np.array):
        return [-999.9, -999.9]
    elif (t == 0):
        return [-999.9, -999.9]
    elif (tt == 0):
        return [-999.9, -999.9]
    elif (tt < 0):
        return [-999.9, -999.9]
    else:
        result_plus = (-1*g(L1, L2, LL, MET, phi) + np.sqrt(g(L1, L2, LL, MET, phi)*g(L1, L2, LL, MET, phi) - 4*c(L2, MET)*f(L1, L2, LL, phi)))/(2 * f(L1, L2, LL, phi))
        result_minus = (-1*g(L1, L2, LL, MET, phi) - np.sqrt(g(L1, L2, LL, MET, phi)*g(L1, L2, LL, MET, phi) - 4*c(L2, MET)*f(L1, L2, LL, phi)))/(2 * f(L1, L2, LL, phi))
        return [result_plus, result_minus]




if __name__ == "__main__":
    
    df = pd.read_pickle("dataset_HWW.pkl")

    #df = df.loc[0:10]

    #df = df.loc[280000:290000]
    #df = df.reset_index()
    
    print("\n")
    print("===========================================")
    print("Running MAOS (mT2 assisted on-shell method)")
    print("===========================================")
        
    positive_phi = []
    negative_phi = []
    absolute_phi = []
    
    positive_numu_px = []
    negative_numu_px = []
    absolute_numu_px = []
    
    positive_nuel_px = []
    negative_nuel_px = []
    absolute_nuel_px = []
    
    positive_numu_py = []
    negative_numu_py = []
    absolute_numu_py = []
    
    positive_nuel_py = []
    negative_nuel_py = []
    absolute_nuel_py = []
    
    cos_theta_p = []
    cos_theta_m = []
    
    cos_theta_p_gen = []
    cos_theta_m_gen = []

    pos_cos_theta_p = []
    pos_cos_theta_m = []
    
    neg_cos_theta_p = []
    neg_cos_theta_m = []

    positive_nup_px = []
    negative_nup_px = []
    absolute_nup_px = []
    positive_num_px = []
    negative_num_px = []
    absolute_num_px = []
    positive_nup_py = []
    negative_nup_py = []
    absolute_nup_py = []
    positive_num_py = []
    negative_num_py = []
    absolute_num_py = []

    
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
    
    phi_l = np.linspace(0.0, 3.14, 500)
    
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
        
        
        ### Numerical solution
        
        mt1_p = []
        mt1_m = []
        
        for phi_i in phi_l:
            
            result = P1(L1, L2, LL, MET, phi_i)
            
            #mt1_p.append( 2 * L1.Pt() * result[0] - (L1.Px()*(result[0]*np.cos(phi_i)) + L1.Py()*(result[0]*np.sin(phi_i))))
            #mt1_m.append( 2 * L1.Pt() * result[1] - (L1.Px()*(result[1]*np.cos(phi_i)) + L1.Py()*(result[1]*np.sin(phi_i))))
            
            if result[0] < 0:
                mt1_p.append(np.NaN)
            else:
                mt1_p.append( 2 * (L1.Pt() * result[0] - L1.Px()*(result[0]*np.cos(phi_i)) + L1.Py()*(result[0]*np.sin(phi_i))))
                
            if result[1] < 0:
                mt1_m.append( 2 * (L1.Pt() * abs(result[1]) - L1.Px()*(abs(result[1])*np.cos(phi_i)) + L1.Py()*(abs(result[1])*np.sin(phi_i))))
            else:
                mt1_m.append( 2 * (L1.Pt() * result[1] - L1.Px()*(result[1]*np.cos(phi_i)) + L1.Py()*(result[1]*np.sin(phi_i))))
                    
                
        test_p = pd.DataFrame()
        test_m = pd.DataFrame()
        
        
        test_p["phi"] = phi_l
        test_p["mT1_p"] = mt1_p
        test_m["phi"] = phi_l
        test_m["mT1_m"] = mt1_m
        
        test_p.dropna(inplace=True) 
        test_m.dropna(inplace=True) 

        index_min_m = -1
        index_min_p = -1
        
        mT1_val_p = test_p.mT1_p.values
        if (len(mT1_val_p)==0):
            min_mT1_p = -999.9
            phi_min_p = -999.9
        else:
            min_mT1_p = min(mT1_val_p)
            index_min_p = np.where(mT1_val_p==min_mT1_p)
            if (len(index_min_p[0])>1):
                phi_min_p = test_p.phi.values[index_min_p[0][0]]
            else:
                phi_min_p = test_p.phi.values[index_min_p]
            
        mT1_val_m = test_m.mT1_m.values
        if (len(mT1_val_m)==0):
            min_mT1_m = -999.9
            phi_min_m = -999.9
        else:
            min_mT1_m = min(mT1_val_m)
            index_min_m = np.where(mT1_val_m==min_mT1_m)
            if (len(index_min_m[0])>1):
                phi_min_m = test_m.phi.values[index_min_m[0][0]]
            else:
                phi_min_m = test_m.phi.values[index_min_m]
                
        #print("Phi min values: ")
        #print(phi_min_m)
        #print(phi_min_p)
        #print("Index: ")
        #print(index_min_m)
        #print(index_min_p)


        if (min_mT1_p<min_mT1_m or min_mT1_m<0.0):
            absolute = 'positive'
        else:
            absolute = 'negative'
                
            
        positive_phi.append(phi_min_p)
        negative_phi.append(phi_min_m)
        
        p1_p = P1(L1, L2, LL, MET, phi_min_p)[0]
        p1_m = P1(L1, L2, LL, MET, phi_min_m)[1]
        
        # Muon neutrino transverse momemta
        positive_numu_px.append(p1_p*np.cos(phi_min_p))
        negative_numu_px.append(p1_m*np.cos(phi_min_m))
        
        positive_numu_py.append(p1_p*np.sin(phi_min_p))
        negative_numu_py.append(p1_m*np.sin(phi_min_m))
        
        # electron neutrino transverse momemta
        positive_nuel_px.append(MET.Px() - p1_p*np.cos(phi_min_p))
        negative_nuel_px.append(MET.Px() - p1_m*np.cos(phi_min_m))
        
        positive_nuel_py.append(MET.Py() - p1_p*np.sin(phi_min_p))
        negative_nuel_py.append(MET.Py() - p1_m*np.sin(phi_min_m))
        

        if (absolute=='positive'):
            
            absolute_phi.append(phi_min_p)
            absolute_numu_px.append(p1_p*np.cos(phi_min_p))
            absolute_numu_py.append(p1_p*np.sin(phi_min_p))
            absolute_nuel_px.append(MET.Px() - p1_p*np.cos(phi_min_p))
            absolute_nuel_py.append(MET.Py() - p1_p*np.sin(phi_min_p))
        
        else:
            
            absolute_phi.append(phi_min_m)
            absolute_numu_px.append(p1_m*np.cos(phi_min_m))
            absolute_numu_py.append(p1_m*np.sin(phi_min_m))
            absolute_nuel_px.append(MET.Px() - p1_m*np.cos(phi_min_m))
            absolute_nuel_py.append(MET.Py() - p1_m*np.sin(phi_min_m))
        
        
        nu_p = ROOT.TLorentzVector(0.0, 0.0, 0.0, 0.0)
        nu_m = ROOT.TLorentzVector(0.0, 0.0, 0.0, 0.0)
        neg_nu_p = ROOT.TLorentzVector(0.0, 0.0, 0.0, 0.0)
        neg_nu_m = ROOT.TLorentzVector(0.0, 0.0, 0.0, 0.0)
        pos_nu_p = ROOT.TLorentzVector(0.0, 0.0, 0.0, 0.0)
        pos_nu_m = ROOT.TLorentzVector(0.0, 0.0, 0.0, 0.0)
        l_p = ROOT.TLorentzVector(0.0, 0.0, 0.0, 0.0)
        l_m = ROOT.TLorentzVector(0.0, 0.0, 0.0, 0.0)
        
        
        if (Lepton_pdgId_0 < 0):
            l_p.SetPtEtaPhiM(Lepton_pt_0, Lepton_eta_0, Lepton_phi_0, 0.0)
            l_m.SetPtEtaPhiM(Lepton_pt_1, Lepton_eta_1, Lepton_phi_1, 0.0)
            
            lp_pdgId = Lepton_pdgId_0
            lm_pdgId = Lepton_pdgId_1
        
        else:
            l_m.SetPtEtaPhiM(Lepton_pt_0, Lepton_eta_0, Lepton_phi_0, 0.0)
            l_p.SetPtEtaPhiM(Lepton_pt_1, Lepton_eta_1, Lepton_phi_1, 0.0)
            
            lp_pdgId = Lepton_pdgId_1
            lm_pdgId = Lepton_pdgId_0
            
            
        if abs(lp_pdgId)==13:
            
            nu_p.SetPxPyPzE(absolute_numu_px[event], absolute_numu_py[event], 0.0, (np.sqrt(absolute_numu_px[event]*absolute_numu_px[event]+absolute_numu_py[event]*absolute_numu_py[event]+30.0**2)))
            nu_m.SetPxPyPzE(absolute_nuel_px[event], absolute_nuel_py[event], 0.0, (np.sqrt(absolute_nuel_px[event]*absolute_nuel_px[event]+absolute_nuel_py[event]*absolute_nuel_py[event]+30.0**2)))
            
            pos_nu_p.SetPxPyPzE(positive_numu_px[event], positive_numu_py[event], 0.0, (np.sqrt(positive_numu_px[event]*positive_numu_px[event]+positive_numu_py[event]*positive_numu_py[event]+30.0**2)))
            pos_nu_m.SetPxPyPzE(positive_nuel_px[event], positive_nuel_py[event], 0.0, (np.sqrt(positive_nuel_px[event]*positive_nuel_px[event]+positive_nuel_py[event]*positive_nuel_py[event]+30.0**2)))
            neg_nu_p.SetPxPyPzE(negative_numu_px[event], negative_numu_py[event], 0.0, (np.sqrt(negative_numu_px[event]*negative_numu_px[event]+negative_numu_py[event]*negative_numu_py[event]+30.0**2)))
            neg_nu_m.SetPxPyPzE(negative_nuel_px[event], negative_nuel_py[event], 0.0, (np.sqrt(negative_nuel_px[event]*negative_nuel_px[event]+negative_nuel_py[event]*negative_nuel_py[event]+30.0**2)))


            positive_nup_px.append(positive_numu_px[event])
            negative_nup_px.append(negative_numu_px[event])
            absolute_nup_px.append(absolute_numu_px[event])
            positive_num_px.append(positive_nuel_px[event])
            negative_num_px.append(negative_nuel_px[event])
            absolute_num_px.append(absolute_nuel_px[event])
            positive_nup_py.append(positive_numu_py[event])
            negative_nup_py.append(negative_numu_py[event])
            absolute_nup_py.append(absolute_numu_py[event])
            positive_num_py.append(positive_nuel_py[event])
            negative_num_py.append(negative_nuel_py[event])
            absolute_num_py.append(absolute_nuel_py[event])
            
        else:
            
            nu_m.SetPxPyPzE(absolute_numu_px[event], absolute_numu_py[event], 0.0, (np.sqrt(absolute_numu_px[event]*absolute_numu_px[event]+absolute_numu_py[event]*absolute_numu_py[event]+30.0**2)))
            nu_p.SetPxPyPzE(absolute_nuel_px[event], absolute_nuel_py[event], 0.0, (np.sqrt(absolute_nuel_px[event]*absolute_nuel_px[event]+absolute_nuel_py[event]*absolute_nuel_py[event]+30.0**2)))
            
            pos_nu_m.SetPxPyPzE(positive_numu_px[event], positive_numu_py[event], 0.0, (np.sqrt(positive_numu_px[event]*positive_numu_px[event]+positive_numu_py[event]*positive_numu_py[event]+30.0**2)))
            pos_nu_p.SetPxPyPzE(positive_nuel_px[event], positive_nuel_py[event], 0.0, (np.sqrt(positive_nuel_px[event]*positive_nuel_px[event]+positive_nuel_py[event]*positive_nuel_py[event]+30.0**2)))
            neg_nu_m.SetPxPyPzE(negative_numu_px[event], negative_numu_py[event], 0.0, (np.sqrt(negative_numu_px[event]*negative_numu_px[event]+negative_numu_py[event]*negative_numu_py[event]+30.0**2)))
            neg_nu_p.SetPxPyPzE(negative_nuel_px[event], negative_nuel_py[event], 0.0, (np.sqrt(negative_nuel_px[event]*negative_nuel_px[event]+negative_nuel_py[event]*negative_nuel_py[event]+30.0**2)))

            positive_nup_px.append(positive_nuel_px[event])
            negative_nup_px.append(negative_nuel_px[event])
            absolute_nup_px.append(absolute_nuel_px[event])
            positive_num_px.append(positive_numu_px[event])
            negative_num_px.append(negative_numu_px[event])
            absolute_num_px.append(absolute_numu_px[event])
            positive_nup_py.append(positive_nuel_py[event])
            negative_nup_py.append(negative_nuel_py[event])
            absolute_nup_py.append(absolute_nuel_py[event])
            positive_num_py.append(positive_numu_py[event])
            negative_num_py.append(negative_numu_py[event])
            absolute_num_py.append(absolute_numu_py[event])
            
            
            

            
        Wp = ROOT.Math.PtEtaPhiEVector()
        Wm = ROOT.Math.PtEtaPhiEVector()
        genlp   = ROOT.Math.PtEtaPhiEVector()
        genlm = ROOT.Math.PtEtaPhiEVector()
        gennup = ROOT.Math.PtEtaPhiEVector()
        gennum = ROOT.Math.PtEtaPhiEVector()
        vector_lp = ROOT.TLorentzVector()
        vector_lm = ROOT.TLorentzVector()
        vector_nup = ROOT.TLorentzVector()
        vector_num = ROOT.TLorentzVector()
        
        genWp = ROOT.Math.PtEtaPhiEVector()
        genWm = ROOT.Math.PtEtaPhiEVector()
        vector_Wp = ROOT.TLorentzVector()
        vector_Wm = ROOT.TLorentzVector()
        
        number_elec = 0
        number_muon = 0
        number_tau = 0
        
        pos_wp = 999
        pos_wm = 999
    
        
        particles = GenPart_pdgId
        pos_mother = GenPartgenPartIdxMother
        
        
        for p in range(len(particles)):
            
            if (particles[p]==11 and particles[pos_mother[p]]==-24 and particles[pos_mother[pos_mother[p]]]!=15):
                pos_wm = pos_mother[p]
                number_elec = number_elec + 1
                vector_lm.SetPtEtaPhiM(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], 0.0)
                genlm.SetCoordinates(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], vector_lm.E())
                
            elif (particles[p]==-11 and particles[pos_mother[p]]==24 and particles[pos_mother[pos_mother[p]]]!=-15):
                pos_wp = pos_mother[p]
                number_elec = number_elec + 1
                vector_lp.SetPtEtaPhiM(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], 0.0)
                genlp.SetCoordinates(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], vector_lp.E())
                
            elif (particles[p]==13 and particles[pos_mother[p]]==-24 and particles[pos_mother[pos_mother[p]]]!=15):
                pos_wm = pos_mother[p]
                number_muon = number_muon + 1
                vector_lm.SetPtEtaPhiM(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], 0.0)
                genlm.SetCoordinates(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], vector_lm.E())
                
            elif (particles[p]==-13 and particles[pos_mother[p]]==24 and particles[pos_mother[pos_mother[p]]]!=-15):
                pos_wp = pos_mother[p]
                number_muon = number_muon + 1
                vector_lp.SetPtEtaPhiM(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], 0.0)
                genlp.SetCoordinates(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], vector_lp.E())
                
                
            elif (particles[p]==15 and particles[pos_mother[p]]==-24):
                pos_wm = pos_mother[p]
                number_tau = number_tau + 1
                vector_lm.SetPtEtaPhiM(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], 0.0)
                genlm.SetCoordinates(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], vector_lm.E())
                
            elif (particles[p]==-15 and particles[pos_mother[p]]==24):
                pos_wp = pos_mother[p]
                number_tau = number_tau + 1
                vector_lp.SetPtEtaPhiM(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], 0.0)
                genlp.SetCoordinates(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], vector_lp.E())

            
            if (particles[p]==-12 and particles[pos_mother[p]]==-24 and particles[pos_mother[pos_mother[p]]]!=15):
                vector_num.SetPtEtaPhiM(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], 0.0)
                gennum.SetCoordinates(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], vector_num.E())
                
            elif (particles[p]==12 and particles[pos_mother[p]]==24 and particles[pos_mother[pos_mother[p]]]!=-15):
                vector_nup.SetPtEtaPhiM(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], 0.0)
                gennup.SetCoordinates(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], vector_nup.E())
                
            elif (particles[p]==-14 and particles[pos_mother[p]]==-24 and particles[pos_mother[pos_mother[p]]]!=15):
                vector_num.SetPtEtaPhiM(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], 0.0)
                gennum.SetCoordinates(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], vector_num.E())
                
            elif (particles[p]==14 and particles[pos_mother[p]]==24 and particles[pos_mother[pos_mother[p]]]!=-15):
                vector_nup.SetPtEtaPhiM(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], 0.0)
                gennup.SetCoordinates(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], vector_nup.E())
                
            elif (particles[p]==-16 and particles[pos_mother[p]]==-24):
                vector_num.SetPtEtaPhiM(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], 0.0)
                gennum.SetCoordinates(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], vector_num.E())
    
            elif (particles[p]==16 and particles[pos_mother[p]]==24):
                vector_nup.SetPtEtaPhiM(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], 0.0)
                gennup.SetCoordinates(GenPart_pt[p], GenPart_eta[p], GenPart_phi[p], vector_nup.E())
                
        vector_Wp.SetPtEtaPhiM(GenPart_pt[pos_wp], GenPart_eta[pos_wp], GenPart_phi[pos_wp], GenPart_mass[pos_wp]) # W plus                                                           
        genWp.SetCoordinates(GenPart_pt[pos_wp], GenPart_eta[pos_wp], GenPart_phi[pos_wp], vector_Wp.E())
        

        vector_Wm.SetPtEtaPhiM(GenPart_pt[pos_wm], GenPart_eta[pos_wm], GenPart_phi[pos_wm], GenPart_mass[pos_wm]) # W minus                                                          
        genWm.SetCoordinates(GenPart_pt[pos_wm], GenPart_eta[pos_wm], GenPart_phi[pos_wm], vector_Wm.E())
        
        if (((number_elec==0 or number_muon==0) and number_tau==0) or pos_wp==999 or pos_wm==999):
            cos_theta_p_gen.append(-9999)
            cos_theta_m_gen.append(-9999)
            #weight_LL.append(-9999)
            #weight_TL.append(-9999)
            #weight_LT.append(-9999)
            #weight_TT.append(-9999)
            #cos_theta_p.append(-9999)
            #cos_theta_m.append(-9999)
            pos_cos_theta_p.append(-9999)
            pos_cos_theta_m.append(-9999)
            neg_cos_theta_p.append(-9999)
            neg_cos_theta_m.append(-9999)
            continue
        
        
        pos_W_p = l_p + pos_nu_p
        pos_W_m = l_m + pos_nu_m

        neg_W_p = l_p + neg_nu_p
        neg_W_m = l_m + neg_nu_m

                
        
        reclp = ROOT.Math.PtEtaPhiEVector()
        reclm = ROOT.Math.PtEtaPhiEVector()
        recWp = ROOT.Math.PtEtaPhiEVector()
        recWm = ROOT.Math.PtEtaPhiEVector()
        
        recWp_pos = ROOT.Math.PtEtaPhiEVector()
        recWm_pos = ROOT.Math.PtEtaPhiEVector()

        recWp_neg = ROOT.Math.PtEtaPhiEVector()
        recWm_neg = ROOT.Math.PtEtaPhiEVector()

        reclp.SetCoordinates(l_p.Pt(), l_p.Eta(), l_p.Phi(), l_p.E())
        reclm.SetCoordinates(l_m.Pt(), l_m.Eta(), l_m.Phi(), l_m.E())

        recWp_pos.SetCoordinates(pos_W_p.Pt(), pos_W_p.Eta(), pos_W_p.Phi(), pos_W_p.E())
        recWm_pos.SetCoordinates(pos_W_m.Pt(), pos_W_m.Eta(), pos_W_m.Phi(), pos_W_m.E())
        
        recWp_neg.SetCoordinates(neg_W_p.Pt(), neg_W_p.Eta(), neg_W_p.Phi(), neg_W_p.E())
        recWm_neg.SetCoordinates(neg_W_m.Pt(), neg_W_m.Eta(), neg_W_m.Phi(), neg_W_m.E())

        reclp.SetCoordinates(l_p.Pt(), l_p.Eta(), l_p.Phi(), l_p.E())
        reclm.SetCoordinates(l_m.Pt(), l_m.Eta(), l_m.Phi(), l_m.E())
        
        recwmRF = ROOT.Math.XYZVector()
        recwpRF = ROOT.Math.XYZVector()
        
        recwpRF = recWp.BoostToCM()
        recwmRF = recWm.BoostToCM()

        recwmRF_pos = ROOT.Math.XYZVector()
        recwpRF_pos = ROOT.Math.XYZVector()

        recwpRF_pos = recWp_pos.BoostToCM()
        recwmRF_pos = recWm_pos.BoostToCM()
        
        recwmRF_neg = ROOT.Math.XYZVector()
        recwpRF_neg = ROOT.Math.XYZVector()

        recwpRF_neg = recWp_neg.BoostToCM()
        recwmRF_neg = recWm_neg.BoostToCM()

        # Positive solution

        leppWRF_pos = ROOT.Math.XYZVector()
        lepmWRF_pos = ROOT.Math.XYZVector()
        leppWRF_pos = ROOT.Math.VectorUtil.boost(reclp, recwpRF_pos)
        lepmWRF_pos = ROOT.Math.VectorUtil.boost(reclm, recwmRF_pos)

        pos_theta_Wp_star = ROOT.Math.VectorUtil.Angle(leppWRF_pos, recWp_pos)
        pos_theta_Wm_star = ROOT.Math.VectorUtil.Angle(lepmWRF_pos, recWm_pos)

        pos_cos_Wp_theta_star = np.cos(pos_theta_Wp_star)
        pos_cos_Wm_theta_star = np.cos(pos_theta_Wm_star)

        pos_cos_theta_p.append(pos_cos_Wp_theta_star)
        pos_cos_theta_m.append(pos_cos_Wm_theta_star)

        # Negative solution
        
        leppWRF_neg = ROOT.Math.XYZVector()
        lepmWRF_neg = ROOT.Math.XYZVector()
        leppWRF_neg = ROOT.Math.VectorUtil.boost(reclp, recwpRF_neg)
        lepmWRF_neg = ROOT.Math.VectorUtil.boost(reclm, recwmRF_neg)

        neg_theta_Wp_star = ROOT.Math.VectorUtil.Angle(leppWRF_neg, recWp_neg)
        neg_theta_Wm_star = ROOT.Math.VectorUtil.Angle(lepmWRF_neg, recWm_neg)

        neg_cos_Wp_theta_star = np.cos(neg_theta_Wp_star)
        neg_cos_Wm_theta_star = np.cos(neg_theta_Wm_star)

        neg_cos_theta_p.append(neg_cos_Wp_theta_star)
        neg_cos_theta_m.append(neg_cos_Wm_theta_star)
        
        
        wmRF_gen = ROOT.Math.XYZVector()
        wpRF_gen = ROOT.Math.XYZVector()
        
        wmRF_gen = genWm.BoostToCM()
        wpRF_gen = genWp.BoostToCM()
        
        leppWRF = ROOT.Math.XYZVector()
        lepmWRF = ROOT.Math.XYZVector()
        leppWRF = ROOT.Math.VectorUtil.boost(genlp, wpRF_gen)
        lepmWRF = ROOT.Math.VectorUtil.boost(genlm, wmRF_gen)
        
        theta_Wp_star_gen = ROOT.Math.VectorUtil.Angle(leppWRF, genWp)
        theta_Wm_star_gen = ROOT.Math.VectorUtil.Angle(lepmWRF, genWm)
        
        cos_Wp_theta_star_gen = np.cos(theta_Wp_star_gen)
        cos_Wm_theta_star_gen = np.cos(theta_Wm_star_gen)
        
        cos_theta_p_gen.append(cos_Wp_theta_star_gen)
        cos_theta_m_gen.append(cos_Wm_theta_star_gen)

    
    df["positive_phi"] = positive_phi
    df["negative_phi"] = negative_phi
    df["absolute_phi"] = absolute_phi
  
    df["positive_numu_px"] = positive_numu_px
    df["negative_numu_px"] = negative_numu_px
    df["absolute_numu_px"] = absolute_numu_px
    df["positive_nuel_px"] = positive_nuel_px
    df["negative_nuel_px"] = negative_nuel_px
    df["absolute_nuel_px"] = absolute_nuel_px
    df["positive_numu_py"] = positive_numu_py
    df["negative_numu_py"] = negative_numu_py
    df["absolute_numu_py"] = absolute_numu_py
    df["positive_nuel_py"] = positive_nuel_py
    df["negative_nuel_py"] = negative_nuel_py
    df["absolute_nuel_py"] = absolute_nuel_py
        
    
    #df["cos_theta_p"] = cos_theta_p
    #df["cos_theta_m"] = cos_theta_m
    df["cos_theta_p_gen"] = cos_theta_p_gen
    df["cos_theta_m_gen"] = cos_theta_m_gen  

    df["pos_cos_theta_p"] = pos_cos_theta_p
    df["pos_cos_theta_m"] = pos_cos_theta_m
    
    df["neg_cos_theta_p"] = neg_cos_theta_p
    df["neg_cos_theta_m"] = neg_cos_theta_m

    df["positive_nup_px"] = positive_nup_px
    df["negative_nup_px"] = negative_nup_px
    df["absolute_nup_px"] = absolute_nup_px
    df["positive_num_px"] = positive_num_px
    df["negative_num_px"] = negative_num_px
    df["absolute_num_px"] = absolute_num_px
    df["positive_nup_py"] = positive_nup_py
    df["negative_nup_py"] = negative_nup_py
    df["absolute_nup_py"] = absolute_nup_py
    df["positive_num_py"] = positive_num_py
    df["negative_num_py"] = negative_num_py
    df["absolute_num_py"] = absolute_num_py

    #df["nup_px"] = nup_px
    #df["nup_py"] = nup_py
    #df["nup_pz"] = nup_pz
    
    #df["num_px"] = num_px
    #df["num_py"] = num_py
    #df["num_pz"] = num_pz

    
    df.to_pickle("dataset_HWW_MAOS.pkl")
