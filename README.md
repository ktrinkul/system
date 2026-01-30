## Распределенная система видео аналитики

### API
- POST /scenario/ - инициализация стейт-машины
- POST /scenario/<scenario_id>/ - изменение статуса стейт-машины
- GET /scenario/<scenario_id>/ - информация о текущем статусе сценария
- GET /prediction/<scenario_id>/ - результаты предсказаний

### Orchestrator
- чтение событий (команды) - получение запроса от api
- контроль состояния - сохраненные изменения передача в api (transactional outbox)
- выполнение действий - управление runner

Поддержка следующих статусов:
- init_startup - инициализация запуска
- in_startup_processing - промежуточное состояние
- active - активное состояние
- init_shutdown - инициализация останова
- in_shutdown_processing - промежуточное состояние
- inactive - выключенное состояние

Жизненный цикл контролируется посредством конечного автомата с следующими переходами:
- init_startup → in_startup_processing → active
- init_shutdown → in_shutdown_processing → inactive

### Runner
- чтение кадра - живой поток или заготовленное локальное видео
- предпроцессинг - подготовка полученного кадра
- отправка кадра - отправка кадра в inference
- получение результата - чтение результатов с предсказаниями
- публикация результата - доступность событий на стороннем api

### Inference
- чтение кадра - получение кадра
- предсказание - inference с помощью модели
- отправка результата - возврат результата в runner

### Updates
- Plan for periodic maintenance based on user reports and feedback received to ensure ongoing software quality.