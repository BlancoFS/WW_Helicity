#!/bin/bash                                                                                                                                                                                                                                  
export X509_USER_PROXY=/afs/cern.ch/user/s/sblancof/.proxy
voms-proxy-info
export SCRAM_ARCH=slc7_amd64_gcc820
export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch
source $VO_CMS_SW_DIR/cmsset_default.sh
cd /afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10
eval `scramv1 ru -sh`
cd /afs/cern.ch/work/s/sblancof/public/CMSSW_10_6_10/src/PlotsConfigurations/Configurations/WW/Full2016_v7/WW_helicity/DNN
#python loader.py
python doMAOS.py
#python doMatrixElement_HWW.py
