from backend import content_generator
from tests.helpers.fakes import FakeCohereClient


def test_generate_study_content_returns_qna_format():
    mock_output = "Q: What is Python?\nA: A programming language."

    fake_client = FakeCohereClient(mock_output)
    output = content_generator.generate_study_content(
        "What is Python?", co_client=fake_client)

    assert "Q:" in output
    assert "A:" in output
