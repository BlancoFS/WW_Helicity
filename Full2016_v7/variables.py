# variables

#### ME variables
'''
variables['D_00_TT'] = { 'name'  : 'D_00_TT',
                         'range' : (30, 0., 1.),
                         'xaxis' : 'Matrix Element method  D_{00TT}',
                         'fold'  : 3}

variables['D_00_T0'] = { 'name'  : 'D_00_T0',
                         'range' : (30, 0., 1.),
                         'xaxis' : 'Matrix Element method  D_{00T0}',
                         'fold'  : 3}

variables['D_TT_T0'] = { 'name'  : 'D_TT_T0',
                         'range' : (30, 0., 1.),
                         'xaxis' : 'Matrix Element method  D_{TTT0}',
                         'fold'  : 3}
'''


variables['rec_cos_theta_p'] = { 'name'  : 'cos_theta_p_dnn',                                                                                                                                             
                                 'range' : (30, -1., 1.),                                                                                                                                                  
                                 'xaxis' : 'Reconstructed cos #theta^{*}_{l^{+}}',                                                                                                                         
                                 'fold'  : 0}

variables['rec_cos_theta_m'] = { 'name'  : 'cos_theta_m_dnn',
                                 'range' : (30, -1., 1.),
                                 'xaxis' : 'Reconstructed cos #theta^{*}_{l^{-}}',
                                 'fold'  : 0}


variables['CosThetaP-CosThetaM'] = { 'name'  : ('cos_theta_p_dnn', 'cos_theta_m_dnn'),
                                     'range': ([-1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0., 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
                                               [-1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0., 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],),
                                     'xaxis' : 'cos #theta_{l^{+}} : cos #theta_{l^{-}}',
                                     'fold'  : 3}

variables['CosThetaP-CosThetaM_2'] = { 'name'  : ('cos_theta_p_dnn', 'cos_theta_m_dnn'),
                                       'range': ([-1.0, -0.8, -0.6, -0.4, -0.2, 0., 0.2, 0.4, 0.6, 0.8, 1.0],
                                                 [-1.0, -0.8, -0.6, -0.4, -0.2, 0., 0.2, 0.4, 0.6, 0.8, 1.0],),
                                       'xaxis' : 'cos #theta_{l^{+}} : cos #theta_{l^{-}}',
                                       'fold'  : 3}

variables['CosThetaP-CosThetaM_3'] = { 'name'  : ('cos_theta_p_dnn', 'cos_theta_m_dnn'),
                                       'range': ([-1.0, -0.66, -0.33, 0., 0.33, 0.66, 1.0],
                                                 [-1.0, -0.66, -0.33, 0., 0.33, 0.66, 1.0],),
                                       'xaxis' : 'cos #theta_{l^{+}} : cos #theta_{l^{-}}',
                                       'fold'  : 3}


variables['MAOS_cos_theta_p'] = { 'name'  : 'cos_theta_p_MAOS',
                                 'range' : (30, -1., 1.),
                                 'xaxis' : 'Reconstructed cos #theta^{*}_{l^{+}}',
                                 'fold'  : 0}


variables['MAOS_cos_theta_m'] = { 'name'  : 'cos_theta_p_MAOS',
                                  'range' : (30, -1., 1.),
                                  'xaxis' : 'Reconstructed cos #theta^{*}_{l^{-}}',
                                  'fold'  : 0}


variables['MAOS_cos_theta_p_neg'] = { 'name'  : 'cos_theta_p_MAOS_neg',
                                 'range' : (30, -1., 1.),
                                 'xaxis' : 'Reconstructed cos #theta^{*}_{l^{+}}',
                                 'fold'  : 0}


variables['MAOS_cos_theta_m_neg'] = { 'name'  : 'cos_theta_p_MAOS_neg',
                                  'range' : (30, -1., 1.),
                                  'xaxis' : 'Reconstructed cos #theta^{*}_{l^{-}}',
                                  'fold'  : 0}

'''
variables['BDTG4SK01F07'] = { 'name'  : 'TMVA_var(Entry$, 1)',
                     'range' : (30, -1., 1.),
                     'xaxis' : 'BDTG4SK01F07',
                     'fold'  : 3,
                     'linesToAdd' : ['.L /afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/WW/Full2016_v7/WW_helicity/scripts/TMVA_var.C+']
}

variables['BDTG4SK01'] = { 'name'  : 'TMVA_var(Entry$, 2)',
                           'range' : (30, -1., 1.),
                           'xaxis' : 'BDTG4SK01',
                           'fold'  : 3,
                           'linesToAdd' : ['.L /afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/WW/Full2016_v7/WW_helicity/scripts/TMVA_var.C+']
}


variables['BDT1'] = { 'name'  : 'TMVA_var(Entry$, 3)',
                     'range' : (30, -1., 1.),
                     'xaxis' : 'BDT1',
                     'fold'  : 3,
                     'linesToAdd' : ['.L /afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/WW/Full2016_v7/WW_helicity/scripts/TMVA_var.C+']
}

variables['BDTG4F07'] = { 'name'  : 'TMVA_var(Entry$, 4)',
                          'range' : (30, -1., 1.),
                          'xaxis' : 'BDTG4F07',
                          'fold'  : 3,
                          'linesToAdd' : ['.L /afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/WW/Full2016_v7/WW_helicity/scripts/TMVA_var.C+']
}

variables['BDTG4D3'] = { 'name'  : 'TMVA_var(Entry$, 5)',
                         'range' : (30, -1., 1.),
                         'xaxis' : 'BDTG4D3',
                         'fold'  : 3,
                         'linesToAdd' : ['.L /afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/WW/Full2016_v7/WW_helicity/scripts/TMVA_var.C+']
}

variables['BDTG4C3'] = { 'name'  : 'TMVA_var(Entry$, 6)',
                         'range' : (30, -1., 1.),
                         'xaxis' : 'BDTG4C3',
                         'fold'  : 3,
                         'linesToAdd' : ['.L /afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/WW/Full2016_v7/WW_helicity/scripts/TMVA_var.C+']
}

variables['BDT2'] = { 'name'  : 'TMVA_var(Entry$, 7)',
                      'range' : (30, -1., 1.),
                      'xaxis' : 'BDT2',
                      'fold'  : 3,
                      'linesToAdd' : ['.L /afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/WW/Full2016_v7/WW_helicity/scripts/TMVA_var.C+']
}


variables['BDTB2'] = { 'name'  : 'TMVA_var(Entry$, 8)',
                       'range' : (30, -1., 1.),
                       'xaxis' : 'BDTB2',
                       'fold'  : 3,
                       'linesToAdd' : ['.L /afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/WW/Full2016_v7/WW_helicity/scripts/TMVA_var.C+']
}

variables['BDTB3'] = { 'name'  : 'TMVA_var(Entry$, 9)',
                       'range' : (30, -1., 1.),
                       'xaxis' : 'BDTB3',
                       'fold'  : 3,
                       'linesToAdd' : ['.L /afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/WW/Full2016_v7/WW_helicity/scripts/TMVA_var.C+']
}


variables['BDTB'] = { 'name'  : 'TMVA_var(Entry$, 1)',
                      'range' : (30, -1., 1.),
                      'xaxis' : 'BDTB',
                      'fold'  : 3,
                      'linesToAdd' : ['.L /afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/WW/Full2016_v7/WW_helicity/scripts/TMVA_BDTB1.C+']
}


variables['LikelihoodKDE'] = { 'name'  : 'TMVA_var(Entry$, 11)',
                               'range' : (30, 0., 1.),
                               'xaxis' : 'LikelihoodKDE',
                               'fold'  : 3,
                               'linesToAdd' : ['.L /afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/WW/Full2016_v7/WW_helicity/scripts/TMVA_var.C+']
}


variables['Likelihood'] = { 'name'  : 'TMVA_var(Entry$, 12)',
                            'range' : (30, 0., 1.),
                            'xaxis' : 'Likelihood',
                            'fold'  : 3,
                            'linesToAdd' : ['.L /afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/WW/Full2016_v7/WW_helicity/scripts/TMVA_Likelihood.C+']
}

variables['MLP'] = { 'name'  : 'TMVA_var(Entry$, 13)',
                     'range' : (30, 0., 1.),
                     'xaxis' : 'MLP',
                     'fold'  : 3,
                     'linesToAdd' : ['.L /afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/WW/Full2016_v7/WW_helicity/scripts/TMVA_MLP.C+']
}

variables['DNN_CPU'] = { 'name'  : 'TMVA_var(Entry$, 14)',
                         'range' : (30, 0., 1.),
                         'xaxis' : 'DNN_CPU',
                         'fold'  : 3,
                         'linesToAdd' : ['.L /afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/WW/Full2016_v7/WW_helicity/scripts/TMVA_DNN.C+']
}
'''


### kinematic variables


'''
variables['Ctot'] = {     'name': 'log((abs(2*Lepton_eta[0]-CleanJet_eta[0]-CleanJet_eta[1])+abs(2*Lepton_eta[1]-CleanJet_eta[0]-CleanJet_eta[1]))/detajj)',
                          'range' : (20, -4, 6),
                          #'range' : (10, -4, 2),
                          'xaxis' : 'Ctot',
                          'fold'  : 3}

variables['costhetall'] = {     'name': 'cos_ll',
                                'range' : (30, -1, 1),
                                'xaxis' : 'cos(#theta_{ll})',
                                'fold'  : 3}

variables['rap1'] = {     'name': 'rap1',
                          'range' : (30, -2.5, 2.5),
                          'xaxis' : 'y_{l+})',
                          'fold'  : 3}

variables['rap2'] = {     'name': 'rap2',
                          'range' : (30, -2.5, 2.5),
                          'xaxis' : 'y_{l-})',
                          'fold'  : 3}

variables['dphi'] = {     'name': 'dphi',
                          'range' : (30, 0.0, 3.14),
                          'xaxis' : '#Delta #Phi_{l2}',
                          'fold'  : 3}

variables['jet1_qgl'] = { 'name'  : 'Jet_qgl[0]',
                          'range' : (20, 0., 1.),
                          'xaxis' : 'Quark Gluon likelihood (1^{st} Jet)',
                          'fold'  : 3}

variables['jet2_qgl'] = { 'name'  : 'Jet_qgl[1]',
                          'range' : (20, 0., 1.),
                          'xaxis' : 'Quark Gluon likelihood (2^{nd} Jet)',
                          'fold'  : 3}

variables['detajj'] = {   'name'  : 'detajj',
                          'range' : (20, 0., 5.),
                          #'range' : (10, 3., 4.),
                          'xaxis' : '|#Delta#eta_{jj}|',
                          'fold'  : 3}

variables['detal1j1'] = { 'name'  : 'abs(Lepton_eta[0]-CleanJet_eta[0])',
                          #'range' : (20, 0., 4.),
                          'range' : (10, 0., 4.),
                          'xaxis' : '|#Delta#eta_{l1j1}|',
                          'fold'  : 3}

variables['detal2j2'] = { 'name'  : 'abs(Lepton_eta[1]-CleanJet_eta[1])',
                          'range' : (20, 0., 4.),
                          'xaxis' : '|#Delta#eta_{l2j2}|',
                          'fold'  : 3}
 
variables['detal1j2'] = { 'name'  : 'abs(Lepton_eta[0]-CleanJet_eta[1])',
                          'range' : (20, 0., 4.),
                          'xaxis' : '|#Delta#eta_{l1j2}|',
                          'fold'  : 3}

variables['detal2j1'] = { 'name'  : 'abs(Lepton_eta[1]-CleanJet_eta[0])',
                          'range' : (20, 0., 4.),
                          'xaxis' : '|#Delta#eta_{l2j1}|',
                          'fold'  : 3}
         
variables['detall'] = { 'name'  : 'abs(Lepton_eta[0]-Lepton_eta[1])',
                          'range' : (20, 0., 5.),
                          'xaxis' : '|#Delta#eta_{l1l2}|',
                          'fold'  : 3}

variables['detall_01'] = { 'name'  : 'abs(Lepton_eta[0]-Lepton_eta[1])',
                          'range' : (10, 0., 1.),
                          'xaxis' : '|#Delta#eta_{l1l2}|',
                          'fold'  : 0}

variables['drjj'] = {     'name'  : 'sqrt((CleanJet_eta[0]-CleanJet_eta[1])**2 + (CleanJet_phi[0]-CleanJet_phi[1])**2)',
                          'range' : (20, 0., 8.),
                          #'range' : (10, 0., 5.),
                          'xaxis' : '#DeltaR_{jj}',
                         #'linesToAdd': ['.L $CMSSW_BASE/src/PlotsConfigurations/Configurations/WW/Full2016_v6/extended/drjj.C+'], #if want to use a script
                          'fold'  : 3}
          
          
variables['dphijjmet'] = {'name'  : 'abs(dphijjmet)',     
                          'range' : (20, 0., 3.2),
                          #'range' : (10, 0., 3.2),
                          'xaxis' : '#Delta#phi_{jjmet}',
                          'fold'  : 3}

variables['dphill'] = {   'name'  : 'abs(dphill)',     
                          'range' : (20, 0., 3.2),   
                          #'range' : (10, 0., 3.2),
                          'xaxis' : '#Delta#phi_{ll}',
                          'fold'  : 3}

variables['dphijj'] = {   'name'  : 'CleanJet_phi[0] - CleanJet_phi[1]',
                          'range' : (20, -3.2, 3.2),
                          #'range' : (10, 0., 3.2),                                                                                                                                                        
                          'xaxis' : '#Delta#phi_{jj}',
                          'fold'  : 3}

variables['dphill_01'] = {   'name'  : 'abs(dphill)',
                          'range' : (10, 0., 1.),
                          'xaxis' : '#Delta#phi_{ll}',
                          'fold'  : 3}

variables['dphillj'] = {  'name'  : 'abs(dphilljet)',     
                          'range' : (20, 0., 3.2),   
                          #'range' : (10, 0., 3.2),
                          'xaxis' : '#Delta#phi_{llj}',
                          'fold'  : 3}

variables['dphilljj'] = { 'name'  : 'abs(dphilljetjet)',     
                          'range' : (20, 0., 3.2),   
                          #'range' : (10, 0., 3.2),
                          'xaxis' : '#Delta#phi_{lljj}',
                          'fold'  : 3}

variables['drll'] = {     'name'  : 'drll',
                          'range' : (30, 0., 5.),
                          #'range' : (10, 0., 2.5),
                          'xaxis' : '#DeltaR_{ll}',
                          'fold'  : 3}

variables['drll_01'] = {  'name'  : 'drll',
                          'range' : (10, 0., 1.),                                                                                                                                                         
                          'xaxis' : '#DeltaR_{ll}',
                          'fold'  : 2}

variables['eta1'] = {     'name'  : 'Lepton_eta[0]',     
                          'range' : (40, -3.2, 3.2),   
                          #'range' : (15, -3.2, 3.2),
                          'xaxis' : '#eta 1st lepton',
                          'fold'  : 3}

variables['eta2'] = {     'name'  : 'Lepton_eta[1]',     
                          'range' : (40, -3.2, 3.2),
                          #'range' : (15, -3.2, 3.2),
                          'xaxis' : '#eta 2nd lepton',
                          'fold'  : 3}

variables['events'] = {   'name'  : '1',
                          'range' : (1, 0, 2),
                          'xaxis' : 'events',
                          'fold'  : 3}

variables['jeteta1'] = {  'name'  : 'CleanJet_eta[0]',
                          #'range' : (80, -4., 4.),
                          'range' : (15, -4., 4.),
                          'xaxis' : '#eta 1st jet',
                          'fold'  : 3}

variables['jeteta2'] = {  'name'  : 'CleanJet_eta[1]',
                          #'range' : (80, -4., 4.),
                          'range' : (15, -4., 4.),
                          'xaxis' : '#eta 2nd jet',
                          'fold'  : 3}

variables['jeteta3'] = {  'name'  : 'CleanJet_eta[2]',
                          #'range' : (80, -4., 4.),
                          'range' : (15, -4., 4.),
                          'xaxis' : '#eta 3rd jet',
                          'fold'  : 3}

variables['jetphi1'] = {  'name'  : 'CleanJet_phi[0]',
                          'range' : (40, -3.2, 3.2),
                          'xaxis' : '#phi 1st jet',
                          'fold'  : 3}

variables['jetphi2'] = {  'name'  : 'CleanJet_phi[1]',
                          'range' : (40, -3.2, 3.2),
                          'xaxis' : '#phi 2nd jet',
                          'fold'  : 3}

variables['jetphi3'] = {  'name'  : 'CleanJet_phi[2]',
                          'range' : (40, -3.2, 3.2),
                          'xaxis' : '#phi 3rd jet',
                          'fold'  : 3}

variables['jetpt1'] = {   'name'  : 'CleanJet_pt[0]*(CleanJet_pt[0]>30)',     
                          #'range' : (40, 30., 190.),
                          'range' : (10, 30., 190.),
                          'xaxis' : 'p_{T} 1st jet',
                          'fold'  : 3}

variables['jetpt1_0j'] = {'name'  : 'CleanJet_pt[0]*(CleanJet_pt[0]<30)',     
                          'range' : (30, 0., 30.),   
                          'xaxis' : 'p_{T} 1st jet (p_{T} < 30 GeV) ',
                          'fold'  : 0}

variables['mjj'] = {      'name'  : 'mjj',
                          #'range' : (25, 200., 400.),
                          'range' : (30, 0., 4000.),
                          'xaxis' : 'm_{jj} [GeV]',
                          'fold'  : 3}

variables['mjj_CR'] = {      'name'  : 'mjj',
                          'range' : (20, 0., 400.),
                          'xaxis' : 'm_{jj} [GeV]',
                          'fold'  : 3}

variables['mjj_WW'] = {      'name'  : 'mjj',
                             'range' : (10, 0., 200.),
                             'xaxis' : 'm_{jj} [GeV]',
                             'fold'  : 3}

variables['mjj_GGH'] = {      'name'  : 'mjj',
                              'range' : (10, 0., 300.),
                              'xaxis' : 'm_{jj} [GeV]',
                              'fold'  : 3}

variables['mll'] = {      'name'  : 'mll',
                          'range' : (20, 10., 100.),
                          'xaxis' : 'm_{ll} [GeV]',
                          'fold'  : 0}

variables['mll_top'] = {      'name'  : 'mll',
                          'range' : (20, 0., 200.),
                          'xaxis' : 'm_{ll} [GeV]',
                              'fold'  : 0}

variables['mll10GeV'] = { 'name'  : 'mll',
                          #'range' : (20, 0., 200.),
                          'range' : (10, 0., 100.),
                          'xaxis' : 'm_{ll} [GeV]',
                          'fold'  : 3}

variables['mpmet'] = {    'name'  : 'mpmet',      
                          'range' : (50, 0., 150.),  
                          'xaxis' : 'min. (proj. tk. E_{T}^{miss}, proj. E_{T}^{miss}) [GeV]', 
                          'fold'  : 3}

variables['mth'] = {      'name'  : 'mth',
                          #'range' : (40, 0., 200.),
                          'range' : (10, 0., 125.),
                          'xaxis' : 'm_{T}^{H} [GeV]',
                          'fold'  : 3}

variables['mth_top'] = {      'name'  : 'mth',
                              #'range' : (40, 0., 200.),                                                                                                                                                   
                              'range' : (40, 0., 200.),
                              'xaxis' : 'm_{T}^{H} [GeV]',
                              'fold'  : 3}

variables['mth_DY'] = {      'name'  : 'mth',
                             'range' : (20, 0., 40.),
                             'xaxis' : 'm_{T}^{H} [GeV]',
                             'fold'  : 3}

variables['mth_WW'] = {      'name'  : 'mth',
                             'range' : (12, 50., 200.),
                             'xaxis' : 'm_{T}^{H} [GeV]',
                             'fold'  : 3}

variables['mth_GGH'] = {      'name'  : 'mth',
                             'range' : (10, 60., 145.),
                             'xaxis' : 'm_{T}^{H} [GeV]',
                             'fold'  : 3}

variables['mtw1']  = {   'name': 'mtw1',            
                         'range' : (20,0,400),    
                         'xaxis' : 'm^{T}_{W1}  [GeV]',
                         'fold'  : 3
                     }

variables['mtw2']  = {   'name': 'mtw2',
                         'range' : (20,0,400),
                         'xaxis' : 'm^{T}_{W1}  [GeV]',
                         'fold'  : 3
                     }

variables['njet'] = {     'name'  : 'Sum$(CleanJet_pt>30)',     
                          'range' : (5, 0, 5),   
                          'xaxis' : 'number of jets',
                          'fold'  : 3}

variables['bjet'] = {     'name'  : 'Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.2217)',     
                          #'name'  : 'Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepFlavB[CleanJet_jetIdx] >  0.0614)',
                          'range' : (5, 0, 5),   
                          'xaxis' : 'number of b jets',
                          'fold'  : 2}

variables['nvtx'] = {     'name'  : 'PV_npvsGood',      
                          'range' : (50, 0, 50),  
                          'xaxis' : 'number of vertices', 
                          'fold'  : 3}

variables['phi1'] = {     'name'  : 'Lepton_phi[0]',
                          'range' : (40, -3.2, 3.2),
                          'xaxis' : '#phi 1st lepton',
                          'fold'  : 3}

variables['phi2'] = {     'name'  : 'Lepton_phi[1]',
                          'range' : (40, -3.2, 3.2),
                          'xaxis' : '#phi 2nd lepton',
                          'fold'  : 3}

variables['pfmet'] = {    'name'  : 'MET_pt',     
                          'range' : (50, 0., 150.),   
                          'xaxis' : 'PF MET [GeV]',
                          'fold'  : 3}

variables['pt1'] = {      'name'  : 'Lepton_pt[0]',     
                          #'range' : (40, 0., 200.),   
                          'range' : (10, 20., 100.),
                          'xaxis' : 'p_{T} 1st lepton [GeV]',
                          'fold'  : 3}

variables['pt2'] = {      'name'  : 'Lepton_pt[1]',     
                          #'range' : (40, 0., 200.),   
                          'range' : (10, 13., 100.),
                          'xaxis' : 'p_{T} 2nd lepton [GeV]',
                          'fold'  : 3}

variables['ptll'] = {     'name'  : 'ptll',
                          #'range' : (40, 30., 200.),
                          'range' : (10, 30., 200.),
                          'xaxis' : 'p_{T}^{ll} [GeV]',
                          'fold'  : 3}

variables['puppimet'] = { 'name'  : 'PuppiMET_pt',
                          'range' : (50, 0., 150.),
                          'xaxis' : 'puppi MET [GeV]',
                          'fold'  : 3}

variables['rawmet'] = {   'name'  : 'RawMET_pt',     
                          'range' : (50, 0., 150.),   
                          'xaxis' : 'raw MET [GeV]',
                          'fold'  : 3}

variables['TkMET'] = {    'name'  : 'TkMET_pt',     
                          'range' : (50, 0., 150.),   
                          'xaxis' : 'tracker MET [GeV]',
                          'fold'  : 3}

variables['ptlljjmet'] = { 'name'  : 'Lepton_pt[0] + Lepton_pt[1] + CleanJet_pt[0] + CleanJet_pt[1] + MET_pt',
                          'range' : (12, 100., 700.),
                          'xaxis' : 'p_{T} leptons+jets+MET',
                          'fold'  : 3}

variables['ptjjj'] = { 'name'  : '(CleanJet_pt[0] + CleanJet_pt[1] + CleanJet_pt[2])*(CleanJet_pt[2] > 30)',
                       'range' : (16, 100., 500.),
                       'xaxis' : 'p_{T} 3 jets',
                       'fold'  : 2}

variables['ptjj'] = { 'name'  : '(CleanJet_pt[0] + CleanJet_pt[1])',
                      'range' : (16, 0., 500.),
                      'xaxis' : 'p_{T} 2 jets',
                      'fold'  : 3}

variables['ptWW'] = {      'name'  : 'pTWW',
                           'range' : (50, 0., 1000.),
                           'xaxis' : 'p_{T, WW} [GeV]',
                           'fold'  : 3}

variables['ptWW_400'] = {      'name'  : 'pTWW',
                               'range' : (50, 0., 400.),
                               'xaxis' : 'p_{T, WW} [GeV]',
                               'fold'  : 3}

variables['ptWW_200'] = {      'name'  : 'pTWW',
                               'range' : (50, 0., 200.),
                               'xaxis' : 'p_{T, WW} [GeV]',
                               'fold'  : 3}

variables['ptWW_100'] = {      'name'  : 'pTWW',
                               'range' : (50, 0., 100.),
                               'xaxis' : 'p_{T, WW} [GeV]',
                               'fold'  : 0}

variables['ptWW_50'] = {      'name'  : 'pTWW',
                               'range' : (50, 0., 50.),
                               'xaxis' : 'p_{T, WW} [GeV]',
                               'fold'  : 0}

variables['detall'] = { 'name'  : 'abs(Lepton_eta[0]-Lepton_eta[1])',
                          'range' : (20, 0., 5.),
                          'xaxis' : '|#Delta#eta_{l1l2}|',
                          'fold'  : 3}

variables['dphill'] = {   'name'  : 'abs(dphill)',
                          'range' : (20, 0., 3.2),
                          #'range' : (10, 0., 3.2),                                                                                                                                                                                          
                          'xaxis' : '#Delta#phi_{ll}',
                          'fold'  : 3}

'''
