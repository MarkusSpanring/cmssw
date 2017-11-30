##########
# Customisation of tau reco&Id for MiniAOD production
# M. Bluj 
# September 2017
##########
#useRun1FixedStrips=False
useRun1FixedStrips=True
useHybrid = False


print 'Production of PFTaus at MiniAOD with a custom tau setup'


######### Setup a custom PFTau (re)reco
# Build Run-1 fixed size strips
if useRun1FixedStrips:
     print '\tUse Run-1 fixed strips' 
     import RecoTauTag.RecoTau.RecoTauPiZeroBuilderPlugins_cfi as piZeroBuilders
     #modify configuration to be MiniAOD compatible
     piZeroBuilders.modStrips.qualityCuts.primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices")
     #put fixed strip builder to configuration of piZero producer
     process.ak4PFJetsLegacyHPSPiZeros.builders = cms.VPSet(piZeroBuilders.modStrips)

if useHybrid:
     print '\tUse Hybrid strips' 
     import RecoTauTag.RecoTau.RecoTauPiZeroBuilderPlugins_cfi as piZeroBuilders
     process.ak4PFJetsLegacyHPSPiZeros.builders= cms.VPSet(piZeroBuilders.hybridStrip)
     process.ak4PFJetsLegacyHPSPiZeros.builders[0].qualityCuts.primaryVertexSrc = cms.InputTag("offlineSlimmedPrimaryVertices")
     process.ak4PFJetsLegacyHPSPiZeros.jetSrc = cms.InputTag("patAK4PFJets")

process.ak4PFJetsLegacyHPSPiZeros.builders[0].minGammaEtStripSeed = cms.double(2.0)


# Other modifications

#End
