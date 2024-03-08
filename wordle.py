class Wordle:

    MAX_ATTEMPT = 6
    WORD_LENGTH = 5

    def __init__(self, secret: str):
        self.secret: str = secret
        self.attempts = []
        pass

    def attempt(self, word: str):
        self.attempts.append(word)

    @property
    def is_solved(self):
        # Check if there's at least one attempt before accessing the last attempt
        if self.attempts and self.attempts[-1] == self.secret:
            return True
        return False

    @property
    def remaining_attempts(self) -> int:
        return self.MAX_ATTEMPT - len(self.attempts)

    @property
    def can_attempt(self):
        return self.remaining_attempts > 0 and not self.is_solved
        pass
