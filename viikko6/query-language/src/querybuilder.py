from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or

class QueryBuilder:
    def __init__(self, query = All()):
        self._query = query

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(HasAtLeast(value, attr), self._query))

    def playsIn(self, team):
        return QueryBuilder(And(PlaysIn(team), self._query))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(HasFewerThan(value, attr), self._query))
    
    def build(self):
        return self._query
    
    def oneOf(self, m1, m2):
        return QueryBuilder(Or(m1, m2))