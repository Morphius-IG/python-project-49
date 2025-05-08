install: #Синхронизация при клонировании
	uv sync
brain-games: #Запуск игры
	uv run brain-games
build: #Сборка проекта
	uv build
package-install: #Установка проекта
	uv tool install dist/*.whl
