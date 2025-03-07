"""An HTMLTestRunner for Python which renders a nice HTML report for
``unittest`` results."""

from .runner import HTMLTestRunner, TestGroupReport, TestCaseReport
from .result import HTMLTestResult, TestCaseResult
from .status import TestStatus
__all__ = ['HTMLTestRunner']

__author__ = 'Tuan-Phong Nguyen'
__email__ = 'tuanphong94@gmail.com'
__version__ = '0.2.7'
