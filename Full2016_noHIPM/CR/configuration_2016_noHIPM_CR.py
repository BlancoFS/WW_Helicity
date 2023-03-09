# VBF configuration file                                                                                                                                                                                   

treeName = 'Events'

tag = 'WW_2016_noHIPM_CR'

# used by mkShape to define output directory for root files                                                                                                                                                
#outputDir = 'Full2018_v9/rootFile'
outputDir = '../../../../../../../../../../../../eos/user/s/sblancof/MC/tmp'

# file with TTree aliases                                                                                                                                                                                  
aliasesFile = 'Full2016_noHIPM/aliases_CR.py'

# file with list of variables                                                                                                                                                                              
variablesFile = 'Full2016_noHIPM/variables_CR.py'

# file with list of cuts                                                                                                                                                                                   
cutsFile = 'Full2016_noHIPM/cuts_CR.py'

# file with list of samples                                                                                                                                                                                
samplesFile = 'Full2016_noHIPM/samples_CR.py'

# file with plot configuration                                                                                                                                                                             
plotFile = 'Full2016_noHIPM/plot_CR.py'

# luminosity to normalize to (in 1/fb)                                                                                                                                                                     
lumi = 16.8

# used by mkPlot to define output directory for plots                                                                                                                                                      
# different from "outputDir" to do things more tidy                                                                                                                                                        
outputDirPlots = 'Full2016_noHIPM/plotWW_2016'

# used by mkDatacards to define output directory for datacards                                                                                                                                             
outputDirDatacard = 'Full2016_noHIPM/datacards'

# structure file for datacard                                                                                                                                                                              
structureFile = 'Full2016_noHIPM/structure.py'

# nuisances file for mkDatacards and for mkShape                                                                                                                                                           
nuisancesFile = 'Full2016_noHIPM/nuisances.py'
