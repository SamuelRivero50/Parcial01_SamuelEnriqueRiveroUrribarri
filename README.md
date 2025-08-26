# Parcial 1 Arquitectura de Software

*Clase:* Arquitectura de Software - S2566-1005

## *Requisitos:*

La alcaldía de Rionegro lo contrata a usted para la elaboración de un software, el cual permita gestionar la información de vuelos (flights) de la ciudad.
  
Un vuelo (flight) tiene: un id (auto-incrementable), un nombre, tipo, y un precio.
  
Nota: el tipo de un vuelo puede ser: “Nacional” o “Internacional”.
  
Cree una aplicación web en Python utilizando django que permita realizar las siguientes acciones:
  
*a.* Database (10%): realice una migración que permita generar automáticamente la tabla vuelo (flight) con sus atributos (columnas).
  
*b.* Zona de inicio (15%): Cree un template inicial que despliegue 3 enlaces, el primero a “registrar vuelos”, el segundo a “listar vuelos” y el tercero a “estadísticas de vuelos”. 
  
*c.* Registrar vuelos (25%). Cree un sistema que permita registrar vuelos. Cree un formulario que pida los datos de los vuelos, y luego regístrelos en la base de datos. Nota: haga las validaciones correspondientes. El tipo lo podría validar solo a nivel de la vista usando un HTML Select.
  
*d.* Listar vuelos (25%). Liste todos los vuelos con los siguientes datos: id, nombre, tipo y precio (ordenados por precio / el de menor precio que aparezca de primero). Para los vuelos tipo “Nacional” muestre el precio en azul. Y para los vuelos tipo “Internacional” muestre el nombre en *negrilla*.
  
*e.* Estadísticas de vuelos (25%). Muestre cuantos vuelos nacionales e internacionales existen registrados en el sistema (por ejemplo: 3 Nacionales, 0 Internacionales). Además, muestre el precio promedio de los vuelos nacionales.
  
*Sugerencia:* no importa si la app se ve visualmente fea (eso no tiene incidencia en la nota).
 

