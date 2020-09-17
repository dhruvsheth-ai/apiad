.PHONY: deploy
deploy:
	cp Readme.md docs/index.md
	(cd deploy && mkdocs gh-deploy --config-file ../mkdocs.yml && git reset --hard && cd .. && git commit -am "Deployed")