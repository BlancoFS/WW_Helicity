#WW cuts                                                                                                                                                                                               


#-------------------------------------------------------------------------------                                                                                                                           
# supercut                                                                                                                                                                                                 
#-------------------------------------------------------------------------------                                                                                                                           
_tmp = [
     'Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13',
     'Lepton_pt[0] > 5.',
     'Lepton_pt[1] > 5.',
     '(abs(Lepton_pdgId[1]) == 13 || Lepton_pt[1] > 5.)',
     '(nLepton >= 2 && Alt$(Lepton_pt[2], 0) < 10.)'
     ]

supercut = ' && '.join(_tmp)


def addcut(name, exprs):
    cuts[name] = ' && '.join(exprs)



#-------------------------------------------------------------------------------                                                                                                                                                             
# Gen                                                                                                                                                                                                                               
#-------------------------------------------------------------------------------                                                                                                                                                             
_tmp = [
     'Lepton_pt[0] > 25.',
     'Lepton_pt[1] > 20.',
     ]

addcut('NoCuts', _tmp)

_tmp = [
     'Lepton_pt[0] > 25.',
     'Lepton_pt[1] > 20.',
     '(Sum$(CleanJet_pt>30) == 0 || Alt$(CleanJet_pt[0], 0) < 30)'
     ]

addcut('NoCuts_0J', _tmp)

_tmp = [
     'Lepton_pt[0] > 25.',
     'Lepton_pt[1] > 20.',
     '(Sum$(CleanJet_pt>30) == 1)'
     ]

addcut('NoCuts_1J', _tmp)


_tmp = [
     'Lepton_pt[0] > 25.',
     'Lepton_pt[1] > 20.',
     '(Sum$(CleanJet_pt>30) >= 2)'
     ]

addcut('NoCuts_2J', _tmp)

