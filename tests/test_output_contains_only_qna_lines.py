from backend import content_generator
from tests.helpers.fakes import FakeCohereClient


def test_generate_study_content_strips_non_qa_lines():
    mock_output = """
        Q: What is Python?
        A: A programming language.
        Let me know if you need more help."""

    fake_client = FakeCohereClient(mock_output)
    output = content_generator.generate_study_content(
        "text", co_client=fake_client)

    for line in output.strip().splitlines():
        clean_line = line.strip()
        assert (clean_line.startswith("Q:")
                or clean_line.startswith("A:")), f"Invalid line: {line}"
