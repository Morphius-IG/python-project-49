install: #Синхронизация при клонировании
	uv sync
brain-games: #Запуск игры
	uv run brain-games
build: #Сборка проекта
	uv build
package-install: #Установка проекта
	uv tool install dist/*.whl
lint: # Проверка проекта линтером
	uv run ruff check brain_games
lint_fix: # Исправление ошибок линтером
	uv run ruff check --fix brain_games
