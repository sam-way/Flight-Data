SELECT f.carrier, f.tailnum, f.month, f.day
FROM flights f, planes p
WHERE f.tailnum = p.tailnum
  AND p.manufacturer = 'AIRBUS INDUSTRIE'
ORDER BY f.carrier, f.tailnum, f.month, f.day
LIMIT 10;