install: #Синхронизация при клонировании
	uv sync
brain-games: #Запуск игры
	uv run brain-games
build: #Сборка проекта
	uv build
package-install: #Установка проекта
	uv tool install dist/*.whl
package-upgrade: #Переустановка пакета
	uv tool install --force dist/hexlet_code-0.1.0-py3-none-any.whl
lint: # Проверка проекта линтером
	uv run ruff check brain_games
lint_fix: # Исправление ошибок линтером
	uv run ruff check --fix brain_games
rec:
	asciinema rec demo.cast
rec-overwrite:
	asciinema rec demo.cast --overwrite
rec-upload:
	asciinema upload demo.cast