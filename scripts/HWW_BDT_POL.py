import ROOT
import numpy as np

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class HWW_VBF_DNN(Module):
  
    def __init__(self, sample):
        print '####################', sample
        self.sample = sample
        self.cmssw_base = os.getenv('CMSSW_BASE')
        self.cmssw_arch = os.getenv('SCRAM_ARCH')


        
   def beginJob(self):
       pass
   def endJob(self):
       pass
   def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        
        self.inputFile = inputFile

        self.out = wrappedOutputTree        
        self.out.branch('Higgs_WW_LL','F')
        self.out.branch('Higgs_WW_TT','F')

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        
        
        Higgs_WW_LL = 1.0
        Higgs_WW_TT = 1.0
        
        GenPart = Collection(event, 'GenPart')
        
        genWp = ROOT.Math.PtEtaPhiEVector()
        genWm = ROOT.Math.PtEtaPhiEVector()
        genlp = ROOT.Math.PtEtaPhiEVector()
        genlm = ROOT.Math.PtEtaPhiEVector()
        gennup = ROOT.Math.PtEtaPhiEVector()
        gennum = ROOT.Math.PtEtaPhiEVector()
        genH = ROOT.Math.PtEtaPhiEVector()
        vector_lp = ROOT.TLorentzVector()
        vector_lm = ROOT.TLorentzVector() 
        vector_nup = ROOT.TLorentzVector()
        vector_num = ROOT.TLorentzVector()
        vector_Wp = ROOT.TLorentzVector() 
        vector_Wm = ROOT.TLorentzVector()
  
        WP = ROOT.TLorentzVector()
        WM = ROOT.TLorentzVector()
        H = ROOT.TLorentzVector()
        
        MW = 8.041900e+01
        WW = 2.047600e+00
        ghWW = 2*MW*MW/246
        GF = ROOT.Math.sqrt(2)/(2*246*246)
        cL = GF*MW*MW*MW/(6.0 * ROOT.Math.Pi()*ROOT.Math.sqrt(2))
        cR = GF*MW*MW*MW/(6.0 * ROOT.Math.Pi()*ROOT.Math.sqrt(2))
    
        number_elec = 0
        number_muon = 0
        number_tau = 0
  
        pos_wp = 999
        pos_wm = 999
  
        mother_pos = 0
        
        nGen = GenPart._len
        
        for p in range(0, nGen+1):
        
          # Leptons 
          
          mother_pos = GenPart[p].genPartIdxMother
          if (GenPart[p].pdgId==11 and GenPart[mother_pos].pdgId==-24 and GenPart[GenPart[mother_pos].genPartIdxMother].pdgId!=15):
      
            pos_wm = mother_pos
            number_elec = number_elec + 1
            vector_lm.SetPtEtaPhiM(GenPart[p].pt, GenPart[p].eta, GenPart[p].phi, 0.0)
            genlm.SetCoordinates(GenPart[p].pt, GenPart[p].eta, GenPart[p].phi, vector_lm.E())
      
          elif (GenPart[p].pdgId==-11 and GenPart[mother_pos].pdgId==24 and GenPart[GenPart[mother_pos].genPartIdxMother].pdgId!=-15):
      
            pos_wp = mother_pos
            number_elec = number_elec + 1
            vector_lp.SetPtEtaPhiM(GenPart[p].pt, GenPart[p].eta, GenPart[p].phi, 0.0)
            genlp.SetCoordinates(GenPart[p].pt, GenPart[p].eta, GenPart[p].phi, vector_lp.E())    
      
          elif (GenPart[p].pdgId==13 and GenPart[mother_pos].pdgId==-24 and GenPart[GenPart[mother_pos].genPartIdxMother].pdgId!=15):
      
            pos_wm = mother_pos
            number_muon = number_muon + 1
            vector_lm.SetPtEtaPhiM(GenPart[p].pt, GenPart[p].eta, GenPart[p].phi, 0.0)
            genlm.SetCoordinates(GenPart[p].pt, GenPart[p].eta, GenPart[p].phi, vector_lm.E())
      
          elif (GenPart[p].pdgId==-13 and GenPart[mother_pos].pdgId==24 and GenPart[GenPart[mother_pos].genPartIdxMother].pdgId!=-15):
      
            pos_wp = mother_pos
            number_muon = number_muon + 1
            vector_lp.SetPtEtaPhiM(GenPart[p].pt, GenPart[p].eta, GenPart[p].phi, 0.0)
            genlp.SetCoordinates(GenPart[p].pt, GenPart[p].eta, GenPart[p].phi, vector_lp.E())    
      
          elif (GenPart[p].pdgId==15 and GenPart[mother_pos].pdgId==-24):
      
            pos_wm = mother_pos
            number_tau = number_tau + 1
            vector_lm.SetPtEtaPhiM(GenPart[p].pt, GenPart[p].eta, GenPart[p].phi, 0.0)
            genlm.SetCoordinates(GenPart[p].pt, GenPart[p].eta, GenPart[p].phi, vector_lm.E())
      
          elif (GenPart[p].pdgId==-15 and GenPart[mother_pos].pdgId==24):
      
            pos_wp = mother_pos
            number_tau = number_tau + 1
            vector_lp.SetPtEtaPhiM(GenPart[p].pt, GenPart[p].eta, GenPart[p].phi, 0.0)
            genlp.SetCoordinates(GenPart[p].pt, GenPart[p].eta, GenPart[p].phi, vector_lp.E())
      
          
      
      
          # Neutrinos
      
          if (GenPart[p].pdgId==-12 and GenPart[mother_pos].pdgId==-24 and GenPart[GenPart[mother_pos].genPartIdxMother].pdgId!=15): 
      
            vector_num.SetPtEtaPhiM(GenPart[p].pt, GenPart[p].eta, GenPart[p].phi, 0.0)
            gennum.SetCoordinates(GenPart[p].pt, GenPart[p].eta, GenPart[p].phi, vector_num.E())
      
          elif (GenPart[p].pdgId==12 and GenPart[mother_pos].pdgId==24 and GenPart[GenPart[mother_pos].genPartIdxMother].pdgId!=-15): 
      
            vector_nup.SetPtEtaPhiM(GenPart[p].pt, GenPart[p].eta, GenPart[p].phi, 0.0)
            gennup.SetCoordinates(GenPart[p].pt, GenPart[p].eta, GenPart[p].phi, vector_nup.E())    
      
          elif (GenPart[p].pdgId==-14 and GenPart[mother_pos].pdgId==-24 and GenPart[GenPart[mother_pos].genPartIdxMother].pdgId!=15): 
      
            vector_num.SetPtEtaPhiM(GenPart[p].pt, GenPart[p].eta, GenPart[p].phi, 0.0)
            gennum.SetCoordinates(GenPart[p].pt, GenPart[p].eta, GenPart[p].phi, vector_num.E())
      
          elif (GenPart[p].pdgId==14 and GenPart[mother_pos].pdgId==24 and GenPart[GenPart[mother_pos].genPartIdxMother].pdgId!=-15){:
      
            vector_nup.SetPtEtaPhiM(GenPart[p].pt, GenPart[p].eta, GenPart[p].phi, 0.0)
            gennup.SetCoordinates(GenPart[p].pt, GenPart[p].eta, GenPart[p].phi, vector_nup.E())    
      
          elif (GenPart[p].pdgId==-16 and GenPart[mother_pos].pdgId==-24):
      
            vector_num.SetPtEtaPhiM(GenPart[p].pt, GenPart[p].eta, GenPart[p].phi, 0.0)
            gennum.SetCoordinates(GenPart[p].pt, GenPart[p].eta, GenPart[p].phi, vector_num.E())
      
          elif (GenPart[p].pdgId==16 and GenPart[mother_pos].pdgId==24):
      
            vector_nup.SetPtEtaPhiM(GenPart[p].pt, GenPart[p].eta, GenPart[p].phi, 0.0)
            gennup.SetCoordinates(GenPart[p].pt, GenPart[p].eta, GenPart[p].phi, vector_nup.E())
      
          
      
        # End loop over particles
  
        # Assign the four-vector of the Ws
        vector_Wp.SetPtEtaPhiM(GenPart[pos_wp].pt, GenPart[pos_wp].eta, GenPart[pos_wp].phi, GenPart[pos_wp].mass) # W plus
        genWp.SetCoordinates(GenPart[pos_wp].pt, GenPart[pos_wp].eta, GenPart[pos_wp].phi, vector_Wp.E())
            
        vector_Wm.SetPtEtaPhiM(GenPart[pos_wm].pt, GenPart[pos_wm].eta, GenPart[pos_wm].phi, GenPart[pos_wm].mass) # W minus
        genWm.SetCoordinates(GenPart[pos_wm].pt, GenPart[pos_wm].eta, GenPart[pos_wm].phi, vector_Wm.E())
        
      
        if (((number_elec==0 or number_muon==0) and number_tau==0) or pos_wp==999 or pos_wm==999):
          Higgs_WW_LL = 1.0
          Higgs_WW_TT = 1.0                                                                                                                           
          self.out.fillBranch('Higgs_WW_LL', Higgs_WW_LL)
          self.out.fillBranch('Higgs_WW_TT', Higgs_WW_TT)
  
          return True
        
      
        # Boost over lepton from the Ws reference frame
        # Compute theta star  
      
        WP = vector_Wp
        WM = vector_Wm
        H = WP + WM
        
        genH.SetCoordinates(H.Pt(), H.Eta(), H.Phi(), H.E());
        
        hRF = ROOT.Math.XYZVector()  
        hRF = henH.BoostToCM();
        
        leppWRF = ROOT.Math.XYZVector()
        lepmWRF = ROOT.Math.XYZVector()
        
        WpHRF = ROOT.Math.XYZVector()
        WmHRF = ROOT.Math.XYZVector()
      
        WpHRF = ROOT.Math.VectorUtil.boost(genWp, hRF)
        WmHRF = ROOT.Math.VectorUtil.boost(genWm, hRF)
        
        leppWRF = ROOT.Math.VectorUtil.boost(genlp, WpHRF)
        nupWRF = ROOT.Math.VectorUtil.boost(gennum, WmHRF)
        
        theta_Wp_star = ROOT.Math.VectorUtil.Angle(leppWRF, genWp)
        theta_Wm_star = ROOT.Math.VectorUtil.Angle(nupWRF, genWm)
      
        cos_Wp_theta_star = ROOT.Math.cos(theta_Wp_star)
        cos_Wm_theta_star = ROOT.Math.cos(theta_Wm_star)
        dphill = leppWRF.Phi() - nupWRF.Phi();
      
        # https://arxiv.org/pdf/2105.07972.pdf
        
        #/////////////////////////////////////
        #//             |ALL|^2             //
        #/////////////////////////////////////
        
        K = ((H.M()*H.M() - WP.M()*WP.M() - WM.M()*WM.M()) / (2 * WP.M() * WM.M()))
        P1 = ( (2 * ghWW * WP.M() * WP.M()) / ((WP.M() * WP.M() - MW*MW)*(WP.M() * WP.M() - MW * MW) + WW * WW * MW * MW))
        P2 = ( (2 * ghWW * WM.M() * WM.M()) / ((WM.M() * WM.M() - MW*MW)*(WM.M() * WM.M() - MW * MW) + WW * WW * MW * MW))
        ALL2 = 4 * K*K * P1 * P2 * (cL*cL + cR*cR)*(cL*cL + cR*cR) * ROOT.Math.sin(theta_Wp_star)*ROOT.Math.sin(theta_Wp_star) * ROOT.Math.sin(theta_Wm_star)*ROOT.Math.sin(theta_Wm_star)
        
        #/////////////////////////////////////
        #//             |A++|^2             //
        #/////////////////////////////////////
        
        plus1 = cL*cL*cL*cL * (1 + ROOT.Math.cos(theta_Wp_star))*(1 + ROOT.Math.cos(theta_Wp_star)) * (1 + ROOT.Math.cos(theta_Wm_star))*(1 + ROOT.Math.cos(theta_Wm_star))
        plus2 = cR*cR*cR*cR * (1 - ROOT.Math.cos(theta_Wp_star))*(1 - ROOT.Math.cos(theta_Wp_star)) * (1 - ROOT.Math.cos(theta_Wm_star))*(1 - ROOT.Math.cos(theta_Wm_star))
        plus3 = cR*cR*cL*cL * (1 + ROOT.Math.cos(theta_Wp_star))*(1 + ROOT.Math.cos(theta_Wp_star)) * (1 - ROOT.Math.cos(theta_Wm_star))*(1 - ROOT.Math.cos(theta_Wm_star))
        plus4 = cR*cR*cL*cL * (1 - ROOT.Math.cos(theta_Wp_star))*(1 - ROOT.Math.cos(theta_Wp_star)) * (1 + ROOT.Math.cos(theta_Wm_star))*(1 + ROOT.Math.cos(theta_Wm_star))
        
        App2 = P1 * P2 * (plus1 + plus2 + plus3 + plus4);
        
        #/////////////////////////////////////
        #//             |A--|^2             //
        #/////////////////////////////////////
        
        minus1 = cL*cL*cL*cL * (1 - ROOT.Math.cos(theta_Wp_star))*(1 - ROOT.Math.cos(theta_Wp_star)) * (1 - ROOT.Math.cos(theta_Wm_star))*(1 - ROOT.Math.cos(theta_Wm_star))
        minus2 = cR*cR*cR*cR * (1 + ROOT.Math.cos(theta_Wp_star))*(1 + ROOT.Math.cos(theta_Wp_star)) * (1 + ROOT.Math.cos(theta_Wm_star))*(1 + ROOT.Math.cos(theta_Wm_star))
        minus3 = cR*cR*cL*cL * (1 + ROOT.Math.cos(theta_Wp_star))*(1 + ROOT.Math.cos(theta_Wp_star)) * (1 - ROOT.Math.cos(theta_Wm_star))*(1 - ROOT.Math.cos(theta_Wm_star))
        minus4 = cR*cR*cL*cL * (1 - ROOT.Math.cos(theta_Wp_star))*(1 - ROOT.Math.cos(theta_Wp_star)) * (1 + ROOT.Math.cos(theta_Wm_star))*(1 + ROOT.Math.cos(theta_Wm_star))
        
        Amm2 = P1 * P2 * (minus1 + minus2 + minus3 + minus4)
        
        #/////////////////////////////////////
        #//            2Re(ALL++)           //
        #/////////////////////////////////////
        
        ReALLpp = -4 * K * P1 * P2 * (plus1 + plus2 - plus3 - plus4) * ROOT.Math.sin(theta_Wp_star) * ROOT.Math.sin(theta_Wm_star) * ROOT.Math.cos(dphill)
        
        #/////////////////////////////////////
        #//            2Re(ALL--)           //
        #/////////////////////////////////////
        
        ReALLmm = -4 * K * P1 * P2 * (minus1 + minus2 - minus3 - minus4) * ROOT.Math.sin(theta_Wp_star) * ROOT.Math.sin(theta_Wm_star) * ROOT.Math.cos(dphill)
      
        #/////////////////////////////////////
        #//            2Re(A++--)           //
        #/////////////////////////////////////
        
        ReAppmm = 2 * P1 * P2 * (cL*cL + cR*cR)*(cL*cL + cR*cR) * ROOT.Math.sin(theta_Wp_star)*ROOT.Math.sin(theta_Wp_star) * ROOT.Math.sin(theta_Wm_star)*ROOT.Math.sin(theta_Wm_star) * ROOT.Math.cos(2*dphill)
        
        
        #/////////////////////////////////////
        #//             |ATT|^2             //
        #/////////////////////////////////////
        
        ATT2 = App2 + Amm2 + ReAppmm
        
        
        # Final weights
        
        Higgs_WW_LL = ALL2 / (ALL2 + ATT2 + ReALLpp + ReALLmm)   
        Higgs_WW_TT = ATT2 / (ALL2 + ATT2 + ReALLpp + ReALLmm)

        
  
        self.out.fillBranch('Higgs_WW_LL', Higgs_WW_LL)
        self.out.fillBranch('Higgs_WW_TT', Higgs_WW_TT)

        return True
