SELECT FirstName,LastName FROM employees
ORDER BY LastName ASC, FirstName ASC

SELECT t.name, t.Milliseconds, a.Title FROM albums a 
JOIN tracks t ON a.AlbumId = t.AlbumId
WHERE a.Title LIKE 'Big Ones' 
ORDER BY t.Milliseconds ASC

SELECT UnitPrice, Name FROM tracks 
ORDER BY tracks.UnitPrice ASC LIMIT 10

SELECT t.UnitPrice,t.name, a.Title, g.Name FROM albums a 
JOIN tracks t ON a.AlbumId = t.AlbumId 
JOIN genres g ON t.GenreId = g.GenreId 
WHERE t.name AND t.UnitPrice = 0.99

SELECT at.name, t.name, t.Milliseconds, a.Title, g.Name FROM albums a 
JOIN tracks t ON a.AlbumId = t.AlbumId 
JOIN genres g ON t.GenreId = g.GenreId 
JOIN artists at ON a.ArtistId = at.ArtistId 
WHERE t.name ORDER BY t.Milliseconds ASC LIMIT 20

SELECT emp.LastName AS empleado, jefe.LastName AS jefe, COUNT(*)  FROM employees emp
JOIN employees jefe ON emp.ReportsTo = jefe.EmployeeId
JOIN customers cus ON emp.EmployeeId = cus.SupportRepId
GROUP BY emp.EmployeeId
ORDER BY jefe ASC

SELECT emp.FirstName AS Nombre_Empleado, emp.LastName AS Apellido_Empleado, 
cus.FirstName AS Nombre_Cliente, cus.LastName AS Apellido_Cliente
FROM employees emp
JOIN customers cus ON emp.EmployeeId = cus.SupportRepId;

SELECT cust.FirstName, cust.LastName, cust.Address, inv.InvoiceDate FROM customers cust
JOIN invoices inv ON cust.CustomerId = inv.CustomerId

SELECT gen.name, sum(tra.TrackId) AS Canciones FROM genres gen 
JOIN tracks tra ON gen.GenreId = tra.GenreId
GROUP by gen.GenreId  
