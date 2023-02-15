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
            ['A','Run2018A-UL2018-v1'] ,
            ['B','Run2018B-UL2018-v1'] ,
            ['C','Run2018C-UL2018-v1'] ,
            ['D','Run2018D-UL2018-v1'] ,
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
          nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50-LO')

else:
  files = nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_ext2') + \
          nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50-LO')


samples['DY'] = {
    'name': files,
    'weight': mcCommonWeight + '*( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0))',
    'FilesPerJob': 2,
}

addSampleWeight(samples,'DY','DYJetsToTT_MuEle_M-50','DY_NLO_pTllrw')
#addSampleWeight(samples,'DY','DYJetsToLL_M-50_ext2','DY_NLO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO','DY_LO_pTllrw')


###### Top #######

files = nanoGetSampleFiles(mcDirectory, 'TTTo2L2Nu') + \
        nanoGetSampleFiles(mcDirectory, 'ST_s-channel') + \
        nanoGetSampleFiles(mcDirectory, 'ST_t-channel_antitop') + \
        nanoGetSampleFiles(mcDirectory, 'ST_t-channel_top') + \
        nanoGetSampleFiles(mcDirectory, 'ST_tW_antitop') + \
        nanoGetSampleFiles(mcDirectory, 'ST_tW_top')

samples['top'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 1,
    'EventsPerJob': 20000,
}

addSampleWeight(samples,'top','TTTo2L2Nu','Top_pTrw')


###### WW ########

samples['WW'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'WWTo2L2Nu'),
    'weight': mcCommonWeight + '*nllW*ewknloW',
    'FilesPerJob': 1
}

samples['WWewk'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'WpWmJJ_EWK_QCD_noTop'),
    'weight': mcCommonWeight + '*(Sum$(abs(GenPart_pdgId)==6 || GenPart_pdgId==25)==0)', #filter tops and Higgs
    'FilesPerJob': 2
}


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
    'weight': mcCommonWeight + '*1.53/1.4', # updating k-factor
    'FilesPerJob': 1,
    'EventsPerJob': 25000
}


######## Vg ########


files = nanoGetSampleFiles(mcDirectory, 'ZGToLLG')

samples['Zg'] = {
    'name': files,
    'weight': mcCommonWeightNoMatch + '*(!(Gen_ZGstar_mass > 0))',
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 2
}

files = nanoGetSampleFiles(mcDirectory, 'WGToLNuG') 

samples['Wg'] = {
    'name': files,
    'weight': mcCommonWeightNoMatch + '*(Gen_ZGstar_mass <= 0)',
    'FilesPerJob': 2
}

######## ZgS ########

files = nanoGetSampleFiles(mcDirectory, 'ZGToLLG')

samples['ZgS'] = {
    'name': files,
    'weight': mcCommonWeight,
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 2,
}
addSampleWeight(samples, 'ZgS', 'ZGToLLG', '(Gen_ZGstar_mass > 0)*0.448')

######## WgS ######## 

files = nanoGetSampleFiles(mcDirectory, 'WGToLNuG') + \
        nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_mllmin4p0') # WZTo3LNu_mllmin01_ext1
        # nanoGetSampleFiles(mcDirectory, 'ZGToLLG') + \

samples['WgS'] = {
    'name': files,
    # 'weight': mcCommonWeight + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
    'weight': mcCommonWeight + ' * (gstarLow * 0.94)',
    'FilesPerJob': 2,
    # 'subsamples': {
    #   'L': 'gstarLow',
    #   'H': 'gstarHigh'
    #}
}
addSampleWeight(samples, 'WgS', 'WGToLNuG', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass <= 4.0)')
# addSampleWeight(samples, 'WgS', 'ZGToLLG', '(Gen_ZGstar_mass > 0)')
addSampleWeight(samples, 'WgS', 'WZTo3LNu_mllmin4p0', '(Gen_ZGstar_mass > 4.0)')

############ WZ ############

# files = nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Nu') + \
#         nanoGetSampleFiles(mcDirectory, 'ZZTo2Q2L_mllmin4p0') + \
#         nanoGetSampleFiles(mcDirectory, 'WZTo2Q2L_mllmin4p0') # 'WZTo2L2Q')

files = nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_mllmin4p0') + \
        nanoGetSampleFiles(mcDirectory, 'WZTo2Q2L_mllmin4p0')

samples['WZ'] = {
    'name': files,
    # 'weight': mcCommonWeight+embed_tautauveto + '*1.11',
    'weight': mcCommonWeight + ' * (gstarHigh)',
    'FilesPerJob': 2
}


############ ZZ ############

files = nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Nu') + \
        nanoGetSampleFiles(mcDirectory, 'ZZTo2Q2L_mllmin4p0') + \
        nanoGetSampleFiles(mcDirectory, 'ZZTo4L')

samples['ZZ'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 2
}

########## VVV #########

files = nanoGetSampleFiles(mcDirectory, 'ZZZ') + \
        nanoGetSampleFiles(mcDirectory, 'WZZ') + \
        nanoGetSampleFiles(mcDirectory, 'WWZ') + \
        nanoGetSampleFiles(mcDirectory, 'WWW')
#+ nanoGetSampleFiles(mcDirectory, 'WWG'), #should this be included? or is it already taken into account in the WW sample?

samples['VVV'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 2
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
    'FilesPerJob': 1
}

signals.append('qqH_hww')


################################################
#############   POLARIZATION  ##################
################################################


##################                                                                                                                                                                                         
#     ggH LL     #
##################

samples['ggH_HWLWL'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'GluGluHToWWTo2L2Nu_M125'), #+ nanoGetSampleFiles(mcDirectory, 'GGHjjToWWTo2L2Nu_minloHJJ_M125'), # Not yet
    'weight': mcCommonWeight + '*Higgs_WW_LL*(Higgs_WW_LL>-5)',
    #'weight': mcCommonWeight + '*(Higgs_WW_LL*(dphill<=1.7)*(Higgs_WW_LL>-5) + (Higgs_WW_LL*Higgs_WW_woInt)*(dphill>1.7)*(Higgs_WW_LL*Higgs_WW_woInt>-5))',
    'FilesPerJob': 1,
}
addSampleWeight(samples, 'ggH_HWLWL', 'GluGluHToWWTo2L2Nu_M125', '(HTXS_stage1_1_cat_pTjet30GeV<107)*Weight2MINLO*1092.7640/1073.2567') #only non GE2J categories with the weight to NNLOPS and renormalize integral                          
#addSampleWeight(samples, 'ggH_HWLWL', 'GGHjjToWWTo2L2Nu_minloHJJ_M125', '(HTXS_stage1_1_cat_pTjet30GeV>106)*1092.7640/1073.2567')

signals.append('ggH_HWLWL')


######################                                                                                                                                                                                                                                                         
#     ggH TT+Int     #                                                                                                                                                                                                                                                         
######################                                                                                                                                                                                                                                                         

samples['ggH_HWW_TTInt'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'GluGluHToWWTo2L2Nu_M125'), #+ nanoGetSampleFiles(mcDirectory, 'GGHjjToWWTo2L2Nu_minloHJJ_M125'), # Not yet                                                                                                                        
    'weight': mcCommonWeight + '*(Higgs_WW_TTInt*(Higgs_WW_TTInt>-50))',
    'FilesPerJob': 1,
}
addSampleWeight(samples, 'ggH_HWW_TTInt', 'GluGluHToWWTo2L2Nu_M125', '(HTXS_stage1_1_cat_pTjet30GeV<107)*Weight2MINLO*1092.7640/1073.2567') #only non GE2J categories with the weight to NNLOPS and renormalize integral                                             
#addSampleWeight(samples, 'ggH_HWW_TTInt', 'GGHjjToWWTo2L2Nu_minloHJJ_M125', '(HTXS_stage1_1_cat_pTjet30GeV>106)*1092.7640/1073.2567')                                                                                                                             

signals.append('ggH_HWW_TTInt')


##################                                                                                                                                                                                                                                                             
#     qqH LL     #                                                                                                                                                                                                                                                             
##################                                                                                                                                                                                                                                                             

samples['qqH_HWLWL'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'VBFHToWWTo2L2Nu_M125'),
    'weight': mcCommonWeight + '*(Higgs_WW_LL*(Higgs_WW_LL>-5))',
    #'weight': mcCommonWeight + '*(Higgs_WW_LL*(dphill<=1.7)*(Higgs_WW_LL>-5) + (Higgs_WW_LL*Higgs_WW_woInt)*(dphill>1.7)*(Higgs_WW_LL*Higgs_WW_woInt>-5))',    
    'FilesPerJob': 1,
} 

signals.append('qqH_HWLWL')



#####################                                                                                                                                                                                                                                                          
#   qqH TT+Int      #                                                                                                                                                                                                                                                          
#####################                                                                                                                                                                                                                                                          

samples['qqH_HWW_TTInt'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'VBFHToWWTo2L2Nu_M125'),
    'weight': mcCommonWeight + '*Higgs_WW_TTInt*(Higgs_WW_TTInt>-50.)',
    'FilesPerJob': 1,
}

signals.append('qqH_HWW_TTInt')


###########################################
############# ALT SIGNALS #################
###########################################

############ ZH H->WW ############

samples['ZH_hww'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'HZJ_HToWW_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 2
}

signals.append('ZH_hww')

samples['ggZH_hww'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'GluGluZH_HToWWTo2L2Nu_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 2
}

signals.append('ggZH_hww')

############ WH H->WW ############ 

samples['WH_hww'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'HWplusJ_HToWW_M125') + nanoGetSampleFiles(mcDirectory, 'HWminusJ_HToWW_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 2
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
    'FilesPerJob': 10
}

signals.append('ggH_htt')

samples['qqH_htt'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'VBFHToTauTau_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 10
}

signals.append('qqH_htt')


samples['ZH_htt'] = {  
    'name': nanoGetSampleFiles(mcDirectory, 'ZHToTauTau_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

signals.append('ZH_htt')


samples['WH_htt'] = {
    'name':  nanoGetSampleFiles(mcDirectory, 'WplusHToTauTau_M125') + nanoGetSampleFiles(mcDirectory, 'WminusHToTauTau_M125'),
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
  'FilesPerJob': 25
}

for _, sd in DataRun:
  for pd in DataSets:
    tag = pd + '_' + sd

    if (   ('DoubleMuon' in pd and 'Run2018B' in sd)
        or ('DoubleMuon' in pd and 'Run2018D' in sd)
        or ('DoubleMuon' in pd and 'Run2018D' in sd) 
        or ('SingleMuon' in pd and 'Run2018A' in sd)
        or ('SingleMuon' in pd and 'Run2018B' in sd)
        or ('SingleMuon' in pd and 'Run2018C' in sd)):
        print("sd      = {}".format(sd))
        print("pd      = {}".format(pd))
        print("Old tag = {}".format(tag))
        tag = tag.replace('v1','v2')
        print("New tag = {}".format(tag))

    files = nanoGetSampleFiles(fakeDirectory, tag)

    samples['Fake']['name'].extend(files)
    samples['Fake']['weights'].extend([DataTrig[pd]] * len(files))

###########################################
################## DATA ###################
###########################################

samples['DATA'] = {
  'name': [],
  'weight': 'LepWPCut*METFilter_DATA',
  'weights': [],
  'isData': ['all'],
  'FilesPerJob': 25
}

for _, sd in DataRun:
  for pd in DataSets:
    tag = pd + '_' + sd

    if (   ('DoubleMuon' in pd and 'Run2018B' in sd)
        or ('DoubleMuon' in pd and 'Run2018D' in sd)
        or ('DoubleMuon' in pd and 'Run2018D' in sd)
        or ('SingleMuon' in pd and 'Run2018A' in sd)
        or ('SingleMuon' in pd and 'Run2018B' in sd)
        or ('SingleMuon' in pd and 'Run2018C' in sd)):
        print("sd      = {}".format(sd))
        print("pd      = {}".format(pd))
        print("Old tag = {}".format(tag))
        tag = tag.replace('v1','v2')
        print("New tag = {}".format(tag))

    files = nanoGetSampleFiles(dataDirectory, tag)

    samples['DATA']['name'].extend(files)
    samples['DATA']['weights'].extend([DataTrig[pd]] * len(files))




