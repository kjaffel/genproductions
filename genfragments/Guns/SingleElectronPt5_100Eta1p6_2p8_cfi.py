import FWCore.ParameterSet.Config as cms

generator = cms.EDProducer("FlatRandomPtGunProducer",
    PGunParameters = cms.PSet(
        MaxPt = cms.double(100.0),
        MinPt = cms.double(5.0),
        PartID = cms.vint32(11),
        MaxEta = cms.double(2.8),
        MaxPhi = cms.double(3.14159265359),
        MinEta = cms.double(1.6),
        MinPhi = cms.double(-3.14159265359) ## in radians

    ),
    Verbosity = cms.untracked.int32(0), ## set to 1 (or greater)  for printouts

    psethack = cms.string('single electron pt 5 - 100'),
    AddAntiParticle = cms.bool(True),
    firstRun = cms.untracked.uint32(1)
)

