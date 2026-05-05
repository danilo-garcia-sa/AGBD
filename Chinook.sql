--1)--
SELECT FirstName,LastName FROM employees
ORDER BY LastName ASC, FirstName ASC

--2)--
SELECT t.name, t.Milliseconds, a.Title FROM albums a 
JOIN tracks t ON a.AlbumId = t.AlbumId
WHERE a.Title LIKE 'Big Ones' 
ORDER BY t.Milliseconds ASC

--3)--
SELECT UnitPrice, Name FROM tracks 
ORDER BY tracks.UnitPrice ASC LIMIT 10

--4)--
SELECT t.UnitPrice,t.name, a.Title, g.Name FROM albums a 
JOIN tracks t ON a.AlbumId = t.AlbumId 
JOIN genres g ON t.GenreId = g.GenreId 
WHERE t.name AND t.UnitPrice = 0.99

--5)--
SELECT at.name, t.name, t.Milliseconds, a.Title, g.Name FROM albums a 
JOIN tracks t ON a.AlbumId = t.AlbumId 
JOIN genres g ON t.GenreId = g.GenreId 
JOIN artists at ON a.ArtistId = at.ArtistId 
WHERE t.name ORDER BY t.Milliseconds ASC LIMIT 20

--6)--
SELECT emp.LastName AS empleado, jefe.LastName AS jefe, COUNT(*)  FROM employees emp
JOIN employees jefe ON emp.ReportsTo = jefe.EmployeeId
JOIN customers cus ON emp.EmployeeId = cus.SupportRepId
GROUP BY emp.EmployeeId
ORDER BY jefe ASC

--7)--
SELECT emp.FirstName AS Nombre_Empleado, emp.LastName AS Apellido_Empleado, 
cus.FirstName AS Nombre_Cliente, cus.LastName AS Apellido_Cliente
FROM employees emp
JOIN customers cus ON emp.EmployeeId = cus.SupportRepId;

--8)--
SELECT c.FirstName, c.LastName, c.Address, inv.InvoiceDate FROM customers c
JOIN invoices inv ON c.CustomerId = inv.CustomerId

--9)--
SELECT g.name, sum(t.TrackId) AS Canciones FROM genres g 
JOIN tracks t ON g.GenreId = t.GenreId
GROUP by g.GenreId

--10)--
SELECT c.FirstName, inv.InvoiceDate, art.name FROM customers c
JOIN invoices inv ON c.CustomerId = inv.CustomerId
JOIN invoice_items inv_i ON inv.InvoiceId = inv_i.InvoiceId
JOIN tracks t ON inv_i.TrackId = t.TrackId
JOIN albums a ON t.AlbumId = a.AlbumId
JOIN artists art ON a.ArtistId = art.ArtistId
ORDER by c.FirstName ASC

--11)--
SELECT c.FirstName, c.City, t.name AS Song, g.name AS Genre FROM customers c
JOIN invoices inv ON c.CustomerId = inv.CustomerId
JOIN invoice_items inv_i ON inv.InvoiceId = inv_i.InvoiceId
JOIN tracks t ON inv_i.TrackId = t.TrackId
JOIN albums a ON t.AlbumId = a.AlbumId
JOIN artists art ON a.ArtistId = art.ArtistId
JOIN genres g ON t.GenreId = g.GenreId

--12)--
SELECT c.FirstName, c.City, t.name AS Song, g.name AS Genre FROM customers c
JOIN employees emp ON c.SupportRepId = emp.EmployeeId
JOIN invoices inv ON c.CustomerId = inv.CustomerId
JOIN invoice_items inv_i ON inv.InvoiceId = inv_i.InvoiceId
JOIN tracks t ON inv_i.TrackId = t.TrackId
JOIN albums a ON t.AlbumId = a.AlbumId
JOIN artists art ON a.ArtistId = art.ArtistId
JOIN genres g ON t.GenreId = g.GenreId
JOIN playlist_track playlst ON t.TrackId = playlst.TrackId
JOIN playlists plist ON playlst.PlaylistId = plist.PlaylistId
JOIN media_types mt ON t.MediaTypeId = mt.MediaTypeId