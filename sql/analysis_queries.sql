
SELECT
    u.name,
    COUNT(p.id) AS total_posts
FROM KS_users u
JOIN KS_posts p
    ON u.id = p.userId
GROUP BY u.id, u.name
HAVING COUNT(p.id) > 5
ORDER BY total_posts DESC;