from HiggsAnalysis.CombinedLimit.PhysicsModel import *
import re

##-------------------------------------
##-------------------------------------
##-------------------------------------

class WWHelicityFitModel(PhysicsModel):
    def __init__(self):
        PhysicsModel.__init__(self)
        # -- Variables definition
        self.FLL_MC = float(0.3743)
        self.FTT_MC = float(0.1509)
        self.FTL_MC = float(0.2378)
        self.FLT_MC = float(0.2378)
        self.ModCase = str("SignalStrength")

    def setPhysicsOptionsBase(self,physOptions):
        "Receive a list of strings with the physics options from command line"                

        for po in physOptions:
            # Model Case
            if po.startswith("ModCase"): 
                self.ModCase = str((po.replace("ModCase=","").split(","))[0])
            # -- MC Parameters
            if po.startswith("FLL_MC"): 
                self.FLL_MC = float((po.replace("FLL_MC=","").split(","))[0])
            if po.startswith("FTT_MC"): 
                self.FTT_MC = float((po.replace("FTT_MC=","").split(","))[0])
            if po.startswith("FTL_MC"): 
                self.FTL_MC = float((po.replace("FTL_MC=","").split(","))[0])
            if po.startswith("FLT_MC"): 
                self.FLT_MC = float((po.replace("FLT_MC=","").split(","))[0])

        print "Model SetUp: " 
        print "Model case set to " + str(self.ModCase) 
        print "FLL(MC) set to "     + str(self.FLL_MC) 
        print "FTT(MC) set to "     + str(self.FTT_MC) 
        print "FTL(MC) set to "     + str(self.FTL_MC)
        print "FLT(MC) set to "     + str(self.FLT_MC)

        pass

    def doParametersOfInterestBase(self):
        """Create POI and other parameters, and define the POI set."""

        # -- Create Variables
        self.modelBuilder.doVar("FLL_MC[%s]" % (self.FLL_MC));
        self.modelBuilder.doVar("FTT_MC[%s]" % (self.FTT_MC));
        self.modelBuilder.doVar("FTL_MC[%s]" % (self.FTL_MC));
        self.modelBuilder.doVar("FLT_MC[%s]" % (self.FLT_MC));

    def getYieldScale(self,bin,process):
        "Return the name of a RooAbsReal to scale this yield by or the two special values 1 and 0 (don't scale, and set to zero)"

        # if process.startswith('FLL_'):
        if process.count('HWLWL'):
            print "Process " + str(process) + " for " + str(bin) + " is scaled by F_LL"
            return "r_FLL"
        # if process.startswith('FTT_'):
        if process.count('HWTWT'):
            print "Process " + str(process) + " for " + str(bin) + " is scaled by F_TT"
            return "r_FTT"
        # if process.startswith('FTL_'):
        if process.count('HWTWL'):
            print "Process " + str(process) + " for " + str(bin) + " is scaled by F_TL"
            return "r_FTL"
        if process.count('HWLWT'):
            print "Process " + str(process) + " for " + str(bin) + " is scaled by F_LT"
            return "r_FLT"
        else:
            print "Process " + str(process) + " for " + str(bin) + " is scaled by 1.0 (Background)"
            return 1

##-------------------------------------
##-------------------------------------

class WWHelicityModel( WWHelicityFitModel):
    def __init__(self):
         WWHelicityFitModel.__init__(self)

    def setPhysicsOptions(self,physOptions):
        self.setPhysicsOptionsBase(physOptions)

    def doParametersOfInterest(self):
        self.doParametersOfInterestBase()

        # -- POIs
        print "Creating fit variables..."
        # Original
        # self.modelBuilder.doVar("FLL_Fit[%s,0.10,  0.50]" % (self.FLL_MC));
        # self.modelBuilder.doVar("FTT_Fit[%s,0.05,  0.50]" % (self.FTT_MC));
        # self.modelBuilder.doVar("FTL_Fit[%s,0.10,  0.70]" % (self.FTL_MC));
        # self.modelBuilder.doVar("FLT_Fit[%s,0.10,  0.70]" % (self.FLT_MC));
        # Extreme
        # self.modelBuilder.doVar("FLL_Fit[%s,0.05,  0.90]" % (self.FLL_MC));
        # self.modelBuilder.doVar("FTT_Fit[%s,0.05,  0.90]" % (self.FTT_MC));
        # self.modelBuilder.doVar("FTL_Fit[%s,0.05,  0.90]" % (self.FTL_MC));
        # self.modelBuilder.doVar("FLT_Fit[%s,0.05,  0.90]" % (self.FLT_MC));
        # Fraction
        self.modelBuilder.doVar("FLL_Fit[%s,%s,%s]" % (self.FLL_MC,(self.FLL_MC-self.FLL_MC*0.30),(self.FLL_MC+self.FLL_MC*0.30)));
        self.modelBuilder.doVar("FTT_Fit[%s,%s,%s]" % (self.FTT_MC,(self.FTT_MC-self.FTT_MC*0.30),(self.FTT_MC+self.FTT_MC*0.30)));
        self.modelBuilder.doVar("FTL_Fit[%s,%s,%s]" % (self.FTL_MC,(self.FTL_MC-self.FTL_MC*0.30),(self.FTL_MC+self.FTL_MC*0.30)));
        self.modelBuilder.doVar("FLT_Fit[%s,%s,%s]" % (self.FLT_MC,(self.FLT_MC-self.FLT_MC*0.30),(self.FLT_MC+self.FLT_MC*0.30)));
        
        # -- Model
        print "Creating model..."

        # -- Factors affecting each WW category
        if self.ModCase=='MCFractions':            
            self.modelBuilder.factory_("expr::r_FLL(\"(@0/%s)\",FLL_Fit)" % (self.FLL_MC))
            self.modelBuilder.factory_("expr::r_FTT(\"(@0/%s)\",FTT_Fit)" % (self.FTT_MC))
            self.modelBuilder.factory_("expr::r_FLT(\"(@0/%s)\",FLT_Fit)" % (self.FLT_MC))
            self.modelBuilder.factory_("expr::r_FTL(\"(@0/%s)\",FTL_Fit)" % (self.FTL_MC))

            self.modelBuilder.doSet("POI","FLL_Fit,FTT_Fit,FTL_Fit, FLT_Fit")

        if self.ModCase=='MCFractionswK':
            # Does it make sense (@0+@1+@2)/(@3+@4+@5) instead of @0/@3 + @1/@4 + @2/@5
            #self.modelBuilder.factory_("expr::Xsec(\"(@0+@1+@2)/(@3+@4+@5)\",F0_Fit,FL_Fit,FR_Fit,F0_MC,FL_MC,FR_MC)") # Original from Top
            
            self.modelBuilder.factory_("expr::Xsec(\"(@0+@1+@2+@3)/(@4+@5+@6+@7)\",FLL_Fit,FTT_Fit,FTL_Fit,FLT_Fit,FLL_MC,FTT_MC,FTL_MC,FLT_MC)")

            self.modelBuilder.factory_("expr::r_FLL(\"(@0/%s)*@1\",FLL_Fit,Xsec)" % (self.FLL_MC))
            self.modelBuilder.factory_("expr::r_FTT(\"(@0/%s)*@1\",FTT_Fit,Xsec)" % (self.FTT_MC))
            self.modelBuilder.factory_("expr::r_FTL(\"(@0/%s)*@1\",FTL_Fit,Xsec)" % (self.FTL_MC))
            self.modelBuilder.factory_("expr::r_FLT(\"(@0/%s)*@1\",FLT_Fit,Xsec)" % (self.FLT_MC))
        
            self.modelBuilder.doSet("POI","FLL_Fit,FTT_Fit,FTL_Fit,FLT_Fit")

        '''
        if self.ModCase=='MCFractionsNormFR':
            self.modelBuilder.factory_("expr::r_F0(\"(@0/%s)\",F0_Fit)" % (self.F0_MC))
            self.modelBuilder.factory_("expr::r_FL(\"(@0/%s)\",FL_Fit)" % (self.FL_MC))
            self.modelBuilder.factory_("expr::r_FR(\"(1.-(@0+@1))/%s\",F0_Fit,FL_Fit)" % (self.FR_MC))

            self.modelBuilder.doSet("POI","F0_Fit,FL_Fit")

        if self.ModCase=='MCFractionsNormFL':
            self.modelBuilder.factory_("expr::r_F0(\"(@0/%s)\",F0_Fit)" % (self.F0_MC))
            self.modelBuilder.factory_("expr::r_FR(\"(@0/%s)\",FR_Fit)" % (self.FR_MC))
            self.modelBuilder.factory_("expr::r_FL(\"(1.-(@0+@1))/%s\",F0_Fit,FR_Fit)" % (self.FL_MC))

            self.modelBuilder.doSet("POI","F0_Fit,FR_Fit")

        if self.ModCase=='MCFractionsNormF0':
            self.modelBuilder.factory_("expr::r_FR(\"(@0/%s)\",FR_Fit)" % (self.FR_MC))
            self.modelBuilder.factory_("expr::r_FL(\"(@0/%s)\",FL_Fit)" % (self.FL_MC))
            self.modelBuilder.factory_("expr::r_F0(\"(1.-(@0+@1))/%s\",FR_Fit,FL_Fit)" % (self.F0_MC))

            self.modelBuilder.doSet("POI","FL_Fit,FR_Fit")
        '''
        if self.ModCase=='MCFractionsNormFRwK':
            self.modelBuilder.doVar("Xsec[1.,0.80,  1.20]");

            self.modelBuilder.factory_("expr::r_FLL(\"(@0/%s)*@1\",FLL_Fit,Xsec)" % (self.FLL_MC))
            self.modelBuilder.factory_("expr::r_FTT(\"(@0/%s)*@1\",FTT_Fit,Xsec)" % (self.FTT_MC))
            self.modelBuilder.factory_("expr::r_FLT(\"(@0/%s)*@1\",FLT_Fit,Xsec)" % (self.FLT_MC))
            self.modelBuilder.factory_("expr::r_FTL(\"(@0/%s)*@1\",FTL_Fit,Xsec)" % (self.FTL_MC))

            self.modelBuilder.doSet("POI","FLL_Fit,FTT_Fit,FTL_Fit,FLT_Fit,Xsec")
         

##-------------------------------------

WWHelicityModel = WWHelicityModel()
