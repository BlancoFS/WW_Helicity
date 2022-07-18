# plot configuration



# groupPlot = {}
# 
# Groups of samples to improve the plots.
# If not defined, normal plots is used
#

groupPlot['Bkg']  = {
                  'nameHR' : 'Main backgrounds',
                  'isSignal' : 0,
                  'color': 921,   # kYellow                                                                                                                                                                
                  'samples'  : ['top', 'ggWW', 'WWewk', 'Fake_me', 'Fake_em', 'DY', 'Dyemb', 'VVV', 'VZ', 'WZ', 'ZZ', 'Vg', 'Wg', 'VgS_H','VgS_L', 'H_htt', 'H_hww', 'ZH_hww', 'ggZH_hww', 'WH_hww','bbH_hww','ttH_hww', 'qqH_htt', 'ggH_htt', 'ggH_hww']
              }


'''
groupPlot['top']  = {
                  'nameHR' : 'tW and t#bar{t}',
                  'isSignal' : 0,
                  'color': 400,   # kYellow                                                                                                                                                                
                  'samples'  : ['top']
              }


groupPlot['WW_bkg']  = {  
                  'nameHR' : 'Other WW',
                  'isSignal' : 0,
                  'color': 851, # kAzure -9 
                  'samples'  : ['ggWW', 'WWewk']
              }

'''


## Test polarization
#groupPlot['WW']  = {
#                  'nameHR' : 'WW (Unp)',
#                  'isSignal' : 0,
#                  'color': 851,
#                  'samples'  : ['WW']
#              }

## Single Polarized

'''
groupPlot['W0W']  = {
                  'nameHR' : 'W_{0}^{+}W_{Unp}^{-}',
                  'isSignal' : 2,
                  'color': 632,
                  'samples'  : ['W0+W-']
              }

groupPlot['WLW']  = {
                  'nameHR' : 'W_{L}^{+}W_{Unp}^{-}',
                  'isSignal' : 2,
                  'color': 400,
                  'samples'  : ['WL+W-']
              }

groupPlot['WRW']  = {
                  'nameHR' : 'W_{R}^{+}W_{Unp}^{-}',
                  'isSignal' : 2,
                  'color': 418,
                  'samples'  : ['WR+W-']
              }

groupPlot['WW0']  = {
                  'nameHR' : 'W_{Unp}^{+}W_{0}^{-}',
                  'isSignal' : 2,
                  'color': 632,
                  'samples'  : ['W+W0-']
              }

groupPlot['WWL']  = {
                  'nameHR' : 'W_{Unp}^{+}W_{L}^{-}',
                  'isSignal' : 2,
                  'color': 400,
                  'samples'  : ['W+WL-']
              }

groupPlot['WWR']  = {
                  'nameHR' : 'W_{Unp}^{+}W_{R}^{-}',
                  'isSignal' : 2,
                  'color': 418,
                  'samples'  : ['W+WR-']
              }
'''


'''
groupPlot['Fake']  = {
                  'nameHR' : 'nonprompt',
                  'isSignal' : 0,
                  'color': 921,    # kGray + 1
                  'samples'  : ['Fake_me', 'Fake_em']
}


groupPlot['DY']  = {  
                  'nameHR' : "DY",
                  'isSignal' : 0,
                  'color': 418,    # kGreen+2
                  'samples'  : ['DY', 'Dyemb']
              }



groupPlot['VVV']  = {  
                  'nameHR' : 'VVV',
                  'isSignal' : 0,
                  'color': 857, # kAzure -3  
                  'samples'  : ['VVV']
              }


groupPlot['VZ']  = {  
                  'nameHR' : "VZ",
                  'isSignal' : 0,
                  'color'    : 617,   # kViolet + 1  
                  'samples'  : ['VZ', 'WZ', 'ZZ']
              }

groupPlot['Vg']  = {  
                  'nameHR' : "V#gamma",
                  'isSignal' : 0,
                  'color'    : 810,   # kOrange + 10
                  'samples'  : ['Vg', 'Wg']
              }

groupPlot['VgS']  = {
                  'nameHR' : "V#gamma*",
                  'isSignal' : 0,
                  'color'    : 409,   # kGreen - 9
                  'samples'  : ['VgS_H','VgS_L']
              }


groupPlot['Higgs']  = {  
                  'nameHR' : 'Higgs',
                  'isSignal' : 0,
                  'color': 920, # kRed 
		  #'samples'  : ['H_htt', 'H_hww', 'ZH_hww', 'ggZH_hww', 'WH_hww', 'qqH_hww', 'ggH_hww','bbH_hww','ttH_hww','ZH_htt', 'ggZH_htt', 'WH_htt', 'qqH_htt', 'ggH_htt','bbH_htt','ttH_htt' ]
		  #'samples'  : ['H_htt', 'H_hww', 'ZH_hww', 'ggZH_hww', 'WH_hww', 'ggH_hww','bbH_hww','ttH_hww', 'qqH_htt', 'ggH_htt' ] with ggH
                  'samples'  : ['H_htt', 'H_hww', 'ZH_hww', 'ggZH_hww', 'WH_hww','bbH_hww','ttH_hww', 'qqH_htt', 'ggH_htt', 'ggH_hww' ]
              }

'''


## Double Polarized                                                                                                                                                                                                                          
groupPlot['WTWL']  = {
                  'nameHR' : 'W_{T}W_{L}',
                  'isSignal' : 0,
                  'color': 400,
                  'samples'  : ['WTWL']
              }

groupPlot['WLWT']  = {
                  'nameHR' : 'W_{L}W_{T}',
                  'isSignal' : 0,
                  'color': 857,
                  'samples'  : ['WLWT']
              }

groupPlot['WTWT']  = {
                  'nameHR' : 'W_{T}W_{T}',
                  'isSignal' : 0,
                  'color': 418,
                  'samples'  : ['WTWT']
              }


groupPlot['WLWL']  = {
                  'nameHR' : 'W_{L}W_{L}',
                  'isSignal' : 1,
                  'color': 632,
                  'samples'  : ['WLWL']
              }


#plot = {}

# keys here must match keys in samples.py    
#


plot['DY']  = {  
                  'color': 418,    # kGreen+2
                  'isSignal' : 0,
                  'isData'   : 0, 
                  'scale'    : 1.0,
                  #'cuts'  : {
                       #'hww2l2v_13TeV_of0j'      : 0.95 ,
                       #'hww2l2v_13TeV_top_of0j'  : 0.95 , 
                       #'hww2l2v_13TeV_dytt_of0j' : 0.95 ,
                       #'hww2l2v_13TeV_em_0j'     : 0.95 , 
                       #'hww2l2v_13TeV_me_0j'     : 0.95 , 
                       ##
                       #'hww2l2v_13TeV_of1j'      : 1.08 ,
                       #'hww2l2v_13TeV_top_of1j'  : 1.08 , 
                       #'hww2l2v_13TeV_dytt_of1j' : 1.08 ,
                       #'hww2l2v_13TeV_em_1j'     : 1.08 , 
                       #'hww2l2v_13TeV_me_1j'     : 1.08 , 
                        #},

              }

if useEmbeddedDY:
  plot['Dyemb']  = {  
                  'color': 418,    # kGreen+2
                  'isSignal' : 0,
                  'isData'   : 0, 
                  'scale'    : 1.0,
              }


plot['Fake_me']  = {  
                  'color': 921,    # kGray + 1
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0                  
              }


plot['Fake_em']  = {  
                  'color': 921,    # kGray + 1
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0                  
              }


plot['top'] = {
                  'nameHR' : 'tw and t#bar{t}',
                  'color': 400,   # kYellow                                                                                                                                                                
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
               }

'''
#plot['WW']  = {
#                  'color': 851,
#                  'isSignal' : 0,
#                  'isData'   : 0,
#                  'scale'    : 1.0
#                  }


## Single Polarized 

plot['W0+W-']  = {
                  'color': 851,
                  'isSignal' : 2,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

plot['WL+W-']  = {
                  'color': 851,
                  'isSignal' : 2,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

plot['WR+W-']  = {
                  'color': 851,
                  'isSignal' : 2,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

plot['W+W0-']  = {
                  'color': 851,
                  'isSignal' : 2,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

plot['W+WL-']  = {
                  'color': 851,
                  'isSignal' : 2,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

plot['W+WR-']  = {
                  'color': 851,
                  'isSignal' : 2,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

'''


## Double Polarized 

plot['WTWL']  = {
                  'color': 851,
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

plot['WLWT']  = {
                  'color': 851,
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

plot['WTWT']  = {
                  'color': 851,
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }


plot['WLWL']  = {
                  'color': 851,
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }


plot['ggWW']  = {
                  'color': 850, # kAzure -10
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1.0
                  }

plot['WWewk']  = {
                  'color': 851, # kAzure -9 
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0   # ele/mu trigger efficiency   datadriven
                  }


plot['Vg']  = { 
                  'color': 859, # kAzure -1  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

plot['VgS_H'] = { 
                  'color'    : 617,   # kViolet + 1  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

plot['VgS_L'] = {
                  'color'    : 617,   # kViolet + 1  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }


plot['VZ']  = { 
                  'color': 858, # kAzure -2  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

plot['VVV']  = { 
                  'color': 857, # kAzure -3  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }


###
'''

# Htautau

plot['ZH_htt'] = {
                  'nameHR' : 'ZHtt',
                  'color': 632+3, # kRed+3 
                  'isSignal' : 1,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }

plot['bbH_htt'] = {
                  'nameHR' : 'bbHtt',
                  'color': 632-1, # kRed-1 
                  'isSignal' : 1,
                  'isData'   : 0,
                  'scale'    : 1    #
                  }

plot['ttH_htt'] = {
                  'nameHR' : 'bbHtt',
                  'color': 632-2, # kRed-1 
                  'isSignal' : 1,
                  'isData'   : 0,
                  'scale'    : 1    #
                  }


plot['ggZH_htt'] = {
                  'nameHR' : 'ggZHtt',
                  'color': 632+4, # kRed+4
                  'isSignal' : 1,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }

plot['WH_htt'] = {
                  'nameHR' : 'WHtt',
                  'color': 632+2, # kRed+2 
                  'isSignal' : 1,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }
'''

####


plot['qqH_htt'] = {
                  'nameHR' : 'qqHtt',
                  'color': 632+1, # kRed+1 
                  'isSignal' : 1,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }


plot['ggH_htt'] = {
                  'nameHR' : 'ggHtt',
                  'color': 632, # kRed 
                  'isSignal' : 1,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }
#
# HWW 

#plot['H_hww'] = {
#                  'nameHR' : 'Hww',
#                  'color': 632, # kRed 
#                  'isSignal' : 1,
#                  'isData'   : 0,    
#                  'scale'    : 1    #
#                  }

plot['ZH_hww'] = {
                  'nameHR' : 'ZH',
                  'color': 920+3, # kRed+3 
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }

plot['ggZH_hww'] = {
                  'nameHR' : 'ggZH',
                  'color': 920+4, # kRed+4
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }

plot['WH_hww'] = {
                  'nameHR' : 'WH',
                  'color': 920+2, # kRed+2 
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }


plot['ggH_hww'] = {
                  'nameHR' : 'ggH',
                  'color': 632, # kRed 
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }


plot['qqH_hww'] = {
                  'nameHR' : 'qqH',
                  'color': 632, # kRed                                                                                                                                                                                                       
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1    #                                                                                                                                                                                                         
                  }

#plot['bbH_hww'] = {
#                  'nameHR' : 'bbH',
#                  'color': 632+5, # kRed+5 
#                  'isSignal' : 1,
#                  'isData'   : 0,
#                  'scale'    : 1    #
#                  }

#plot['ttH_hww'] = {
#                  'nameHR' : 'ttH',
#                  'color': 632+6, # kRed+6
#                  'isSignal' : 1,
#                  'isData'   : 0,
#                  'scale'    : 1    #
#                  }
#

# data

plot['DATA']  = { 
                  'nameHR' : 'Data',
                  'color': 1 ,  
                  'isSignal' : 0,
                  'isData'   : 1 ,
                  'isBlind'  : 1
              }



# additional options

legend['lumi'] = 'L = 35.9/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'




