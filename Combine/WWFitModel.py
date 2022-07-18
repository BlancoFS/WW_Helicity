from HiggsAnalysis.CombinedLimit.PhysicsModel import *
import re

##-------------------------------------
##-------------------------------------
##-------------------------------------

class WHelicityFitModel(PhysicsModel):
    def __init__(self):
        PhysicsModel.__init__(self)
        # -- Variables definition
        self.FR_MC = float(0.002)
        self.FL_MC = float(0.224)
        self.F0_MC = float(0.774)
        self.ModCase = str("SignalStrength")

    def setPhysicsOptionsBase(self,physOptions):
        "Receive a list of strings with the physics options from command line"                

        for po in physOptions:
            # Model Case
            if po.startswith("ModCase"): 
                self.ModCase = str((po.replace("ModCase=","").split(","))[0])
            # -- MC Parameters
            if po.startswith("FR_MC"): 
                self.FR_MC = float((po.replace("FR_MC=","").split(","))[0])
            if po.startswith("FL_MC"): 
                self.FL_MC = float((po.replace("FL_MC=","").split(","))[0])
            if po.startswith("F0_MC"): 
                self.F0_MC = float((po.replace("F0_MC=","").split(","))[0])

        print "Model SetUp: " 
        print "Model case set to " + str(self.ModCase) 
        print "FR(MC) set to "     + str(self.FR_MC) 
        print "FL(MC) set to "     + str(self.FL_MC) 
        print "F0(MC) set to "     + str(self.F0_MC) 

        pass

    def doParametersOfInterestBase(self):
        """Create POI and other parameters, and define the POI set."""

        # -- Create Variables
        self.modelBuilder.doVar("FR_MC[%s]" % (self.FR_MC));
        self.modelBuilder.doVar("FL_MC[%s]" % (self.FL_MC));
        self.modelBuilder.doVar("F0_MC[%s]" % (self.F0_MC));

    def getYieldScale(self,bin,process):
        "Return the name of a RooAbsReal to scale this yield by or the two special values 1 and 0 (don't scale, and set to zero)"

        # if process.startswith('F0_'):
        if process.count('CP5_ttbarSgn-F0'):
            print "Process " + str(process) + " for " + str(bin) + " is scaled by F_0"
            return "r_F0"
        # if process.startswith('FL_'):
        if process.count('CP5_ttbarSgn-FL'):
            print "Process " + str(process) + " for " + str(bin) + " is scaled by F_L"
            return "r_FL"
        # if process.startswith('FR_'):
        if process.count('CP5_ttbarSgn-FR'):
            print "Process " + str(process) + " for " + str(bin) + " is scaled by F_R"
            return "r_FR"
        else:
            print "Process " + str(process) + " for " + str(bin) + " is scaled by 1.0 (Background)"
            return 1

##-------------------------------------
##-------------------------------------

class WHelicityModel( WHelicityFitModel):
    def __init__(self):
         WHelicityFitModel.__init__(self)

    def setPhysicsOptions(self,physOptions):
        self.setPhysicsOptionsBase(physOptions)

    def doParametersOfInterest(self):
        self.doParametersOfInterestBase()

        # -- POIs
        print "Creating fit variables..."
        # Original
        # self.modelBuilder.doVar("F0_Fit[%s,0.50,  0.90]" % (self.F0_MC));
        # self.modelBuilder.doVar("FL_Fit[%s,0.10,  0.40]" % (self.FL_MC));
        # self.modelBuilder.doVar("FR_Fit[%s,0.0001,0.10]" % (self.FR_MC));
        # Extreme
        # self.modelBuilder.doVar("F0_Fit[%s,0.01,  0.90]" % (self.F0_MC));
        # self.modelBuilder.doVar("FL_Fit[%s,0.001, 0.90]" % (self.FL_MC));
        # self.modelBuilder.doVar("FR_Fit[%s,0.0001,0.10]" % (self.FR_MC));
        # Fraction
        self.modelBuilder.doVar("F0_Fit[%s,%s,%s]" % (self.F0_MC,(self.F0_MC-self.F0_MC*0.20),(self.F0_MC+self.F0_MC*0.20)));
        self.modelBuilder.doVar("FL_Fit[%s,%s,%s]" % (self.FL_MC,(self.FL_MC-self.FL_MC*0.20),(self.FL_MC+self.FL_MC*0.20)));
        self.modelBuilder.doVar("FR_Fit[%s,%s,%s]" % (self.FR_MC,(self.FR_MC-self.FR_MC*0.99),(self.FR_MC+self.FR_MC*10.0)));
        #self.modelBuilder.doVar("FR_Fit[%s]" % (self.FR_MC));
        
        # -- Model
        print "Creating model..."

        # -- Factors affecting each TOP category
        if self.ModCase=='MCFractions':            
            self.modelBuilder.factory_("expr::r_F0(\"(@0/%s)\",F0_Fit)" % (self.F0_MC))
            self.modelBuilder.factory_("expr::r_FL(\"(@0/%s)\",FL_Fit)" % (self.FL_MC))
            self.modelBuilder.factory_("expr::r_FR(\"(@0/%s)\",FR_Fit)" % (self.FR_MC))

            self.modelBuilder.doSet("POI","F0_Fit,FL_Fit,FR_Fit")

        if self.ModCase=='MCFractionswK':
            self.modelBuilder.factory_("expr::Xsec(\"(@0+@1+@2)/(@3+@4+@5)\",F0_Fit,FL_Fit,FR_Fit,F0_MC,FL_MC,FR_MC)")

            self.modelBuilder.factory_("expr::r_F0(\"(@0/%s)*@1\",F0_Fit,Xsec)" % (self.F0_MC))
            self.modelBuilder.factory_("expr::r_FL(\"(@0/%s)*@1\",FL_Fit,Xsec)" % (self.FL_MC))
            self.modelBuilder.factory_("expr::r_FR(\"(@0/%s)*@1\",FR_Fit,Xsec)" % (self.FR_MC))
        
            self.modelBuilder.doSet("POI","F0_Fit,FL_Fit,FR_Fit")

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

        if self.ModCase=='MCFractionsNormFRwK':
            self.modelBuilder.doVar("Xsec[1.,0.90,  1.10]");

            self.modelBuilder.factory_("expr::r_F0(\"(@0/%s)*@1\",F0_Fit,Xsec)" % (self.F0_MC))
            self.modelBuilder.factory_("expr::r_FL(\"(@0/%s)*@1\",FL_Fit,Xsec)" % (self.FL_MC))
            self.modelBuilder.factory_("expr::r_FR(\"(1.-(@0+@1))/%s\",F0_Fit,FL_Fit)" % (self.FR_MC))

            self.modelBuilder.doSet("POI","F0_Fit,FL_Fit,Xsec")

##-------------------------------------

WHelicityModel = WHelicityModel()
