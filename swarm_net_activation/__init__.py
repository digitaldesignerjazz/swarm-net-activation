"""
swarm-net-activation: SolNetP2P Swarm Net Activation System
Innovative decentralized agent swarm activation, orchestration & emergence engine.
Native to SolNetP2P, NovaNet, QNET.

Version: 0.1.0
"""

__version__ = "0.1.0"

from .agent import Agent, Role
from .swarm import SwarmOrchestrator
from .communication import InMemoryTransport, Transport
from .intelligence import PheromoneSystem, BiddingSystem, ConsensusEngine, EvolutionaryEngine
from .solnet_integration import SolNetP2PNode, activate_swarm

__all__ = [
    "Agent", "Role",
    "SwarmOrchestrator",
    "Transport", "InMemoryTransport",
    "PheromoneSystem", "BiddingSystem", "ConsensusEngine", "EvolutionaryEngine",
    "SolNetP2PNode", "activate_swarm",
]