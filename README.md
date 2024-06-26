# Branch and Bound

## Ответ DeepSeek номер раз

Функция ``dynamic_branch_and_bound`` используется для решения задачи оптимального размещения грузов в грузовики. Этот метод
является вариантом алгоритма "ветвей и границ" (branch and bound), адаптированного для динамического программирования.
Вот пошаговое объяснение того, что делает эта функция:

1. **Инициализация:**

- Функция принимает список грузов cargos, лучшее найденное решение `best_solution` (изначально это может быть результат
  другого алгоритма, например, first-fit), и начальную вместимость грузовиков `initial_capacity`.
- Грузы сортируются по размеру.
- Создается стек `stack`, в который сначала помещается пара: отсортированный список грузов и пустой список грузовиков.
- Создается список `visited` для отслеживания состояний, которые уже были рассмотрены.

2. **Основной цикл:**

- Пока стек не пуст, извлекается пара `(cargos, trucks)` из стека.
- Если количество грузовиков в текущем решении trucks больше или равно количеству грузовиков в лучшем решении
  `best_solution`, то это решение игнорируется (пропуск).
- Если текущее состояние уже было посещено (проверяется через `state_hash`), то это решение также игнорируется.
- Если список грузов пуст (`len(cargos) == 0`), значит все грузы размещены. Если количество грузовиков в текущем решении
  меньше, чем в лучшем решении, то обновляется лучшее решение.

3. **Разветвление решений:**

- Берётся первый груз из списка `cargos`.
- Создается новое решение, где этот груз помещается в новый грузовик. Новый грузовик добавляется в список `new_trucks`, а
  груз удаляется из списка `new_cargos`. Это новое состояние добавляется обратно в стек.
- Проверяется, можно ли поместить текущий груз в один из уже существующих грузовиков. Если можно, создается новое
  состояние, где груз добавляется в этот грузовик, и это состояние также добавляется в стек.

4. **Завершение:**

- После того как стек становится пустым, функция возвращает лучшее найденное решение, где все грузы размещены с
  минимальным количеством грузовиков.

Этот алгоритм эффективно использует принцип "ветвей и границ", чтобы избежать перебора всех возможных комбинаций грузов
и грузовиков, что было бы чрезвычайно ресурсоёмким.

## Ответ DeepSeek номер два

Алгоритм `dynamic_branch_and_bound` соответствует принципам алгоритма "ветвей и границ" в следующих аспектах:

1. Ветвление (Branching):

Ветвление происходит, когда для каждого груза решается, в какой грузовик его поместить. 
Это приводит к созданию новых состояний, где груз либо помещается в новый грузовик, 
либо добавляется в уже существующий. 
Каждое такое решение порождает новое состояние, которое добавляется в стек `stack`.

2. Границы (Bounding):

Границы устанавливаются путем сравнения количества грузовиков в текущем решении с количеством грузовиков 
в лучшем найденном решении `best_solution`. 
Если текущее решение уже имеет больше или равное количество грузовиков, оно 
отбрасывается, так как не может привести к улучшению лучшего решения.

Дополнительно, использование функции `state_hash` для проверки посещенных 
состояний служит для исключения повторного рассмотрения одних и тех же состояний, 
что экономит вычислительные ресурсы и ускоряет процесс поиска решения.