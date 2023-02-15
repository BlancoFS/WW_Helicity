# cuts

#supercut = ' mll > 12 \
#            && Lepton_pt[0]>25 \
#            && Lepton_pt[1]>13 \
#            && (nLepton>=2 && Alt$(Lepton_pt[2],0)<10) \
#            && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5 \
#            && ptll>30 \
#            && PuppiMET_pt > 20 \
#            && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) \
#            '

_tmp = [
     'Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13',
     'Lepton_pt[0] > 25.',
     'Lepton_pt[1] > 15.',
     '(abs(Lepton_pdgId[1]) == 13 || Lepton_pt[1] > 13.)',
     '(nLepton >= 2 && Alt$(Lepton_pt[2], 0) < 10.)'
     ]

supercut = ' && '.join(_tmp)


'''
## Top control regions
cuts['hww2l2v_13TeV_top']  = { 
   'expr' : 'topcr',
    # Define the sub-categorization of topcr
   'categories' : {
       '2j' : 'multiJet',
   }
}

## DYtt control regions
cuts['hww2l2v_13TeV_dytt']  = { 
   'expr' : 'dycr',
   # Define the sub-categorization of dycr
   'categories' : { 
       '2j' : 'multiJet',
   }
}
'''

cuts['hww2l2v_13TeV_WW'] = {
 'expr' : 'sr',
 'categories' : {
     '2j' : 'multiJet && BDTG4D3_2J<0.75 && BDTG4D3_VBF<0.90'
 }
}


cuts['hww2l2v_13TeV_WW_BDT'] = {
 'expr' : 'sr',
 'categories' : {
     '2j' : 'multiJet && BDTG4D3_2J>0.05 && BDTG4D3_2J<0.75 && BDTG4D3_VBF>0.05 && BDTG4D3_VBF<0.90'
 }
}

