class SampleTooBigException(Exception):
    def __str__(self) -> str:
        return 'The sample size is too big!'
