from worker import FlashcardWorker
from unittest.mock import patch, mock_open

import pytest


def test_worker_uses_api():
    # Patch requests.post
    with patch("worker.requests.post") as mock_post:
        mock_response = mock_post.return_value
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {"result": "Q: Test\nA: Answer"}

        # Patch file reading
        with patch("builtins.open", mock_open(read_data="Some input text")):
            worker = FlashcardWorker(file_path="dummy.txt", instruction="simple terms")

            results = {}

            def capture_result(r):
                results["value"] = r

            def capture_error(e):
                pytest.fail(f"Worker emitted error: {e}")

            worker.finished.connect(capture_result)
            worker.error.connect(capture_error)

            worker.run()

            assert results["value"].startswith("Q:")
