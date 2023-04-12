from HiggsAnalysis.CombinedLimit.PhysicsModel import *

##-------------------------------------
##--------- Higgs HELCITY -------------
##-------------------------------------


class Higgshelicity(PhysicsModel):
    def __init__(self):
        self.isFraction = False
        self.isXsec = False
        self.isInt = False
        self.isIntXsec = False        
        self.poiMap = []
        self.pois = {}
        self.verbose = False
        self.xsec= 1.0 

    def setModelBuilder(self, modelBuilder):
        PhysicsModel.setModelBuilder(self,modelBuilder)
        self.modelBuilder.doModelBOnly = False
 
    def getYieldScale(self,bin,process):
        if process == "ggH_HWLWL": return "ggH_LL_func"
        elif process == "ggH_HWTWT": return "ggH_TT_func"
        elif process == "ggH_hww": return "ggH_sbi_func"
        elif process == "ggH_HWW_Int": return "ggH_Int_func"
        #elif process in ["ggH","qqH","ttH","WH","ZH","VH"]: return "CMS_zz4l_mu"
        else:
            return 1
            

    def setPhysicsOptions(self,physOptions):
        for po in physOptions:
            if po == "doFitFractions":
                print("Will consider cards in 2l2nu style (separated S, B, S+B+I)")
                self.isFraction = True
            if po == "doFitXsec":
                print("Will consider cards in 2l2nu+xs style (separated S, B, S+B+I) using xsec normalization")
                self.isXsec = True
            if po == "doInter":
                print("Will consider cards in interference style (separated S, B, I)")
                self.isInt = True
            if po == "doIntXsec":
                print("Will consider cards in interference+xs style (separated S, B, I with constrain to the xsec)")
                self.isIntXsec = True


    def setXsec(self):
        self.xsec = 1.32200
        self.xsec_LL = 1.3200  * 0.42967
        self.xsec_TT = 1.3200  * 0.3809
        self.xsec_Int = 1.3200 * 0.1893
        self.FLL_MC  = 0.42967
        self.FTT_MC  = 0.3809
        self.FInt_MC = 0.1893



    def doParametersOfInterest(self):
        """Create POI and other parameters, and define the POI set."""

        if self.isFraction:
            
            self.setXsec()

            #self.modelBuilder.doVar("FLL_Fit[%s,%s,%s]" % (self.FLL_MC,(self.FLL_MC-self.FLL_MC*0.50),(self.FLL_MC+self.FLL_MC*0.50)));
            #self.modelBuilder.doVar("FTT_Fit[%s,%s,%s]" % (self.FTT_MC,(self.FTT_MC-self.FTT_MC*0.50),(self.FTT_MC+self.FTT_MC*0.50)));

            self.modelBuilder.doVar("FLL_Fit[%s,%s,%s]" % (self.FLL_MC, 0.0, 100))
            self.modelBuilder.doVar("FTT_Fit[%s,%s,%s]" % (self.FTT_MC, 0.0, 100))

            self.modelBuilder.doVar("expr::r_LL(\"(@0/%s)\", FLL_Fit)" % (self.FLL_MC))
            self.modelBuilder.doVar("expr::r_TT(\"(@0/%s)\", FTT_Fit)" % (self.FTT_MC))

            self.modelBuilder.factory_( "expr::ggH_LL_func(\"@0-sqrt(@0*@1)\", r_LL,r_TT)")
            self.modelBuilder.factory_( "expr::ggH_TT_func(\"@1-sqrt(@0*@1)\", r_LL,r_TT)")
            self.modelBuilder.factory_( "expr::ggH_sbi_func(\"sqrt(@0*@1)\", r_LL,r_TT)")
            
            poi = "FLL_Fit,FTT_Fit"

        if self.isXsec:

            self.setXsec()
            
            self.modelBuilder.doVar("Xsec[1.,0.0,  10]");
            
            #self.modelBuilder.doVar("FLL_Fit[%s,%s,%s]" % (self.FLL_MC,(self.FLL_MC-self.FLL_MC*0.50),(self.FLL_MC+self.FLL_MC*0.50)));
            #self.modelBuilder.doVar("FTT_Fit[%s,%s,%s]" % (self.FTT_MC,(self.FTT_MC-self.FTT_MC*0.50),(self.FTT_MC+self.FTT_MC*0.50)));

            self.modelBuilder.doVar("FLL_Fit[%s,%s,%s]" % (self.FLL_MC, 0.0, 100))
            self.modelBuilder.doVar("FTT_Fit[%s,%s,%s]" % (self.FTT_MC, 0.0, 100))

            self.modelBuilder.doVar("expr::r_LL(\"(@0/%s)*@1\", FLL_Fit,Xsec)" % (self.FLL_MC))
            self.modelBuilder.doVar("expr::r_TT(\"(@0/%s)*@1\", FTT_Fit,Xsec)" % (self.FTT_MC))

            self.modelBuilder.factory_( "expr::ggH_LL_func(\"@0-sqrt(@0*@1)\", r_LL,r_TT)")
            self.modelBuilder.factory_( "expr::ggH_TT_func(\"@1-sqrt(@0*@1)\", r_LL,r_TT)")
            self.modelBuilder.factory_( "expr::ggH_sbi_func(\"sqrt(@0*@1)\", r_LL,r_TT)")

            poi = "FLL_Fit,FTT_Fit,Xsec"

        if self.isInt:

            self.setXsec()

            #self.modelBuilder.doVar("FLL_Fit[%s,%s,%s]" % (self.FLL_MC,(self.FLL_MC-self.FLL_MC*0.50),(self.FLL_MC+self.FLL_MC*0.50)));
            #self.modelBuilder.doVar("FTT_Fit[%s,%s,%s]" % (self.FTT_MC,(self.FTT_MC-self.FTT_MC*0.50),(self.FTT_MC+self.FTT_MC*0.50)));
            #self.modelBuilder.doVar("FInt_Fit[%s,%s,%s]" % (self.FInt_MC,(self.FInt_MC-self.FInt_MC*0.50),(self.FInt_MC+self.FInt_MC*0.50)));

            self.modelBuilder.doVar("FLL_Fit[%s,%s,%s]" % (self.FLL_MC, 0.0, 100))
            self.modelBuilder.doVar("FTT_Fit[%s,%s,%s]" % (self.FTT_MC, 0.0, 100))
            self.modelBuilder.doVar("FInt_Fit[%s,%s,%s]" % (self.FInt_MC, 0.0, 100))

            #self.modelBuilder.factory_("expr::Xsec(\"(@0+@1+@2)/(@3+@4+@5)\",FLL_Fit,FTT_Fit,FInt_Fit,FLL_MC,FTT_MC,FInt_MC)")

            self.modelBuilder.doVar("expr::r_LL(\"(@0/%s)\", FLL_Fit)" % (self.FLL_MC))
            self.modelBuilder.doVar("expr::r_TT(\"(@0/%s)\", FTT_Fit)" % (self.FTT_MC))
            self.modelBuilder.doVar("expr::r_Int(\"(@0/%s)\", FInt_Fit)" % (self.FInt_MC))

            self.modelBuilder.factory_( "expr::ggH_LL_func(\"@0\", r_LL)")
            self.modelBuilder.factory_( "expr::ggH_TT_func(\"@0\", r_TT)")
            self.modelBuilder.factory_( "expr::ggH_Int_func(\"@0\", r_Int)")

            poi = "FLL_Fit,FTT_Fit,FInt_Fit"

        if self.isIntXsec:

            self.setXsec()

            self.modelBuilder.doVar("Xsec[1.,0.80,  1.20]");

            self.modelBuilder.doVar("FLL_Fit[%s,%s,%s]" % (self.FLL_MC,(self.FLL_MC-self.FLL_MC*0.50),(self.FLL_MC+self.FLL_MC*0.50)));
            self.modelBuilder.doVar("FTT_Fit[%s,%s,%s]" % (self.FTT_MC,(self.FTT_MC-self.FTT_MC*0.50),(self.FTT_MC+self.FTT_MC*0.50)));
            self.modelBuilder.doVar("FInt_Fit[%s,%s,%s]" % (self.FInt_MC,(self.FInt_MC-self.FInt_MC*0.50),(self.FInt_MC+self.FInt_MC*0.50)));

            self.modelBuilder.doVar("expr::r_LL(\"(@0/%s)*@1\", FLL_Fit,Xsec)" % (self.FLL_MC))
            self.modelBuilder.doVar("expr::r_TT(\"(@0/%s)*@1\", FTT_Fit,Xsec)" % (self.FTT_MC))
            self.modelBuilder.doVar("expr::r_Int(\"(1.-(@0+@1)/%s)\", FLL_Fit,FTT_Fit)" % (self.FInt_MC))

            self.modelBuilder.factory_( "expr::ggH_LL_func(\"@0\", r_LL)")
            self.modelBuilder.factory_( "expr::ggH_TT_func(\"@0\", r_TT)")
            self.modelBuilder.factory_( "expr::ggH_Int_func(\"@0\", r_Int)")
            
            poi = "FLL_Fit,FTT_Fit,Xsec"

            
        self.modelBuilder.doSet("POI",poi)


higgshelicity = Higgshelicity()
