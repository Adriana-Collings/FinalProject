import scr.SamplePathClasses as PathCls
import scr.StatisticalClasses as StatCls
import scr.RandomVariantGenerators as rndClasses
import scr.EconEvalClasses as EconCls
import ParameterClasses as P
import InputData as Data


class Patient:
    def __init__(self, id, parameters):
        self._id = id
        self._rng = None
        self._param = parameters
        self._stateMonitor = PatientStateMonitor(parameters)
        self._delta_t = parameters.get_delta_t()

    def simulate(selfself, sim_length):
        self._rng = rndClass.RNG(self._id)
        k = 0
        while self._stateMonitor.get_if_uti() and k*self._delta_t < sim_length:
