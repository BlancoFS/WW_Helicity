import os
import copy
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # ggH2016
configurations = os.path.dirname(configurations) # Differential
configurations = os.path.dirname(configurations) # Configurations

#aliases = {}

# imported from samples.py:
# samples, signals

mc = [skey for skey in samples if skey not in ('Fake', 'DATA', 'Dyemb')]
mc_emb = [skey for skey in samples if skey not in ('Fake', 'DATA')]

eleWP = 'mva_90p_Iso2016'
muWP = 'cut_Tight80x_tthmva_80'

aliases['LepWPCut'] = {
    'expr': 'LepCut2l__ele_'+eleWP+'__mu_'+muWP,
    'samples': mc_emb + ['DATA']
}

aliases['gstarLow'] = {
    'expr': 'Gen_ZGstar_mass >0 && Gen_ZGstar_mass < 4',
    'samples': 'VgS'
}

aliases['gstarHigh'] = {
    'expr': 'Gen_ZGstar_mass <0 || Gen_ZGstar_mass > 4',
    'samples': 'VgS'
}

aliases['embedtotal'] = {
    'expr': 'embed_total_mva16',  # wrt. eleWP
    'samples': 'Dyemb'
}

# Fake leptons transfer factor
aliases['fakeW'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP,
    'samples': ['Fake']
}
# And variations - already divided by central values in formulas !
aliases['fakeWEleUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_EleUp',
    'samples': ['Fake']
}
aliases['fakeWEleDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_EleDown',
    'samples': ['Fake']
}
aliases['fakeWMuUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_MuUp',
    'samples': ['Fake']
}
aliases['fakeWMuDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_MuDown',
    'samples': ['Fake']
}
aliases['fakeWStatEleUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statEleUp',
    'samples': ['Fake']
}
aliases['fakeWStatEleDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statEleDown',
    'samples': ['Fake']
}
aliases['fakeWStatMuUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statMuUp',
    'samples': ['Fake']
}
aliases['fakeWStatMuDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statMuDown',
    'samples': ['Fake']
}

# gen-matching to prompt only (GenLepMatch2l matches to *any* gen lepton)
aliases['PromptGenLepMatch2l'] = {
    'expr': 'Alt$(Lepton_promptgenmatched[0]*Lepton_promptgenmatched[1], 0)',
    'samples': mc
}

# Polarization weights

gen_weights = ['LL', 'TL', 'LT', 'TT', 'cos_wp', 'cos_wm', 'f0_p', 'fL_p', 'fR_p', 'f0_m', 'fL_m', 'fR_m']

for pol in gen_weights:
    aliases['WW_helRw_' + pol] = {
        'linesToAdd': ['.L /afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/WW/Full2016_v7/WW_helicity/scripts/doPolarizationWeight.cc+' ],
        'class': 'DoPolarizationWeight',
        'args': (pol,),
        'samples': mc
    }


aliases['Top_pTrw'] = {
    'expr': '(topGenPt * antitopGenPt > 0.) * (TMath::Sqrt((0.103*TMath::Exp(-0.0118*topGenPt) - 0.000134*topGenPt + 0.973) * (0.103*TMath::Exp(-0.0118*antitopGenPt) - 0.000134*antitopGenPt + 0.973))) * (TMath::Sqrt(TMath::Exp(1.61468e-03 + 3.46659e-06*topGenPt - 8.90557e-08*topGenPt*topGenPt) * TMath::Exp(1.61468e-03 + 3.46659e-06*antitopGenPt - 8.90557e-08*antitopGenPt*antitopGenPt))) + (topGenPt * antitopGenPt <= 0.)', # Same Reweighting as other years, but with additional fix for tune CUET -> CP5
    'samples': ['top']
}

#'samples': ['ttbar', 'STop']

aliases['nCleanGenJet'] = {
    'linesToAdd': ['.L /afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/Differential/ngenjet.cc+' ],
    'class': 'CountGenJet',
    'samples': mc
}

##### DY Z pT reweighting
aliases['getGenZpt_OTF'] = {
    'linesToAdd':['.L /afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/patches/getGenZpt.cc+'],
    'class': 'getGenZpt',
    'samples': ['DY']
}
handle = open('/afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/patches/DYrew30.py','r')
exec(handle)
handle.close()
aliases['DY_NLO_pTllrw'] = {
    'expr': '('+DYrew['2016']['NLO'].replace('x', 'getGenZpt_OTF')+')*(nCleanGenJet == 0)+1.0*(nCleanGenJet > 0)',
    'samples': ['DY']
}
aliases['DY_LO_pTllrw'] = {
    'expr': '('+DYrew['2016']['LO'].replace('x', 'getGenZpt_OTF')+')*(nCleanGenJet == 0)+1.0*(nCleanGenJet > 0)',
    'samples': ['DY']
}

# Jet bins
# using Alt$(CleanJet_pt[n], 0) instead of Sum$(CleanJet_pt >= 30) because jet pt ordering is not strictly followed in JES-varied samples

# No jet with pt > 30 GeV
aliases['zeroJet'] = {
    'expr': 'Alt$(CleanJet_pt[0], 0) < 30.'
}

aliases['oneJet'] = {
    'expr': 'Alt$(CleanJet_pt[0], 0) > 30.'
}

aliases['multiJet'] = {
    'expr': 'Alt$(CleanJet_pt[1], 0) > 30.'
}


#######
####### B tagging
#######

btag_algo = 'deepcsv'

if btag_algo == 'deepcsv':
    
    aliases['bVeto'] = {
        'expr': 'Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.2217) == 0'
    }
    
    aliases['bReq'] = {
        'expr': 'Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.2217) >= 1'
    }

    # CR definitions
    
    aliases['topcr'] = {
        'expr': 'mpmet>20 && PuppiMET_pt>20 && mll>20 && ptll>30 && ((zeroJet && !bVeto) || bReq)'
    }
    
    aliases['bVetoSF'] = {
        'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_deepcsv_shape[CleanJet_jetIdx]+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))',
        'samples': mc
    }

    aliases['bReqSF'] = {
        'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_deepcsv_shape[CleanJet_jetIdx]+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))',
        'samples': mc
    }
    
    aliases['btagSF'] = {
        'expr': '(bVeto || (topcr && zeroJet))*bVetoSF + (topcr && !zeroJet)*bReqSF',
        'samples': mc
    }
    
    for shift in ['jes','lf','hf','lfstats1','lfstats2','hfstats1','hfstats2','cferr1','cferr2']:
        
        for targ in ['bVeto', 'bReq']:
            alias = aliases['%sSF%sup' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
            alias['expr'] = alias['expr'].replace('btagSF_deepcsv_shape', 'btagSF_deepcsv_shape_up_%s' % shift)
            
            alias = aliases['%sSF%sdown' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
            alias['expr'] = alias['expr'].replace('btagSF_deepcsv_shape', 'btagSF_deepcsv_shape_down_%s' % shift)
            
        aliases['btagSF%sup' % shift] = {
            'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'up'),
            'samples': mc
        }
        
        aliases['btagSF%sdown' % shift] = {
            'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'down'),
            'samples': mc
        }

elif btag_algo == 'deepflav':
    
    btagSFSource = '%s/src/PhysicsTools/NanoAODTools/data/btagSF/DeepJet_2016LegacySF_V1.csv' % os.getenv('CMSSW_BASE')
    
    aliases['bVeto'] = {
        'expr': 'Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepFlavB[CleanJet_jetIdx] >  0.0614) == 0'
    }
    
    aliases['bReq'] = {
        'expr': 'Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepFlavB[CleanJet_jetIdx] >  0.0614) >= 1'
    }

    aliases['topcr'] = {
        'expr': 'mpmet>20 && PuppiMET_pt>20 && mll>20 && ptll>30 && ((zeroJet && !bVeto) || bReq)'
    }

    aliases['Jet_btagSF_deepflav_shape'] = {
        'linesToAdd': [
            'gSystem->Load("libCondFormatsBTauObjects.so");',
            'gSystem->Load("libCondToolsBTau.so");',
            'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_RELEASE_BASE'),
            '.L /afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/patches/btagsfpatch.cc+'
        ],
        'class': 'BtagSF',
        'args': (btagSFSource,'central','deepjet'),
        'samples': mc
    }
        
    aliases['bVetoSF'] = {
        'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_deepflav_shape[CleanJet_jetIdx]+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))',
        'samples': mc
    }
    
    aliases['bReqSF'] = {
        'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_deepflav_shape[CleanJet_jetIdx]+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5))))',
        'samples': mc
    }

    aliases['btagSF'] = {
        'expr': '(bVeto || (topcr && zeroJet))*bVetoSF + (topcr && !zeroJet)*bReqSF',
        'samples': mc
    }

    #'hf' 
    for shift in ['jes', 'lf','lfstats1', 'lfstats2', 'hfstats1', 'hfstats2', 'cferr1', 'cferr2']:
        aliases['Jet_btagSF_deepflav_shape_up_%s' % shift] = {
            'class': 'BtagSF',
            'args': (btagSFSource, 'up_' + shift,'deepjet'),
            'samples': mc
        }
        aliases['Jet_btagSF_deepflav_shape_down_%s' % shift] = {
            'class': 'BtagSF',
            'args': (btagSFSource, 'down_' + shift,'deepjet'),
            'samples': mc
        }
        
        for targ in ['bVeto', 'bReq']:
            alias = aliases['%sSF%sup' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
            alias['expr'] = alias['expr'].replace('btagSF_deepflav_shape', 'btagSF_deepflav_shape_up_%s' % shift)
            
            alias = aliases['%sSF%sdown' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
            alias['expr'] = alias['expr'].replace('btagSF_deepflav_shape', 'btagSF_deepflav_shape_down_%s' % shift)
            
        aliases['btagSF%sup' % shift] = {
            'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'up'),
            'samples': mc
        }
        
        aliases['btagSF%sdown' % shift] = {
            'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'down'),
            'samples': mc
        }
        



aliases['Jet_PUIDSF'] = {
  'expr' : 'TMath::Exp(Sum$((Jet_jetId>=2)*TMath::Log(Jet_PUIDSF_loose)))',
  'samples': mc
}

aliases['Jet_PUIDSF_up'] = {
  'expr' : 'TMath::Exp(Sum$((Jet_jetId>=2)*TMath::Log(Jet_PUIDSF_loose_up)))',
  'samples': mc
}

aliases['Jet_PUIDSF_down'] = {
  'expr' : 'TMath::Exp(Sum$((Jet_jetId>=2)*TMath::Log(Jet_PUIDSF_loose_down)))',
  'samples': mc
}


# data/MC scale factors
aliases['SFweight'] = {
    'expr': ' * '.join(['SFweight2l','LepWPCut', 'LepSF2l__ele_' + eleWP + '__mu_' + muWP, 'btagSF', 'PrefireWeight', 'Jet_PUIDSF']),
    'samples': mc
}

# Muon ttHMVA SF needed for tau embedded samples
aliases['Muon_ttHMVA_SF'] = {
    'expr': '( (abs(Lepton_pdgId[0]) == 13)*(Lepton_tightMuon_cut_Tight80x_tthmva_80_IdIsoSF[0]/Lepton_tightMuon_cut_Tight80x_IdIsoSF[0])+(abs(Lepton_pdgId[0]) == 11) )*( (abs(Lepton_pdgId[1]) == 13)*(Lepton_tightMuon_cut_Tight80x_tthmva_80_IdIsoSF[1]/Lepton_tightMuon_cut_Tight80x_IdIsoSF[1])+ (abs(Lepton_pdgId[1]) == 11) )',
    'samples' : ['Dyemb']
}

# variations
aliases['SFweightEleUp'] = {
    'expr': 'LepSF2l__ele_'+eleWP+'__Up',
    'samples': mc_emb
}
aliases['SFweightEleDown'] = {
    'expr': 'LepSF2l__ele_'+eleWP+'__Do',
    'samples': mc_emb
}
aliases['SFweightMuUp'] = {
    'expr': 'LepSF2l__mu_'+muWP+'__Up',
    'samples': mc_emb
}
aliases['SFweightMuDown'] = {
    'expr': 'LepSF2l__mu_'+muWP+'__Do',
    'samples': mc_emb
}

aliases['Weight2MINLO'] = {
    'linesToAdd': ['.L /afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/Differential/weight2MINLO.cc+'],
    'class': 'Weight2MINLO',
    'args': '/afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/LatinoAnalysis/Gardener/python/data/powheg2minlo/NNLOPS_reweight.root',
    'samples' : [skey for skey in samples if 'ggH_hww' in skey],
}


# GGHUncertaintyProducer wasn't run for 2016 nAODv5 non-private
thus = [
    'ggH_mu',
    'ggH_res',
    'ggH_mig01',
    'ggH_mig12',
    'ggH_VBF2j',
    'ggH_VBF3j',
    'ggH_pT60',
    'ggH_pT120',
    'ggH_qmtop'
]

for thu in thus:
    aliases[thu+'_2'] = {
        'linesToAdd': ['.L /afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/Differential/gghuncertainty.cc+'],
        'class': 'GGHUncertainty',
        'args': (thu,),
        'samples': ['ggH_hww'],
        'nominalOnly': True
    }


# In WpWmJJ_EWK events, partons [0] and [1] are always the decay products of the first W
aliases['lhe_mW1'] = {
    'expr': 'TMath::Sqrt(2. * LHEPart_pt[2] * LHEPart_pt[3] * (TMath::CosH(LHEPart_eta[2] - LHEPart_eta[3]) - TMath::Cos(LHEPart_phi[2] - LHEPart_phi[3])))',
    'samples': ['WWewk']
}

# and [2] [3] are the second W
aliases['lhe_mW2'] = {
    'expr': 'TMath::Sqrt(2. * LHEPart_pt[4] * LHEPart_pt[5] * (TMath::CosH(LHEPart_eta[4] - LHEPart_eta[5]) - TMath::Cos(LHEPart_phi[4] - LHEPart_phi[5])))',
    'samples': ['WWewk']
}



###
### MATRIX ELEMENT METHOD FOR POLARIZATION
###

'''
aliases['W0W0_ME']={
    'linesToAdd': [
        'gSystem->Load("/afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/lib/libmomemta.so.1.0.0","", kTRUE);',
        'gSystem->Load("/afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/lib/libmomemta.so.1","", kTRUE);',
        'gSystem->Load("/afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/lib/libmomemta.so","", kTRUE);',
        'gSystem->Load("/afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/lib/libLHAPDF.so", "", kTRUE);',
        '.L /afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/patches/RecoME_MoMEMta_WWj_15.cc+'],
    'class': 'RecoME_WWj_15',
    'args': 'W0W0'
}

aliases['WTW0_ME']={
    'linesToAdd': [
        'gSystem->Load("/afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/lib/libmomemta.so.1.0.0","", kTRUE);',
        'gSystem->Load("/afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/lib/libmomemta.so.1","", kTRUE);',
        'gSystem->Load("/afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/lib/libmomemta.so","", kTRUE);',
        'gSystem->Load("/afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/lib/libLHAPDF.so", "", kTRUE);',
        '.L /afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/patches/RecoME_MoMEMta_WWj_15.cc+'],
    'class': 'RecoME_WWj_15',
    'args': 'WTW0'
}

aliases['WTWT_ME']={
    'linesToAdd': [
        'gSystem->Load("/afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/lib/libmomemta.so.1.0.0","", kTRUE);',
        'gSystem->Load("/afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/lib/libmomemta.so.1","", kTRUE);',
        'gSystem->Load("/afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/lib/libmomemta.so","", kTRUE);',
        'gSystem->Load("/afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/lib/libLHAPDF.so", "", kTRUE);',
        '.L /afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/patches/RecoME_MoMEMta_WWj_15.cc+'],
    'class': 'RecoME_WWj_15',
    'args': 'WTWT'
}


aliases['D_00_TT'] = {
    'expr': '(abs(W0W0_ME)/(abs(W0W0_ME) + (1/40) * abs(WTWT_ME)))'
}

aliases['D_00_T0'] = {
    'expr': '(abs(W0W0_ME)/(abs(W0W0_ME) + abs(WTW0_ME)))'
}

aliases['D_TT_T0'] = {
    'expr': '(abs(WTWT_ME)/(abs(WTWT_ME) + 2 * abs(WTW0_ME)))'
}
'''

aliases['cos_ll'] = {
    'linesToAdd': ['.L /afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/WW/Full2016_v7/WW_helicity/scripts/GetCosTheta.cc+' ],
    'class': 'GetCosTheta',
    'args': ('cos_ll')
}

aliases['rap1'] = {
    'linesToAdd': ['.L /afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/WW/Full2016_v7/WW_helicity/scripts/GetCosTheta.cc+' ],
    'class': 'GetCosTheta',
    'args': ('rap1')
}

aliases['rap2'] = {
    'linesToAdd': ['.L /afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/WW/Full2016_v7/WW_helicity/scripts/GetCosTheta.cc+' ],
    'class': 'GetCosTheta',
    'args': ('rap2')
}

aliases['dphi'] = {
    'linesToAdd': ['.L /afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/WW/Full2016_v7/WW_helicity/scripts/GetCosTheta.cc+' ],
    'class': 'GetCosTheta',
    'args': ('dphi')
}


###
### NEUTRINO RECONSTRUCTION AND ME
###

aliases['cos_theta_p_dnn'] = {
    'linesToAdd': ['.L /afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/WW/Full2016_v7/WW_helicity/DNN/evaluate_nu.cc+'],
    'class': 'evaluate_cos_theta',
    'args': 0,
}


aliases['cos_theta_m_dnn'] = {
    'linesToAdd': ['.L /afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/WW/Full2016_v7/WW_helicity/DNN/evaluate_nu.cc+'],
    'class': 'evaluate_cos_theta',
    'args': 1,
}

aliases['cos_theta_p_MAOS'] = {
    'linesToAdd': ['.L /afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/WW/Full2016_v7/WW_helicity/DNN/evaluate_nu.cc+'],
    'class': 'evaluate_cos_theta',
    'args': 2,
}

aliases['cos_theta_m_MAOS'] = {
    'linesToAdd': ['.L /afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/WW/Full2016_v7/WW_helicity/DNN/evaluate_nu.cc+'],
    'class': 'evaluate_cos_theta',
    'args': 4,
}


aliases['cos_theta_p_MAOS_neg'] = {
    'linesToAdd': ['.L /afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/WW/Full2016_v7/WW_helicity/DNN/evaluate_nu.cc+'],
    'class': 'evaluate_cos_theta',
    'args': 3,
}

aliases['cos_theta_m_MAOS_neg'] = {
    'linesToAdd': ['.L /afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/WW/Full2016_v7/WW_helicity/DNN/evaluate_nu.cc+'],
    'class': 'evaluate_cos_theta',
    'args': 5,
}

'''
methods = ['BDT', 'BDTG4SK01F07', 'BDTG4SK01', 'BDT1', 'BDTG4F07', 'BDTG4D3', 'BDTG4C3', 'BDT2', 'BDTB2', 'BDTB3', 'BDTB', 'LikelihoodKDE', 'Likelihood', 'MLP', 'DNN_CPU']

for m in methods:
    aliases[m] = {
        'linesToAdd': ['.L /afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/WW/Full2016_v7/WW_helicity/scripts/TMVA_apply.cc+' ],
        'class': 'TMVA_app',
        'args': (m)
    }


aliases['ttbar_ME']={
    'linesToAdd': [
        'gSystem->Load("/afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/lib/libmomemta.so.1.0.0","", kTRUE);',
        'gSystem->Load("/afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/lib/libmomemta.so.1","", kTRUE);',
        'gSystem->Load("/afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/lib/libmomemta.so","", kTRUE);',
        'gSystem->Load("/afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/lib/libLHAPDF.so", "", kTRUE);',
        '.L /afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/patches/RecoME_MoMEMta_WWj.cc+'],
    'class': 'RecoME_WWj',
    'args': 'top_2'
}


aliases['WWj_ME']={
    'linesToAdd': [
        'gSystem->Load("/afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/lib/libmomemta.so.1.0.0","", kTRUE);',
        'gSystem->Load("/afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/lib/libmomemta.so.1","", kTRUE);',
        'gSystem->Load("/afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/lib/libmomemta.so","", kTRUE);',
        'gSystem->Load("/afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/lib/libLHAPDF.so", "", kTRUE);',
        '.L /afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/patches/RecoME_MoMEMta_WWj.cc+'],
    'class': 'RecoME_WWj',
    'args': 'WW_2'
}


aliases['D_Top'] = {
    'expr': '(abs(WWj_ME)/(abs(WWj_ME) + 1e4 * abs(ttbar_ME))) + 9999.0 * (ttbar_ME <= -99.0)'
}
'''
