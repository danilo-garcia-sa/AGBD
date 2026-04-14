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

SELECT at.name, t.name, t.Milliseconds, a.Title, g.Name FROM albums a JOIN tracks t ON a.AlbumId = t.AlbumId 
JOIN genres g ON t.GenreId = g.GenreId 
JOIN artists at ON a.ArtistId = at.ArtistId 
WHERE t.name ORDER BY t.Milliseconds ASC LIMIT 20