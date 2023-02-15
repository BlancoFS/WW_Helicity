# VBF configuration file                                                                                                                                                                                   

treeName = 'Events'

tag = 'WW_2018_1j'

# used by mkShape to define output directory for root files                                                                                                                                                
#outputDir = 'Full2018_v9/rootFile'
outputDir = '../../../../../../../../../../../../eos/user/s/sblancof/MC/tmp'

# file with TTree aliases                                                                                                                                                                                  
aliasesFile = 'Full2018_v9/aliases_1J.py'

# file with list of variables                                                                                                                                                                              
variablesFile = 'Full2018_v9/variables_1J.py'

# file with list of cuts                                                                                                                                                                                   
cutsFile = 'Full2018_v9/cuts_1J.py'

# file with list of samples                                                                                                                                                                                
samplesFile = 'Full2018_v9/samples_1J.py'

# file with plot configuration                                                                                                                                                                             
plotFile = 'Full2018_v9/plot.py'

# luminosity to normalize to (in 1/fb)                                                                                                                                                                     
lumi = 59.74

# used by mkPlot to define output directory for plots                                                                                                                                                      
# different from "outputDir" to do things more tidy                                                                                                                                                        
outputDirPlots = 'Full2018_v9/plotWW_2018'

# used by mkDatacards to define output directory for datacards                                                                                                                                             
outputDirDatacard = 'Full2018_v9/datacards'

# structure file for datacard                                                                                                                                                                              
structureFile = 'Full2018_v9/structure.py'

# nuisances file for mkDatacards and for mkShape                                                                                                                                                           
nuisancesFile = 'Full2018_v9/nuisances.py'
