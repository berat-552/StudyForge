from backend import content_generator


def test_generate_study_content_returns_qna_format(monkeypatch):
    class FakeResponse:
        class Generations:
            text = "Q: What is Python?\nA: A programming language."

        generations = [Generations()]

    class FakeCohereClient:

        def generate(self, *args, **kwargs):
            return FakeResponse()

    # Patch the entire cohere client in content_generator
    monkeypatch.setattr(content_generator, "co", FakeCohereClient())

    output = content_generator.generate_study_content("What is Python?")
    assert "Q:" in output
    assert "A:" in output
