# miniDSP 2x4HD Home Assistant Add-on

1. Сделай fork или создай новый репозиторий с содержимым этого аддона.
2. В Home Assistant: Supervisor -> Add-on store -> Add-on repository -> paste your repo URL.
3. Установи add-on.
4. В `Configuration` Add-on проверь `devices` — если нет доступа к USB, добавь правильные `/dev/hidrawX`.
5. Запусти add-on.
6. API будет доступен на порту 8080 (или через Supervisor web UI). Примеры:

