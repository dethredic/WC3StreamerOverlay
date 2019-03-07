.DEFAULT_GOAL=release

release:
	@echo 'Building bot...'
	@pyinstaller.exe -F -n WC3StreamerOverlay --specpath build src/main.py

	@echo 'Building tests...'
	@pyinstaller.exe -F -n test_1v1 --specpath build tests/test_1v1.py
	@pyinstaller.exe -F -n test_team --specpath build tests/test_team.py

	@echo 'Building client...'
	@cd client; npm install
	@cd client; npm run build
	@mkdir -p dist/client
	@cp -R client/build/* dist/client/

	@echo 'Packaging release...'
	@cp README.md dist
	@cp LICENSE dist
	@cd dist; zip -r WC3StreamerOverlay *

clean:
	rm -rf build
	rm -rf dist
	rm -rf client/build
