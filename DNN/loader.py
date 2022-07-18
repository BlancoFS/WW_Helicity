#!/usr/bin/env python
from __future__ import print_function
import pickle
import ROOT 
import numpy as np  
import pandas as pd
import sys
import os
import root_numpy



dir16 = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7/'
dir17 = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7/'
dir18 = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Autumn18_102X_nAODv7_Full2018v7/MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7/'


#
#
# WW Monte Carlo
#
#


def load_dataset_ww ( max_entries = -1 ):
  _branches = [
    "Lepton_eta[0]",
    "Lepton_eta[1]",
    "Lepton_pt[0]",
    "Lepton_pt[1]",
    "Lepton_phi[0]",
    "Lepton_phi[1]",
    "Lepton_pdgId[0]",
    "Lepton_pdgId[1]",
    "CleanJet_eta[0]",
    "CleanJet_eta[1]",
    "CleanJet_phi[0]",
    "CleanJet_phi[1]",
    "CleanJet_pt[0]",
    "CleanJet_pt[1]",
    "PuppiMET_pt",
    "PuppiMET_phi",
    "MET_pt",
    "MET_phi",
    "ptll",
    "mll",
    "mth",
    "mTi",
    "mtw1",
    "mtw2",
    "XSWeight",
    "METFilter_MC",
    "GenPart_pt", 
    "GenPart_eta", 
    "GenPart_phi", 
    "GenPart_mass", 
    "GenPart_pdgId", 
    "GenPart_status", 
    "GenPart_genPartIdxMother",
    "NeutrinoGen_phi[0]",
    "NeutrinoGen_phi[1]",
    "NeutrinoGen_eta[0]",
    "NeutrinoGen_eta[1]",
    "NeutrinoGen_pdgId[0]",
    "NeutrinoGen_pdgId[1]",
    "NeutrinoGen_pt[0]",
    "NeutrinoGen_pt[1]"]
 
  #ROOT.gROOT.ProcessLineSync(".L ./mlljj.C+")
  #ROOT.gROOT.ProcessLineSync(".L /afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/WW/Full2016_v7/WW_helicity/scripts/doPolarizationWeight.cc+")
    

  chain = ROOT.TChain('Events')
  
  '''
  chain.Add(dir16+'nanoLatino_WWTo2L2NuHerwigPS__part0.root')
  chain.Add(dir16+'nanoLatino_WWTo2L2NuHerwigPS__part1.root')
  chain.Add(dir16+'nanoLatino_WWTo2L2NuHerwigPS__part2.root')
  chain.Add(dir16+'nanoLatino_WWTo2L2NuHerwigPS__part3.root') 
  
  for i in range(7):
    chain.Add(dir16+'nanoLatino_WW-LO_ext1__part'+str(i)+'.root')

  for i in range(35):
    chain.Add(dir17+'nanoLatino_WWJTo2L2Nu_NNLOPS__part'+str(i)+'.root')

  for i in range(5):
    chain.Add(dir17+'nanoLatino_WW-LO__part'+str(i)+'.root')

  for i in range(21):
    chain.Add(dir18+'nanoLatino_WW-LO__part'+str(i)+'.root')

  chain.Add(dir18+'nanoLatino_WWJTo2L2Nu_NNLOPS__part0.root')
  chain.Add(dir18+'nanoLatino_WWJTo2L2Nu_NNLOPS__part1.root')
  chain.Add(dir18+'nanoLatino_WWJTo2L2Nu_NNLOPS__part2.root')
  '''

  # VBF                                                                                                                                                                                                                                      
  for i in range(4):
    chain.Add(dir16+'nanoLatino_VBFHToWWTo2L2NuPowheg_M125__part'+str(i)+'.root')

  for i in range(2):
    chain.Add(dir16+'nanoLatino_VBFHToWWTo2L2Nu_alternative_M125__part'+str(i)+'.root')

  for i in range(3):
    chain.Add(dir16+'nanoLatino_VBFHToWWTo2L2NuAMCNLO_M125__part'+str(i)+'.root')

  for i in range(13):
    chain.Add(dir17+'nanoLatino_VBFHToWWTo2L2Nu_M125_CP5Up__part'+str(i)+'.root')

  chain.Add(dir17+'nanoLatino_VBFHToWWTo2L2Nu_M125_CP5Up__part0.root')

  for i in range(30):
    chain.Add(dir18+'nanoLatino_VBFHToWWTo2L2Nu_M125_DipoleRecoil_private__part'+str(i)+'.root')

  
  # GGH                                                                                                                                                                                                                                      
  chain.Add(dir16+'nanoLatino_GluGluHToWWTo2L2Nu_M125__part0.root')
  chain.Add(dir16+'nanoLatino_GluGluHToWWTo2L2Nu_M125__part1.root')
  chain.Add(dir16+'nanoLatino_GluGluHToWWTo2L2Nu_M125_herwigpp__part0.root')
  chain.Add(dir16+'nanoLatino_GluGluHToWWTo2L2NuAMCNLO_M125__part0.root')
  chain.Add(dir16+'nanoLatino_GluGluHToWWTo2L2NuAMCNLO_M125__part1.root')
  chain.Add(dir16+'nanoLatino_GluGluHToWWTo2L2NuAMCNLO_M125__part2.root')

  
  for i in range(49):
    chain.Add(dir17+'nanoLatino_GluGluHToWWTo2L2Nu_Powheg_M125__part'+str(i)+'.root')


  for i in range(21):
    chain.Add(dir18+'nanoLatino_GluGluHToWWTo2L2NuPowhegNNLOPS_M125__part'+str(i)+'.root')

  '''
  # TOP
  for i in range(71):
    chain.Add(dir16+'nanoLatino_TT_TuneCUETP8M2T4__part'+str(i)+'.root')

  for i in range(11):
    chain.Add(dir17+'nanoLatino_TTTo2L2Nu__part'+str(i)+'.root')

  for i in range(6):
    chain.Add(dir17+'nanoLatino_TTTo2L2Nu_CP5Down__part'+str(i)+'.root')

  for i in range(9):
    chain.Add(dir17+'nanoLatino_TTTo2L2Nu_CP5Up__part'+str(i)+'.root')

  for i in range(8):
    chain.Add(dir18+'nanoLatino_TTTo2L2Nu_CP5Down__part'+str(i)+'.root')

  for i in range(9):
    chain.Add(dir18+'nanoLatino_TTTo2L2Nu_CP5Up__part'+str(i)+'.root')
  '''
    
  print(chain.GetEntries())

  _dataset = root_numpy.tree2array (chain, 
      #selection = 'Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13 && Lepton_pt[0] > 25. && Lepton_pt[1] > 13. && (abs(Lepton_pdgId[1]) == 13 || Lepton_pt[1] > 13.) && (nLepton >= 2 && Alt$(Lepton_pt[2], 0) < 10.) && Alt$(CleanJet_pt[1], 0) > 30. && abs(CleanJet_eta[0]) < 4.7 && abs(CleanJet_eta[1]) < 4.7 && Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.2217) == 0 && Sum$(CleanJet_pt>30) >= 2 && Sum$(CleanJet_pt>30) <= 3 && RecoMELA_VBF(Sum$(CleanJet_pt>30), nLepton, PuppiMET_pt, PuppiMET_phi, Lepton_pt[0], Lepton_pt[1], Lepton_phi[0], Lepton_phi[1], Lepton_eta[0], Lepton_eta[1], CleanJet_pt[0], CleanJet_pt[1], CleanJet_phi[0], CleanJet_phi[1], CleanJet_eta[0], CleanJet_eta[1], Lepton_pdgId[0], Lepton_pdgId[1]) > 0.2 && mth > 60 && mth < 125',
      selection = 'Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13',
      branches = _branches,
      stop = max_entries
     )

  return { b : _dataset[b] for b in _branches }




if __name__ == '__main__':
    
    
    #VARS = ["mjj", "Ctot", "Jet_qgl[0]", "Jet_qgl[1]", "detajj", "detall", "drjj", "dphill", "dphijjmet", "dphilljetjet", "drll", "Lepton_eta[0]", "Lepton_eta[1]", "Lepton_pt[0]", "Lepton_pt[1]", "Lepton_phi[0]", "Lepton_phi[1]", "CleanJet_eta[0]", "CleanJet_eta[1]", "CleanJet_phi[0]", "CleanJet_phi[1]", "CleanJet_pt[0]", "CleanJet_pt[1]", "MET_pt", "Met_phi", "mth", "mTi", "mtw2", "detal1j1", "detal1j2", "detal2j1", "detal2j2", "ptll", "mlljj", "pt_Total",  "mll", "RecoMELA_VBF"]

    #NDIM = len(VARS)

        
    print("Starting WW datasets \n")
    
    dataset_ww = load_dataset_ww(-1)
    
    print("Closing WW datasets \n")

    df_ww = pd.DataFrame(dataset_ww)
    
    df_ww.to_pickle('dataset_HWW.pkl')
    
    print(len(df_ww))
    print("Done!") 
