VENV = .venv

$(VENV): setup.cfg
	python3 -m venv $(VENV)
	$(VENV)/bin/pip install -e .
	touch $(VENV)

.PHONY: run
run: $(VENV)
	$(VENV)/bin/python3 main.py