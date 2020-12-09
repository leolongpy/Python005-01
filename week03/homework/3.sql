SELECT DISTINCT player_id, player_name, count(*) as num #7
FROM player JOIN team ON player.team_id = team.team_id #1
WHERE height > 1.80 #2
GROUP BY player.team_id #3 
HAVING num > 2 #4
ORDER BY num DESC#5 
LIMIT 2#6
