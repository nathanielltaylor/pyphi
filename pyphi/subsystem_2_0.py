#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# subsystem_2_0.py

"""Implementation of IIT 2.0"""

import pyphi
from pyphi.distribution import max_entropy_distribution


class Subsystem_2_0:

    def __init__(self, network, state, node_indices):
        self.network = network
        self.state = tuple(state)
        self.node_indices = node_indices

        # IIT 3.0 subsystem used to compute cause repertoires
        # Note that external elements are *not* frozen - that is handled
        # by the `_external_indices=()` argument.
        self._subsystem_3_0 = pyphi.Subsystem(
            self.network, self.state, self.node_indices, _external_indices=())

    def __len__(self):
        return len(self.node_indices)

    def prior_repertoire(self):
        """The a priori repertoire of the system."""
        return max_entropy_distribution(self.node_indices, len(self))

    def posterior_repertoire(self):
        """The a posteriori repertoire of the system."""
        return self._subsystem_3_0.cause_repertoire(self.node_indices,
                                                    self.node_indices)