# VBF configuration file                                                                                                                                                                                   

treeName = 'Events'

tag = 'WW_2017_CR'

# used by mkShape to define output directory for root files                                                                                                                                                
#outputDir = 'Full2018_v9/rootFile'
outputDir = '../../../../../../../../../../../../eos/user/s/sblancof/MC/tmp'

# file with TTree aliases                                                                                                                                                                                  
aliasesFile = 'Full2017_v9/aliases_CR.py'

# file with list of variables                                                                                                                                                                              
variablesFile = 'Full2017_v9/variables_CR.py'

# file with list of cuts                                                                                                                                                                                   
cutsFile = 'Full2017_v9/cuts_CR.py'

# file with list of samples                                                                                                                                                                                
samplesFile = 'Full2017_v9/samples_CR.py'

# file with plot configuration                                                                                                                                                                             
plotFile = 'Full2017_v9/plot_CR.py'

# luminosity to normalize to (in 1/fb)                                                                                                                                                                     
lumi = 41.48

# used by mkPlot to define output directory for plots                                                                                                                                                      
# different from "outputDir" to do things more tidy                                                                                                                                                        
outputDirPlots = 'Full2017_v9/plotWW_2017'

# used by mkDatacards to define output directory for datacards                                                                                                                                             
outputDirDatacard = 'Full2017_v9/datacards'

# structure file for datacard                                                                                                                                                                              
structureFile = 'Full2017_v9/structure.py'

# nuisances file for mkDatacards and for mkShape                                                                                                                                                           
nuisancesFile = 'Full2017_v9/nuisances.py'
