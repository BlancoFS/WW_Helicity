

variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3
                        }
variables['nvtx']  = {   'name': 'PV_npvsGood',
                       'range' : (20,0,100),
                       'xaxis' : 'nvtx',
                        'fold' : 3
                     }
variables['mll']  = {   'name': 'mll',
                        'range' : (20, 20., 60.),
                        'xaxis' : 'm_{ll} [GeV]',
                        'fold' : 3
                        }
variables['mjj'] = {      'name'  : 'mjj',                                                                                                                                                  
                          'range' : (30, 0., 400.),
                          'xaxis' : 'm_{jj} [GeV]',
                          'fold'  : 3
                   }
variables['mth']  = {   'name': 'mth',
                        'range' : (50, 0.,200),
                        'xaxis' : 'm_{T}^{H} [GeV]',
                        'fold' : 0
                        }
variables['mtw1']  = {   'name': 'mtw1',
                        'range' : (50, 0.,100),
                        'xaxis' : 'm_{T}^{H} [GeV]',
                        'fold' : 0
                        }
variables['mtw2']  = {   'name': 'mtw2',
                        'range' : (50, 0.,100),
                        'xaxis' : 'm_{T}^{H} [GeV]',
                        'fold' : 0
                        }
variables['mth-DY']  = {   'name': 'mth',
                        'range' : (30, 0, 60),
                        'xaxis' : 'm_{T}^{H} [GeV]',
                        'fold' : 0
                        }
variables['ptll']  = {   'name': 'ptll',
                        'range' : (50, 0,200),
                        'xaxis' : 'p_{T}^{ll} [GeV]',
                        'fold' : 0
                        }
variables['pt1']  = {   'name': 'Lepton_pt[0]',
                        'range' : (40,20,100),
                        'xaxis' : 'p_{T} 1st lep',
                        'fold'  : 0
                        }
variables['pt2']  = {   'name': 'Lepton_pt[1]',
                        'range' : (40,10,100),
                        'xaxis' : 'p_{T} 2nd lep',
                        'fold'  : 0
                        }
variables['eta1']  = {  'name': 'Lepton_eta[0]',
                        'range' : (30, -2.5, 2.5),
                        'xaxis' : '#eta 1st lep',
                        'fold'  : 3
                        }
variables['eta2']  = {  'name': 'Lepton_eta[1]',
                        'range' : (30, -2.5, 2.5),
                        'xaxis' : '#eta 2nd lep',
                        'fold'  : 3
                        }
variables['phi1']  = {  'name': 'Lepton_phi[0]',
                        'range' : (30,-3.2, 3.2),
                        'xaxis' : '#phi 1st lep',
                        'fold'  : 3
                        }
variables['phi2']  = {  'name': 'Lepton_phi[1]',
                        'range' : (30,-3.2, 3.2),
                        'xaxis' : '#phi 2nd lep',
                        'fold'  : 3
                        }
variables['dphill'] = {   'name'  : 'dphill',
                          'range' : (20, 0.0, 2.3),
                          'xaxis' : '#Delta#phi_{ll}',
                          'fold'  : 3
                      }
variables['detall'] = { 'name'  : 'abs(detall)',
                        'range' : (40, 0., 5.),
                        'xaxis' : '|#Delta#eta_{ll}|',
                        'fold'  : 3
                      }
variables['drll'] = {     'name'  : 'drll',
                          'range' : (30, 0.5, 2.5),
                          'xaxis' : '#DeltaR_{ll}',
                          'fold'  : 3}

variables['puppimet']  = {
                        'name': 'PuppiMET_pt',
                        'range' : (20,0,200),
                        'xaxis' : 'puppimet [GeV]',
                        'fold'  : 3
                        }
variables['mpmet']  = {
                        'name': 'mpmet',
                        'range' : (20,0,200),
                        'xaxis' : 'mpmet [GeV]',
                        'fold'  : 3
                        }
variables['njet']  = {
                        'name': 'Sum$(CleanJet_pt>30)',
                        'range' : (5,0,5),
                        'xaxis' : 'Number of jets',
                        'fold' : 2   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }
variables['jetpt1']  = {
                        'name': '(Sum$(CleanJet_pt>30)>0)*(Alt$(CleanJet_pt[0], 0)) - (Sum$(CleanJet_pt>30)==0)*99',
                        'range' : (20,0,200),
                        'xaxis' : 'p_{T} 1st jet',
                        'fold' : 2   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }
variables['jetpt2']  = {
                        'name': '(Sum$(CleanJet_pt>30)>0)*(Alt$(CleanJet_pt[1], 0)) - (Sum$(CleanJet_pt>30)==0)*99',
                        'range' : (20,0,200),
                        'xaxis' : 'p_{T} 2nd jet',
                        'fold' : 2   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }
variables['jeteta1']  = {  'name': '(Sum$(CleanJet_pt>30)>0)*(Alt$(CleanJet_eta[0], 0)) - (Sum$(CleanJet_pt>30)==0)*99',
                        'range' : (30,-5.0,5.0),
                        'xaxis' : '#eta 1st jet',
                        'fold'  : 0
                        }
variables['jeteta2']  = {  'name': '(Sum$(CleanJet_pt>30)>1)*(Alt$(CleanJet_eta[1], 0)) - (Sum$(CleanJet_pt>30)<=1)*99',
                        'range' : (30,-5.0,5.0),
                        'xaxis' : '#eta 2nd jet',
                        'fold'  : 0
                        }
variables['dphijj'] = {   'name'  : 'dphijj',
                          'range' : (20, 0.0, 3.1416),
                          #'range' : (10, 0., 3.2),                                                                                                                                                        
                          'xaxis' : '#Delta#phi_{jj}',
                          'fold'  : 3}
variables['mjj'] = {      'name'  : 'mjj',
                          #'range' : (25, 200., 400.),
                          'range' : (30, 0., 4000.),
                          'xaxis' : 'm_{jj} [GeV]',
                          'fold'  : 3}
