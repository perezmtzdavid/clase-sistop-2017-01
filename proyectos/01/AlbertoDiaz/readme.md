# Monitor de Recursos
##Autor
Carlos Alberto Díaz Olivares
##Version de Python
Este programa funciona con la versión 2.7 de Python
##Problema a resolver
Este programa busca ser un monitor de recursos de un sistema operativo Linux.
##Logica de Operacion
Se importan los modulos de threading(Implementacion de Hilos), time, commands(Ejecucion y lectura de la resuesta de comandos del Sistema Operativo) y os(Ejecución de comandos del Sistema Operativo) para la programacion del monitor. Se hace uso de un semaforo como señalización entre hilos. Cada opcion te muestra la informacion un total de 10 segundos antes de volver al hilo principal.
##Ejecucion
Solo basta con la ejecucion del siguiente comando en una terminal Linux con python 2.7
	python monitorRecursos.py
##Sitios de Consulta
https://gist.github.com/celtha/1214442
https://www.ibiblio.org/pub/linux/docs/LDP/system-admin-guide/translations/es/html/ch04s07.html