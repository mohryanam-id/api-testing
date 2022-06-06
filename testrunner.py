import pytest

pytest.main(['--html=report.html','--self-contained-html','--json-report','--json-report-file=report.json','--benchmark-histogram'])