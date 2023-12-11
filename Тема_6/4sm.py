def employee_movement(log, employee_id):
   indices = [i for i, x in enumerate(log) if x == employee_id]
   if len(indices) < 2:
      return log[indices[0]:] if indices else ()
   else:
      return log[indices[0]:indices[1] + 1]


# Проверка функции на предложенных примерах
print(employee_movement((1, 2, 3), 8))
print(employee_movement((1, 8, 3, 4, 8, 8, 9, 2), 1))
print(employee_movement((1, 2, 8, 5, 1, 2, 9), 2))
