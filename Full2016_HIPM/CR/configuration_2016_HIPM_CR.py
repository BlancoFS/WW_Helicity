# VBF configuration file                                                                                                                                                                                   

treeName = 'Events'

tag = 'WW_2016_HIPM_CR'

# used by mkShape to define output directory for root files                                                                                                                                                
#outputDir = 'Full2018_v9/rootFile'
outputDir = '../../../../../../../../../../../../eos/user/s/sblancof/MC/tmp'

# file with TTree aliases                                                                                                                                                                                  
aliasesFile = 'Full2016_HIPM/aliases_CR.py'

# file with list of variables                                                                                                                                                                              
variablesFile = 'Full2016_HIPM/variables_CR.py'

# file with list of cuts                                                                                                                                                                                   
cutsFile = 'Full2016_HIPM/cuts_CR.py'

# file with list of samples                                                                                                                                                                                
samplesFile = 'Full2016_HIPM/samples_CR.py'

# file with plot configuration                                                                                                                                                                             
plotFile = 'Full2016_HIPM/plot_CR.py'

# luminosity to normalize to (in 1/fb)                                                                                                                                                                     
lumi = 19.5

# used by mkPlot to define output directory for plots                                                                                                                                                      
# different from "outputDir" to do things more tidy                                                                                                                                                        
outputDirPlots = 'Full2016_HIPM/plotWW_2016'

# used by mkDatacards to define output directory for datacards                                                                                                                                             
outputDirDatacard = 'Full2016_HIPM/datacards'

# structure file for datacard                                                                                                                                                                              
structureFile = 'Full2016_HIPM/structure.py'

# nuisances file for mkDatacards and for mkShape                                                                                                                                                           
nuisancesFile = 'Full2016_HIPM/nuisances.py'
