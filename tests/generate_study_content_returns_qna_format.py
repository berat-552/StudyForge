from backend import content_generator


def test_generate_study_content_returns_qna_format(monkeypatch):
    class FakeResponse:
        class Generations:
            text = "Q: What is Python?\nA: A programming language."
        generations = [Generations()]

    def fake_generate(*args, **kwargs):
        return FakeResponse()

    monkeypatch.setattr(content_generator.co, "generate", fake_generate)

    output = content_generator.generate_study_content("What is Python?")
    assert "Q:" in output
    assert "A:" in output
