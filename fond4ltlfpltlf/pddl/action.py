# -*- coding: utf-8 -*-

"""This module contains the implementations of a PDDL Action."""


from fond4ltlfpltlf.pddl.formulas import FormulaAnd, FormulaOneOf
from fond4ltlfpltlf.pddl.literal import Literal
from fond4ltlfpltlf.pddl.predicate import Predicate


class Action:
    """A class for the PDDL Action."""

    def __init__(self, name, parameters, preconditions, effects):
        """Initialize the formula."""
        self.name = name  # string
        self.parameters = parameters  # list
        self.preconditions = preconditions  # formula.FormulaXXX
        self.effects = effects  # formula.FormulaXXX

    def __str__(self):
        """Get the string."""
        operator_str = "{0}\n".format(self.name)
        operator_str += "\t:parameters ({0})\n".format(
            " ".join(map(str, self.parameters))
        )
        operator_str += "\t:precondition {0}\n".format(self.preconditions)
        operator_str += "\t:effect {0}\n".format(self.effects)
        return operator_str

    def add_to_precond(self):
        """Modify action preconditions."""
        if isinstance(self.preconditions, FormulaAnd):
            self.preconditions.complete_domain_turn(True)
        else:
            old_formula = self.preconditions
            precond_to_be_added = Literal.positive(Predicate("turnDomain"))
            self.preconditions = FormulaAnd([old_formula, precond_to_be_added])

    def add_to_effect(self):
        """Modify action effects."""
        if isinstance(self.effects, FormulaAnd):
            self.effects.complete_domain_turn(False)
        else:
            old_formula = self.effects
            effect_to_be_added = Literal.negative(Predicate("turnDomain"))
            self.effects = FormulaAnd([old_formula, effect_to_be_added])

    def add_turn_domain(self):
        """Add turn domain predicate."""
        self.add_to_precond()
        self.add_to_effect()

    def isOneOf(self):
        """Check if there is a OneOf formula."""
        if isinstance(self.effects, FormulaOneOf):
            return True
        else:
            return False
