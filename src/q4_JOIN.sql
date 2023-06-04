
SELECT f.carrier, f.tailnum, f.month, f.day
FROM flights f
JOIN planes p
  ON f.tailnum = p.tailnum
WHERE p.manufacturer = 'AIRBUS INDUSTRIE'
ORDER BY f.carrier, f.tailnum, f.month, f.day
LIMIT 10;