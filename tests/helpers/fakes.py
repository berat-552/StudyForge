class FakeCohereResponse:
    def __init__(self, text):
        class Generations:
            pass
        gen = Generations()
        gen.text = text
        self.generations = [gen]


class FakeCohereClient:
    def __init__(self, mock_text):
        self.mock_text = mock_text

    def generate(self, *args, **kwargs):
        return FakeCohereResponse(self.mock_text)
