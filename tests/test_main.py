"""Test __main__.py."""
from unittest import TestCase

from ansible_lint_plugin.__main__ import main  # pylint: disable=import-error


class TestMain(TestCase):
    """Test __main__.py."""

    def test_main(self) -> None:
        """Execute main() to verify it completes without any errors."""
        main()
