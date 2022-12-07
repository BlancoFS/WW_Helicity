import os
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # ggH2018
configurations = os.path.dirname(configurations) # Differential
configurations = os.path.dirname(configurations) # Configurations

from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight, getBaseWnAOD

def nanoGetSampleFiles(inputDir, sample):
    try:
        if _samples_noload:
            return []
    except NameError:
        pass

    return getSampleFiles(inputDir, sample, True, 'nanoLatino_')

# samples

try:
    len(samples)
except NameError:
    import collections
    samples = collections.OrderedDict()

################################################
################# SKIMS ########################
################################################

mcProduction = 'Summer20UL18_106x_nAODv9_Full2018v9'

dataReco = 'Run2018_UL2018_nAODv9_Full2018v9'

fakeReco = dataReco

mcSteps = 'MCl1loose2018v9__MCCorr2018v9NoJERInHorn__l2tightOR2018v9'

fakeSteps = 'DATAl1loose2018v9__l2loose__fakeW'

dataSteps = 'DATAl1loose2018v9__l2loose__l2tightOR2018v9'

##############################################
###### Tree base directory for the site ######
##############################################

SITE=os.uname()[1]
if    'iihe' in SITE:
  treeBaseDir = '/pnfs/iihe/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'
elif  'cern' in SITE:
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'

def makeMCDirectory(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var='__trigFix'))

mcDirectory = makeMCDirectory()
fakeDirectory = os.path.join(treeBaseDir, fakeReco, fakeSteps)
dataDirectory = os.path.join(treeBaseDir, dataReco, dataSteps)

################################################
############ DATA DECLARATION ##################
################################################

DataRun = [
            ['A','Run2018A-02Apr2020-v1'] ,
            ['B','Run2018B-02Apr2020-v1'] ,
            ['C','Run2018C-02Apr2020-v1'] ,
            ['D','Run2018D-02Apr2020-v1'] ,
          ]

DataSets = ['MuonEG','DoubleMuon','SingleMuon','EGamma']

DataTrig = {
            'MuonEG'         : 'Trigger_ElMu' ,
            'DoubleMuon'     : '!Trigger_ElMu && Trigger_dblMu' ,
            'SingleMuon'     : '!Trigger_ElMu && !Trigger_dblMu && Trigger_sngMu' ,
            'EGamma'         : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && (Trigger_sngEl || Trigger_dblEl)' ,
           }


#########################################
############ MC COMMON ##################
#########################################

mcCommonWeightNoMatch = 'XSWeight*SFweight*METFilter_MC'
mcCommonWeight = 'XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC'

###########################################
#############  BACKGROUNDS  ###############
###########################################

###### DY #######
useDYtt = True

files=[]
if useDYtt:
  files = nanoGetSampleFiles(mcDirectory, 'DYJetsToTT_MuEle_M-50') + \
          nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50-LO_ext1')

else:
  files = nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_ext2') + \
          nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50-LO_ext1')


samples['DY'] = {
    'name': files,
    'weight': mcCommonWeight + '*( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0))',
    'FilesPerJob': 6,
}

addSampleWeight(samples,'DY','DYJetsToTT_MuEle_M-50','DY_NLO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_ext2','DY_NLO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO_ext1','DY_LO_pTllrw')

###### Top #######

files = nanoGetSampleFiles(mcDirectory, 'TTTo2L2Nu') + \
    nanoGetSampleFiles(mcDirectory, 'ST_s-channel') + \
    nanoGetSampleFiles(mcDirectory, 'ST_t-channel_antitop') + \
    nanoGetSampleFiles(mcDirectory, 'ST_t-channel_top') + \
    nanoGetSampleFiles(mcDirectory, 'ST_tW_antitop_noHad') + \
    nanoGetSampleFiles(mcDirectory, 'ST_tW_top_noHad')

samples['top'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 1,
}

addSampleWeight(samples,'top','TTTo2L2Nu','Top_pTrw')


###### WW ########

samples['WW'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'WWTo2L2Nu'),
    'weight': mcCommonWeight+embed_tautauveto + '*nllW*ewknloW',
    'FilesPerJob': 3
}

#samples['WWewk'] = {
#    'name': nanoGetSampleFiles(mcDirectory, 'WpWmJJ_EWK_QCD_noTop'),
#    'weight': mcCommonWeight + '*(Sum$(abs(GenPart_pdgId)==6 || GenPart_pdgId==25)==0)', #filter tops and Higgs
#    'FilesPerJob': 4
#}

# k-factor 1.4 already taken into account in XSWeight
files = nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENEN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENMN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENTN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNEN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNMN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNTN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNEN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNMN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNTN')

samples['ggWW'] = {
    'name': files,
    'weight': mcCommonWeight+embed_tautauveto + '*1.53/1.4', # updating k-factor
    'FilesPerJob': 4
}

######## Vg ########

useWgFXFX=True

if useWgFXFX:
  files = nanoGetSampleFiles(mcDirectory, 'WGToLNuG') + \ 
      nanoGetSampleFiles(mcDirectory, 'Wg_AMCNLOFXFX_01J') + \
      nanoGetSampleFiles(mcDirectory, 'Wg_AMCNLOFXFX_01J_PDF') + \
      nanoGetSampleFiles(mcDirectory, 'ZGToLLG')
  
  samples['Vg'] = {
      'name': files,
      'weight': mcCommonWeightNoMatch + '*(Gen_ZGstar_mass <= 0)',
      'FilesPerJob': 2
  }
  
  wgbasew = getBaseWnAOD(mcDirectory,'Summer20UL18_106x_nAODv9_Full2018v9',['WGToLNuG','Wg_AMCNLOFXFX_01J','Wg_AMCNLOFXFX_01J_PDF'])
  addSampleWeight(samples,'Vg','WGToLNuG','191.4/586.*'+wgbasew+'/baseW')
  addSampleWeight(samples,'Vg','Wg_AMCNLOFXFX_01J','191.4/586.*'+wgbasew+'/baseW')
  addSampleWeight(samples,'Vg','Wg_AMCNLOFXFX_01J_PDF','191.4/586.*'+wgbasew+'/baseW')
  
  
  ######## VgS ########
  
  files = nanoGetSampleFiles(mcDirectory, 'WGToLNuG') + \ 
      nanoGetSampleFiles(mcDirectory, 'Wg_AMCNLOFXFX_01J') + \
      nanoGetSampleFiles(mcDirectory, 'Wg_AMCNLOFXFX_01J_PDF') + \
      nanoGetSampleFiles(mcDirectory, 'ZGToLLG') + \
      nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_mllmin0p1')
  
  samples['VgS'] = {
      'name': files,
      'weight': mcCommonWeight + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
      'FilesPerJob': 4,
      'subsamples': {
        'L': 'gstarLow',
        'H': 'gstarHigh'
      }
  }
  
  addSampleWeight(samples, 'VgS', 'WGToLNuG', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)*191.4/586.*'+wgbasew+'/baseW')
  addSampleWeight(samples, 'VgS', 'Wg_AMCNLOFXFX_01J', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)*191.4/586.*'+wgbasew+'/baseW')
  addSampleWeight(samples, 'VgS', 'Wg_AMCNLOFXFX_01J_PDF', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)*191.4/586.*'+wgbasew+'/baseW')
  addSampleWeight(samples, 'VgS', 'ZGToLLG', '(Gen_ZGstar_mass > 0)')
  addSampleWeight(samples, 'VgS', 'WZTo3LNu_mllmin0p1', '(Gen_ZGstar_mass > 0.1)')

else:
  files = nanoGetSampleFiles(mcDirectory, 'Wg_MADGRAPHMLM') + \
      nanoGetSampleFiles(mcDirectory, 'ZGToLLG')
  
  samples['Vg'] = {
      'name': files,
      'weight': mcCommonWeightNoMatch+embed_tautauveto + '*(Gen_ZGstar_mass <= 0)',
      'FilesPerJob': 2
  }
  
  
  ######## VgS ########
  
  files = nanoGetSampleFiles(mcDirectory, 'WGToLNuG') + \
      nanoGetSampleFiles(mcDirectory, 'ZGToLLG') + \
      nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_mllmin0p1')
  
  samples['VgS'] = {
      'name': files,
      'weight': mcCommonWeight + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
      'FilesPerJob': 2,
      'subsamples': {
        'L': 'gstarLow',
        'H': 'gstarHigh'
      }
  }
  addSampleWeight(samples, 'VgS', 'WGToLNuG', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
  addSampleWeight(samples, 'VgS', 'ZGToLLG', '(Gen_ZGstar_mass > 0)')
  addSampleWeight(samples, 'VgS', 'WZTo3LNu_mllmin0p1', '(Gen_ZGstar_mass > 0.1)')

############ VZ ############

files = nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Nu') + \
    nanoGetSampleFiles(mcDirectory, 'ZZTo2Q2L_mllmin4p0') + \
    nanoGetSampleFiles(mcDirectory, 'ZZTo4L') + \
    nanoGetSampleFiles(mcDirectory, 'WZTo2Q2L_mllmin4p0')

samples['VZ'] = {
    'name': files,
    'weight': mcCommonWeight + '*1.11',
    'FilesPerJob': 4
}

########## VVV #########

files = nanoGetSampleFiles(mcDirectory, 'ZZZ') + \
    nanoGetSampleFiles(mcDirectory, 'WZZ') + \
    nanoGetSampleFiles(mcDirectory, 'WWZ') + \
    nanoGetSampleFiles(mcDirectory, 'WWW')

samples['VVV'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}


###########################################
#############   SIGNALS  ##################
###########################################
signals = []

#### ggH -> WW

samples['ggH_hww'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'GluGluHToWWTo2L2Nu_M125'), #+ nanoGetSampleFiles(mcDirectory, 'GGHjjToWWTo2L2Nu_minloHJJ_M125'), # Not yet
    'weight': mcCommonWeight,
    'FilesPerJob': 1,
}
addSampleWeight(samples, 'ggH_hww', 'GluGluHToWWTo2L2Nu_M125', '(HTXS_stage1_1_cat_pTjet30GeV<107)*Weight2MINLO*1092.7640/1073.2567') #only non GE2J categories with the weight to NNLOPS and renormalize integral                          
#addSampleWeight(samples, 'ggH_hww', 'GGHjjToWWTo2L2Nu_minloHJJ_M125', '(HTXS_stage1_1_cat_pTjet30GeV>106)*1092.7640/1073.2567')

signals.append('ggH_hww')


############ VBF H->WW ############
samples['qqH_hww'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'VBFHToWWTo2L2Nu_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

signals.append('qqH_hww')


################################################
#############   POLARIZATION  ##################
################################################

samples['ggH_HWLWL'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'GluGluHToWWTo2L2Nu_M125'), #+ nanoGetSampleFiles(mcDirectory, 'GGHjjToWWTo2L2Nu_minloHJJ_M125'), # Not yet
    'weight': mcCommonWeight + 'Higgs_WW_LL',
    'FilesPerJob': 1,
}
addSampleWeight(samples, 'ggH_HWLWL', 'GluGluHToWWTo2L2Nu_M125', '(HTXS_stage1_1_cat_pTjet30GeV<107)*Weight2MINLO*1092.7640/1073.2567') #only non GE2J categories with the weight to NNLOPS and renormalize integral                          
#addSampleWeight(samples, 'ggH_HWLWL', 'GGHjjToWWTo2L2Nu_minloHJJ_M125', '(HTXS_stage1_1_cat_pTjet30GeV>106)*1092.7640/1073.2567')

signals.append('ggH_HWLWL')




samples['ggH_HWTWT'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'GluGluHToWWTo2L2Nu_M125'), #+ nanoGetSampleFiles(mcDirectory, 'GGHjjToWWTo2L2Nu_minloHJJ_M125'), # Not yet
    'weight': mcCommonWeight + 'Higgs_WW_TT',
    'FilesPerJob': 1,
}
addSampleWeight(samples, 'ggH_HWTWT', 'GluGluHToWWTo2L2Nu_M125', '(HTXS_stage1_1_cat_pTjet30GeV<107)*Weight2MINLO*1092.7640/1073.2567') #only non GE2J categories with the weight to NNLOPS and renormalize integral                          
#addSampleWeight(samples, 'ggH_HWTWT', 'GGHjjToWWTo2L2Nu_minloHJJ_M125', '(HTXS_stage1_1_cat_pTjet30GeV>106)*1092.7640/1073.2567')

signals.append('ggH_HWTWT')




samples['qqH_HWLWL'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'VBFHToWWTo2L2Nu_M125'),
    'weight': mcCommonWeight + 'Higgs_WW_LL',
    'FilesPerJob': 4
}

signals.append('qqH_HWLWL')


samples['qqH_HWTWT'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'VBFHToWWTo2L2Nu_M125'),
    'weight': mcCommonWeight + 'Higgs_WW_TT',
    'FilesPerJob': 4
}

signals.append('qqH_HWTWT')




###########################################
############# ALT SIGNALS #################
###########################################

############ ZH H->WW ############

samples['ZH_hww'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'HZJ_HToWW_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

signals.append('ZH_hww')

samples['ggZH_hww'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'GluGluZH_HToWWTo2L2Nu_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

signals.append('ggZH_hww')

############ WH H->WW ############  Not yet

samples['WH_hww'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'HWplusJ_HToWWTo2L2Nu_WToLNu_M125') + nanoGetSampleFiles(mcDirectory, 'HWminusJ_HToWW_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

signals.append('WH_hww')

############ ttH ############

samples['ttH_hww'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'ttHToNonbb_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 1
}

signals.append('ttH_hww')

############ H->TauTau ############

samples['ggH_htt'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'GluGluHToTauTau_M125_Powheg'),
    'weight': mcCommonWeight,
    'FilesPerJob': 20
}

signals.append('ggH_htt')

samples['qqH_htt'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'VBFHToTauTau_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 10
}

signals.append('qqH_htt')

## Not yet

#samples['ZH_htt'] = {  
#    'name': nanoGetSampleFiles(mcDirectory, 'HZJ_HToTauTau_M125'),
#    'weight': mcCommonWeight,
#    'FilesPerJob': 4
#}
#
#signals.append('ZH_htt')


samples['WH_htt'] = {
    'name':  nanoGetSampleFiles(mcDirectory, 'HWplusJ_HToTauTau_M125') + nanoGetSampleFiles(mcDirectory, 'HWminusJ_HToTauTau_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

signals.append('WH_htt')

###########################################
################## FAKE ###################
###########################################

samples['Fake'] = {
  'name': [],
  'weight': 'METFilter_DATA*fakeW',
  'weights': [],
  'isData': ['all'],
  'FilesPerJob': 50,
  #'suppressNegative' :['all'],
  #'suppressNegativeNuisances' :['all'],
}

for _, sd in DataRun:
  for pd in DataSets:
    files = nanoGetSampleFiles(fakeDirectory, pd + '_' + sd)
    samples['Fake']['name'].extend(files)
    samples['Fake']['weights'].extend([DataTrig[pd]] * len(files))

'''
samples['Fake']['subsamples'] = {
  'em': 'abs(Lepton_pdgId[0]) == 11',
  'me': 'abs(Lepton_pdgId[0]) == 13'
}
'''

###########################################
################## DATA ###################
###########################################

samples['DATA'] = {
  'name': [],
  'weight': 'METFilter_DATA*LepWPCut',
  'weights': [],
  'isData': ['all'],
  'FilesPerJob': 50
}

for _, sd in DataRun:
  for pd in DataSets:
    files = nanoGetSampleFiles(dataDirectory, pd + '_' + sd)
    samples['DATA']['name'].extend(files)
    samples['DATA']['weights'].extend([DataTrig[pd]] * len(files))
