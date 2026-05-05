/* En esta sentencia basicamente se fija en la tabla de inhabitant y chequeo cuales
habitantes son amigables */
SELECT * FROM inhabitant WHERE state = 'friendly'

/* En esta haces lo mismo que en la sentencia anteriror pero ahora tiene que cumplir
con que sea herrero de armas y amigable */
SELECT * FROM inhabitant WHERE state = 'friendly' AND job = 'weaponsmith'

/* En esto se fija cuales habitantes son amigables y se fijan que el trabajo 
termine con smith por el porcentaje al comienzo de '%smith' */
SELECT * FROM inhabitant WHERE state = 'friendly' AND job LIKE '%smith'

/* Selecciona la columna personid de la tabla inhabitant y te fijas que haya un nombre
similar o igual a 'stranger' */
SELECT personid FROM inhabitant WHERE name LIKE 'stranger'

/* Selecciona la columna gold de la tabla inhabitant y vuelve 
a chequear si hay un nombre similar o igual a stranger */
SELECT gold FROM inhabitant WHERE name LIKE 'stranger'

/* Selecciona todas las columnas de la tabla ITEM y se fija que ITEMS no tienen dueño */
SELECT * FROM ITEM WHERE owner IS NULL

/* En esta actualiza la tabla item y establece que en los items sin dueño
el dueño sea el 20 que era el personid que te dio lo de inhabitant */
UPDATE item SET owner = 20 WHERE owner is null

/* Selecciona todas las columnas de la tabla inhabitant y se fija cuales habitantes son 
amigables y busca cuales son dealer o merchant */
SELECT * FROM inhabitant WHERE state = 'friendly' AND job LIKE 'dealer' OR job LIKE 'merchant'

/* En esta sentencia haces que los items que sean ring o teapot los establescas a owner 15 */
UPDATE item SET owner = 15 WHERE item LIKE 'ring' or item LIKE 'teapot'

/* En esta sentencia establece 'RealName' como nombre del personid 20 */
UPDATE inhabitant SET name = 'RealName' WHERE personid = 20

/* Selecciona todas las columnas de inhabitant y busca un 
habitante con trabajo baker ordenado del mas barato al mas caro */
SELECT * FROM inhabitant WHERE job LIKE 'baker' ORDER BY GOLD asc

/* Selecciona todas las columnas de inhabitant y busca un habitante con trabajo de piloto */
SELECT * FROM inhabitant WHERE job LIKE 'pilot'