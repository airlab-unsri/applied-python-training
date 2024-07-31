clean-docs:
	@rm -rf docs/_build

build-docs: clean-docs
	@jupyter-book build docs

serve-docs:
	@sphinx-autobuild docs _build/html -b html
