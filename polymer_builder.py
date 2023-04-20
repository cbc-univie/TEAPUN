import sys
import os
sys.path.append("/site/raid3/mazin/TEAPUN/")
from PolymerChain import PolymerChain

###############################
#####################################################################################################################################################################################################################
# code to EXECute#####################################################################################################################################################################################################
#####################################################################################################################################################################################################################
chain = PolymerChain(
    "p1",
    monomers=["AMC"],
    n_of_monomers=[4500],
    toppar="cg_dihe.str",
    #charmm="charmm",
    charmm="charmm_c47_omm_domdecgpu"
)
# chain.build_Monomers(verbose=True)
chain.build_simpleChain(verbose=True, iter=0)  # , random=True)
chain.relax_chain(500_000)
chain.solvate(
    1,
    "BMW",
    "auto",
    #square=True,
    verbose=True,
    boxsize=701,
    build=True,
    salt=False,
    usepdb=True,
        )
chain.equilibrate("p1_in_bmw.psf", "p1_in_bmw.crd", nstep=5_000_000,)
chain.restart(
    "p1_in_bmw.psf",
    "p1.rst",
    uPME=True,
    T=300,
    dt=0.002,
    nstep=5_000_000,
    )
######################################################################################################################################################################################################################
#####################################################################################################################################################################################################################
