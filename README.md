# Luminescence

Это репозиторий для рассчета графиков для лабораторной работы "люминесценция" по дисцлине "материалы и технологии фотоники"

Графики автоматически генерируются в готовом виде на основе файлов данных, полученных при выполнении работы.

Порядок действий для получения графиков:
  - клонировать репозиторий на локальный компьютер
  - создать виртуальное окружение при помощи команды `python -m venv myenv`, где `myenv` - имя вашего окружения
  - выполнить команду `pip install -r requirements.txt`, находясь внутри окружения
  - добавить в папку с проектом файлы с данными в формате .txt, полученные при проведении замеров
  - запустить файл `math.py`
  - готово, графики сохранены в папку `output_files`
