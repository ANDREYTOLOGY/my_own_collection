# Домашнее задание к занятию "`Создание собственных модулей`" - `Чернышов Андрей`

### Проверка работы модуля
![ansible 1](https://github.com/ANDREYTOLOGY/terraform-hw/blob/main/img/ansible3-1.png)  
На скриншоте показан первый запуск playbook с использованием модуля.  
Результат: changed=1, что означает создание файла.  

### Проверка идемпотентности
![ansible 1](https://github.com/ANDREYTOLOGY/terraform-hw/blob/main/img/ansible3-2.png)  
Повторный запуск playbook.
Результат: changed=0, что подтверждает, что модуль не вносит изменений при совпадении содержимого.  

### Установка collection
![ansible 1](https://github.com/ANDREYTOLOGY/terraform-hw/blob/main/img/ansible3-4.png)  
На скриншоте показан процесс установки collection из локального архива .tar.gz.  

### Финальный запуск через установленную collection
![ansible 1](https://github.com/ANDREYTOLOGY/terraform-hw/blob/main/img/ansible3-5.png)  
Playbook запускается уже с установленной collection.  
Результат: успешное выполнение без ошибок.

В ходе работы был разработан собственный Ansible module, оформленный в collection.  
Проведена проверка идемпотентности и корректности работы через role и playbook.
