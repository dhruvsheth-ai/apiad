.PHONY: deploy
deploy:
	(cd deploy && mkdocs gh-deploy --config-file ../mkdocs.yml)