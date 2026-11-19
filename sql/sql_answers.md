# SQL Analysis Answers

## Q1. Top 5 users based on average post body length (excluding title)

**Approach:** Join users and posts, calculate the average length of the post body for each user, and return the top five.

**Results:**

| User ID | User Name | Average Body Length |
|---:|---|---:|
| 4 | Patricia Lebsack | 182.3 |
| 1 | Leanne Graham | 164.5 |
| 7 | Kurtis Weissnat | 163.5 |
| 2 | Ervin Howell | 162.9 |
| 5 | Chelsey Dietrich | 162.5 |

## Q2. Average post length including title and body for the top 5 users

**Approach:** Identify the top five users from Q1 and calculate the average combined length of their post titles and bodies.

**Results:**

| User Name | Average Total Post Length |
|---|---:|
| Patricia Lebsack | 217.4 |
| Chelsey Dietrich | 210.9 |
| Ervin Howell | 202.9 |
| Kurtis Weissnat | 200.9 |
| Leanne Graham | 198.3 |

## Q3. Weekday with the most lengthy posts

**Approach:** Use each post ID as the number of days after the UNIX epoch date (1970-01-01). Convert the resulting date to a weekday and count posts with status `lengthy`.

**Result:**

| Weekday | Lengthy Post Count |
|---|---:|
| Wednesday | 12 |

## Conclusion

All three SQL analysis queries were executed successfully against the SQLite database.