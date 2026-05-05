/* Selecciona la tabla de “crime_scene_report” y hago un filtro que busque
la persona que coincida la fecha, que tenga el type murder y que viva en sql city */
SELECT * FROM crime_scene_report
WHERE date = 20180115 AND type = 'murder' AND city LIKE 'sql city'

/* Con la info que me dio la anterior sentencia, selecciono la tabla de person 
y me fijo en la en la primera dirección que me dijeron lo ordene del más alto
al mas bajo ya que también había dicho que tenia el numero de la casa mas alto */
SELECT * FROM person
WHERE address_street_name LIKE 'Northwestern Dr'
ORDER BY address_number DESC

/* En este hice lo mismo que en el de arriba solo que esta vez tenía 
el nombre de la persona en vez del número de la casa */
SELECT * FROM person
WHERE address_street_name LIKE 'Franklin Ave' AND name LIKE 'Annabel%'

/* Aca me fije en la tabla de las entrevistas y como antes saque los ids 
de los sospechosos me fije en las entrevistas que les hice */
SELECT * FROM interview
WHERE person_id = 14887 OR person_id = 16371

/* Selecciona la tabla de “get_fit_now_check_in”, lo renombro a gi, 
despues hago 3 joins y los renombró, a la vez un filtro que busque la que 
en membership_id arranque con “48Z%”, ya que tiene el % al final, 
también me voy a membership_status y tiene que tener membresia “gold” 
y además me fijo que en la número de la placa contenga “%H42W%” 
ya que los porcentajes al comienzo y al final indican eso mismo. */
SELECT * FROM get_fit_now_check_in gi
JOIN get_fit_now_member g ON gi.membership_id = g.id
JOIN person p ON g.person_id = p.id
JOIN drivers_license dl ON p.license_id = dl.id
WHERE membership_id LIKE '48Z%' AND membership_status LIKE 'Gold' AND
plate_number LIKE '%H42W%'

/* Aca es lo mismo que arriba solo que en el filtro agregó que se fije que en 
check_in_date que termine con la fecha “%0109” en la que vieron el asesinato */
SELECT * FROM get_fit_now_check_in gi
JOIN get_fit_now_member g ON gi.membership_id = g.id
JOIN person p ON g.person_id = p.id
JOIN drivers_license dl ON p.license_id = dl.id
WHERE membership_id LIKE '48Z%' AND membership_status LIKE 'Gold' AND
plate_number LIKE '%H42W%' AND check_in_date LIKE '%0109'
