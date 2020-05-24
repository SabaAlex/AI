class PopulationTooBigException(Exception):
    def __str__(self) -> str:
        return 'The swarm is too big to insert a new individual!'
