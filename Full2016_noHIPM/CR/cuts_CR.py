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
     #'Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13',
     'Lepton_pt[0] > 25.',
     'Lepton_pt[1] > 15.',
     '(abs(Lepton_pdgId[1]) == 13 || Lepton_pt[1] > 13.)',
     '(nLepton >= 2 && Alt$(Lepton_pt[2], 0) < 10.)'
     ]

supercut = ' && '.join(_tmp)


### Inclusive

cuts['hww2l2v_13TeV_WW_noVeto_Inclusive']  = {
   'expr' : 'mth>40 && mtw2>30 && mll>100 && Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13',
}
cuts['hww2l2v_13TeV_top_Inclusive']  = {
   'expr' : 'topcr && Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13',
}

cuts['hww2l2v_13TeV_WW_Inclusive']  = {
   'expr' : 'mth>40 && mtw2>30 && bVeto && mll>100 && Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13',
}

cuts['hww2l2v_13TeV_Inclusive']  = {
   'expr' : 'mtw2>30 && mth>40 && mll>20 && Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13',
}



## Top control regions
cuts['hww2l2v_13TeV_top']  = { 
   'expr' : 'topcr && Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13',
    # Define the sub-categorization of topcr
   'categories' : {
       '0j' : 'zeroJet',
       '1j' : 'oneJet && Alt$(CleanJet_pt[1],0)<30',
       '2j' : 'multiJet',
   }
}

## DYtt control regions
cuts['hww2l2v_13TeV_dytt']  = { 
   'expr' : 'mth<40 && mtw2>30 && bVeto && mll>12 && Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13',
   'categories' : { 
       '0j' : 'zeroJet',
       '1j' : 'oneJet && Alt$(CleanJet_pt[1],0)<30',
       '2j' : 'multiJet',
   }
}


cuts['hww2l2v_13TeV_WW']  = {
   'expr' : 'mth>40 && mtw2>30 && bVeto && mll>100 && Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13',
   'categories' : {
       '0j' : 'zeroJet',
       '1j' : 'oneJet && Alt$(CleanJet_pt[1],0)<30',
       '2j' : 'multiJet',
   }
}

cuts['hww2l2v_13TeV_WW_mth60']  = {
   'expr' : 'mth>60 && mtw2>30 && bVeto && mll>100 && Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13',
   'categories' : {
       '0j' : 'zeroJet',
       '1j' : 'oneJet && Alt$(CleanJet_pt[1],0)<30',
       '2j' : 'multiJet',
   }
}

cuts['hww2l2v_13TeV_WW_noVeto']  = {
   'expr' : 'mth>40 && mtw2>30 && mll>100 && Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13',
   'categories' : {
       '0j' : 'zeroJet',
       '1j' : 'oneJet && Alt$(CleanJet_pt[1],0)<30',
       '2j' : 'multiJet',
   }
}


