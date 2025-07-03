from backend import content_generator


def test_generate_study_content_returns_qna_format():
    class FakeResponse:
        class Generations:
            text = "Q: What is Python?\nA: A programming language."
        generations = [Generations()]

    class FakeCohereClient:
        def generate(self, *args, **kwargs):
            return FakeResponse()

    output = content_generator.generate_study_content("What is Python?", co_client=FakeCohereClient())
    assert "Q:" in output
    assert "A:" in output
